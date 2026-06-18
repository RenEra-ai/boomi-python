
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..models import (
    SharedWebServer,
    SharedWebServerBulkRequest,
    SharedWebServerBulkResponse,
)


class SharedWebServerService(BaseService):
    @staticmethod
    def _require_fields(obj, field_names, path):
        missing = [field for field in field_names if not hasattr(obj, field)]
        if missing:
            raise ValueError(
                f"{path} missing required field(s): {', '.join(missing)}"
            )

    @classmethod
    def _validate_shared_web_server_update_body(cls, request_body: SharedWebServer):
        """Guard against a degenerate update body.

        The read model is intentionally tolerant of sparse live GET responses,
        which omit whole sections AND fields within them (verified against the
        live API: a cloud runtime returns only ``cloud_tennant_general``, a
        local runtime only ``general_settings`` — and that section's nested
        objects are themselves sparse). So the natural GET -> modify -> update
        readback must keep working, and deep field validation here would reject
        legitimate updates. We only reject a clearly-empty update — missing
        ``atom_id`` or carrying neither settings section — and leave full field
        validation to the server, which is authoritative.
        """
        if request_body is None:
            return

        cls._require_fields(request_body, ("atom_id",), "request_body")

        # A section set to None serializes away (``_map`` drops None), so check
        # for a non-None value, not mere attribute presence — otherwise
        # SharedWebServer(atom_id="a", cloud_tennant_general=None) would pass the
        # guard yet send an atom-id-only body.
        if (
            getattr(request_body, "cloud_tennant_general", None) is None
            and getattr(request_body, "general_settings", None) is None
        ):
            raise ValueError(
                "request_body must include cloud_tennant_general (cloud runtime) "
                "or general_settings (local runtime)"
            )

    @staticmethod
    def _validate_shared_web_server_update_dict(request_body: dict):
        """Guard against a degenerate JSON-``dict`` update body.

        Mirrors :meth:`_validate_shared_web_server_update_body` for the lossless
        dict path (which does not hydrate the model, so the model-attribute guard
        cannot run). Uses the JSON wire keys: an update is a full document, so it
        must carry ``atomId`` plus a runtime settings section — ``cloudTennantGeneral``
        (cloud runtime) or ``generalSettings`` (local runtime). A section set to
        ``None`` serializes away, so check for a non-None value, not mere key
        presence. Field-level requirements are left to the server.
        """
        if not request_body.get("atomId"):
            raise ValueError("request_body must include atomId")
        if (
            request_body.get("cloudTennantGeneral") is None
            and request_body.get("generalSettings") is None
        ):
            raise ValueError(
                "request_body must include cloudTennantGeneral (cloud runtime) "
                "or generalSettings (local runtime)"
            )

    @cast_models
    def get_shared_web_server(self, id_: str) -> Union[SharedWebServer, str, dict]:
        """Retrieves the details of a Shared Web Server configuration for this atom/cloud ID by its unique ID. The response can be in either XML or JSON format based on your request.

        :param id_: id_
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[SharedWebServer, str, dict]
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/SharedWebServer/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        return self._deserialize_or_raw(SharedWebServer, response, status, content)

    @cast_models
    def update_shared_web_server(
        self, id_: str, request_body: SharedWebServer = None
    ) -> Union[SharedWebServer, str, dict]:
        """Updates a Shared Web Server object based on the supplied Runtime ID.

        :param request_body: The request body., defaults to None
        :type request_body: SharedWebServer, optional
        :param id_: id_
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[SharedWebServer, str, dict]
        """

        Validator(SharedWebServer).is_optional().validate(request_body)
        Validator(str).validate(id_)
        self._validate_shared_web_server_update_body(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/SharedWebServer/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        return self._deserialize_or_raw(SharedWebServer, response, status, content)

    def get_shared_web_server_json(self, id_: str) -> Union[dict, str]:
        """Get a Shared Web Server configuration as a lossless JSON ``dict``.

        Unlike :meth:`get_shared_web_server`, this returns the decoded JSON body
        **as-is** without hydrating the ``SharedWebServer`` model. The typed model
        does not map every cloud-runtime field (e.g. ``externalHost``,
        ``internalHost``, ``sslCertificate``, ``maxNumberOfThreads``); unmapped
        fields land in ``_kwargs`` and ``JsonMap._map()`` drops them, so a
        GET -> mutate -> typed-UPDATE roundtrip would silently strip them. Use this
        method (paired with :meth:`update_shared_web_server_json`) when you need a
        field-faithful full-document update.

        :param id_: id_
        :type id_: str
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        :return: The decoded JSON body (``dict``), or ``str`` for an empty/undecodable 2xx body.
        :rtype: Union[dict, str]
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/SharedWebServer/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .add_header("Accept", "application/json")
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        return self._raw_json_or_error(response, status)

    def update_shared_web_server_json(
        self, id_: str, request_body: dict
    ) -> Union[dict, str]:
        """Update a Shared Web Server configuration from a lossless JSON ``dict``.

        Unlike :meth:`update_shared_web_server`, the ``dict`` body is sent **as-is**
        (no typed-model roundtrip, so no field loss) and the response is returned
        decoded without hydration. Intended for the GET -> mutate -> update flow:
        fetch with :meth:`get_shared_web_server_json`, change the fields you need,
        and POST the whole document back. A dict-shaped degenerate-body guard
        (:meth:`_validate_shared_web_server_update_dict`) mirrors the typed update's
        check — a full-document update must carry ``atomId`` plus a settings section
        (``cloudTennantGeneral`` or ``generalSettings``) — using the JSON wire keys
        rather than the model-attribute guard, which cannot inspect a plain dict.

        :param id_: id_
        :type id_: str
        :param request_body: The full Shared Web Server document as a JSON ``dict``.
        :type request_body: dict
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        :return: The decoded JSON body (``dict``), or ``str`` for an empty/undecodable 2xx body.
        :rtype: Union[dict, str]
        """

        Validator(str).validate(id_)
        Validator(dict).validate(request_body)
        self._validate_shared_web_server_update_dict(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/SharedWebServer/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .add_header("Accept", "application/json")
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        return self._raw_json_or_error(response, status)

    @cast_models
    def bulk_shared_web_server(
        self, request_body: SharedWebServerBulkRequest = None
    ) -> Union[SharedWebServerBulkResponse, str, dict]:
        """To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

        :param request_body: The request body., defaults to None
        :type request_body: SharedWebServerBulkRequest, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[SharedWebServerBulkResponse, str, dict]
        """

        Validator(SharedWebServerBulkRequest).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/SharedWebServer/bulk",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        return self._deserialize_or_raw(SharedWebServerBulkResponse, response, status, content)
