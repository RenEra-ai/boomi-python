
import time
import urllib.request
import urllib.error
from typing import Any, Dict, Tuple, Generator
from enum import Enum

from .default_headers import DefaultHeaders, DefaultHeadersKeys

from ...net.headers.base_header import BaseHeader

from ...net.transport.request import Request
from ...net.transport.response import base_media_type
from ...net.transport.api_error import ApiError
from ...net.transport.utils import parse_xml_to_dict
from ...net.request_chain.request_chain import RequestChain
from ...net.request_chain.handlers.hook_handler import HookHandler
from ...net.request_chain.handlers.http_handler import HttpHandler
from ...net.headers.access_token_auth import AccessTokenAuth
from ...net.headers.basic_auth import BasicAuth
from ...net.request_chain.handlers.retry_handler import RetryHandler


class BaseService:
    """
    A base class for services providing common functionality.

    :ivar str base_url: The base URL for the service.
    :ivar dict _default_headers: A dictionary of default headers.
    """

    def __init__(self, base_url: str) -> None:
        """
        Initializes a BaseService instance.

        :param str base_url: The base URL for the service. Defaults to None.
        """
        self.base_url = base_url
        self._default_headers = DefaultHeaders()
        self._timeout = 60000

        self._update_request_handler()

    def set_access_token(self, access_token: str):
        """
        Sets the access token for the service.
        """
        self._default_headers.set_header(
            DefaultHeadersKeys.ACCESS_AUTH, AccessTokenAuth(access_token)
        )

        return self

    def get_access_token(self) -> BaseHeader:
        """
        Get the access auth header.

        :return: The access auth header.
        :rtype: BaseHeader
        """
        return self._default_headers.get_header(DefaultHeadersKeys.ACCESS_AUTH)

    def set_basic_auth(self, username: str, password: str):
        """
        Sets the username and password for the service.
        """
        self._default_headers.set_header(
            DefaultHeadersKeys.BASIC_AUTH, BasicAuth(username, password)
        )

        return self

    def get_basic_auth(self) -> BaseHeader:
        """
        Get the basic auth header.

        :return: The basic auth header.
        :rtype: BaseHeader
        """
        return self._default_headers.get_header(DefaultHeadersKeys.BASIC_AUTH)

    def set_timeout(self, timeout: int):
        """
        Sets the timeout for the service.

        :param int timeout: The timeout (ms) to be set.
        :return: The service instance.
        """
        self._timeout = timeout
        self._update_request_handler()

        return self

    def get_timeout(self) -> int:
        """
        Get the configured request timeout in milliseconds.

        :return: The timeout in milliseconds.
        :rtype: int
        """
        return self._timeout

    def set_base_url(self, base_url: str):
        """
        Sets the base URL for the service.

        :param str base_url: The base URL to be set.
        """
        self.base_url = base_url

        return self

    def send_request(self, request: Request) -> Tuple[Dict, int, str]:
        """
        Sends the given request.

        :param Request request: The request to be sent.
        :return: The response data.
        :rtype: Tuple[Dict, int, str]
        """
        response = self._request_handler.send(request)
        return (
            response.body,
            response.status,
            # Normalize to the bare media type so services that branch on
            # ``content == "application/xml"`` / ``== "application/json"`` still
            # match when the server adds a charset (e.g. "; charset=UTF-8").
            base_media_type(response.headers.get("Content-Type", "").lower()),
        )

    def send_request_raw(self, request: Request) -> Tuple[bytes, int, str]:
        """Send a request and return the raw, undecoded response body bytes.

        Unlike :meth:`send_request`, this bypasses all content-type-based body
        parsing and text decoding, so opaque payloads (e.g. Component XML) are
        returned byte-for-byte identical to a direct API call. Used by the
        raw-only Component endpoints.

        :param Request request: The request to be sent.
        :return: ``(raw_bytes, status, content_type)``.
        :rtype: Tuple[bytes, int, str]
        """
        response = self._request_handler.send(request)
        return (
            response.raw_body,
            response.status,
            base_media_type(response.headers.get("Content-Type", "").lower()),
        )

    def _deserialize_or_raw(self, model, response, status, content):
        """Deserialize a JSON/XML body onto ``model``; on a 2xx hydration
        failure, return the raw payload instead of raising.

        Boomi can return a sparse or partial 2xx body (omitted required
        fields, an unknown enum value, an unexpected shape) that a strict
        generated model cannot hydrate. Rather than discard a usable success
        response and force callers back to raw transport, any hydration error
        on a 2xx status returns the raw payload (dict/str); on a non-2xx the
        error propagates. Services opting in declare a ``dict`` member in
        their return type. The catch is intentionally broad because nested
        model construction raises several exception types and the goal is to
        never lose a successful response.
        """
        try:
            if content == "application/json":
                return model._unmap(response)
            if content == "application/xml":
                return model._unmap(parse_xml_to_dict(response))
        except Exception:
            if 200 <= status < 300:
                # A 2xx body the transport could not decode (empty body, or a
                # gateway error page served with a JSON/XML content type) arrives
                # as bytes; decode it so the raw fallback stays within the
                # declared str return member instead of leaking a bytes object.
                if isinstance(response, (bytes, bytearray)):
                    return bytes(response).decode("utf-8", errors="replace")
                return response
            raise
        raise ApiError("Error on deserializing the response.", status, response)

    def _raw_json_or_error(self, response, status):
        """Return a successful 2xx body as-is, without hydrating a typed model.

        Used by lossless-JSON endpoints (e.g. ``SharedWebServer``) where a typed
        model roundtrip would silently drop unknown/unmapped fields (they land in
        ``_kwargs`` and ``JsonMap._map()`` skips private attributes). Returning the
        decoded payload (``dict``/``list``/``str``) lets a GET -> mutate -> update
        roundtrip preserve every field. Mirrors :meth:`_deserialize_or_raw`'s
        ``200 <= status < 300`` boundary and bytes->str fallback (an empty/
        undecodable 2xx JSON body arrives as bytes); a non-2xx propagates.
        """
        if 200 <= status < 300:
            if isinstance(response, (bytes, bytearray)):
                return bytes(response).decode("utf-8", errors="replace")
            return response
        raise ApiError("Error on the response.", status, response)

    @staticmethod
    def _require_model_or_dict(request_body, model):
        """Reject a JSON request body that is neither ``None``, a typed ``model``,
        nor a ``dict``.

        ``Validator(Union[model, dict])`` cannot enforce this on its own: its
        oneOf path early-returns primitives (``str``/``int``/``float``/``bool``)
        without raising (see ``one_of_base_model.py``), so a stray primitive would
        otherwise be serialized as the JSON body instead of failing fast. ``None``
        is allowed (the body is optional).
        """
        if request_body is not None and not isinstance(request_body, (model, dict)):
            raise TypeError(
                f"request_body must be {model.__name__} or dict, "
                f"not {type(request_body).__name__}"
            )

    def stream_request(self, request: Request) -> Generator[Dict, None, None]:
        """
        Streams the given request.

        :param Request request: The request to be streamed.
        :return: A generator of the response data.
        :rtype: Generator[Dict, None, None]
        """
        for response in self._request_handler.stream(request):
            yield (
                response.body,
                response.status,
                base_media_type(response.headers.get("Content-Type", "").lower()),
            )

    def get_default_headers(self) -> list:
        """
        Get the default headers.

        :return: A list of the default headers.
        :rtype: list
        """
        return self._default_headers.get_headers()

    def _get_request_handler(self) -> RequestChain:
        """
        Get the request chain.

        :return: The request chain.
        :rtype: RequestChain
        """
        return (
            RequestChain()
            .add_handler(HookHandler())
            .add_handler(RetryHandler())
            .add_handler(HttpHandler(self._timeout))
        )

    def _poll_download_url(
        self, url: str, max_retries: int = 10, initial_delay: float = 2.0
    ) -> bytes:
        """
        Poll a Boomi download URL with authentication until content is ready.

        The Boomi API download pattern returns HTTP 202 while content is being
        prepared, then HTTP 200 with the actual content once ready.

        :param str url: The absolute download URL returned by a create_* method.
        :param int max_retries: Maximum number of polling attempts. Defaults to 10.
        :param float initial_delay: Initial delay in seconds between retries. Defaults to 2.0.
        :return: The raw downloaded content.
        :rtype: bytes
        """
        auth_headers = {}
        basic_auth = self.get_basic_auth()
        if basic_auth is not None:
            auth_headers = basic_auth.get_headers()
        if not auth_headers:
            access_token = self.get_access_token()
            if access_token is not None:
                auth_headers = access_token.get_headers()
        if not auth_headers:
            raise ApiError("No authentication configured for download", 401, None)

        delay = initial_delay
        for attempt in range(max_retries):
            if attempt > 0:
                time.sleep(delay)
                delay = min(delay * 2, 30.0)

            req = urllib.request.Request(url, headers=auth_headers)
            try:
                with urllib.request.urlopen(
                    req, timeout=self._timeout / 1000
                ) as response:
                    status = response.status
                    if status == 202:
                        if attempt < max_retries - 1:
                            continue
                        raise ApiError(
                            f"Download not ready after {max_retries} attempts",
                            202,
                            None,
                        )
                    content = response.read()
                    if len(content) == 0 and attempt < max_retries - 1:
                        continue
                    return content
            except urllib.error.HTTPError as e:
                raise ApiError(f"Download failed with HTTP {e.code}", e.code, None)

        raise ApiError(f"Download timed out after {max_retries} retries", 408, None)

    def _update_request_handler(self) -> None:
        """
        Update the request handler.
        """
        self._request_handler = self._get_request_handler()
