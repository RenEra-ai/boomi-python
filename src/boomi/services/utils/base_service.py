
import time
import urllib.request
import urllib.error
from typing import Any, Dict, Tuple, Generator
from enum import Enum

from .default_headers import DefaultHeaders, DefaultHeadersKeys

from ...net.headers.base_header import BaseHeader

from ...net.transport.request import Request
from ...net.transport.api_error import ApiError
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
            response.headers.get("Content-Type", "").lower(),
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
                response.headers.get("Content-Type", "").lower(),
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
