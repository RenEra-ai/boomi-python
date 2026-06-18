
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.api_error import ApiError
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..net.transport.utils import require_raw_xml
from ..models import (
    OrganizationComponent,
    OrganizationComponentBulkRequest,
    OrganizationComponentQueryConfig,
    OrganizationComponentQueryResponse,
)


class OrganizationComponentService(BaseService):

    def create_organization_component(
        self, request_body: Union[str, bytes] = None
    ) -> bytes:
        """Create an Organization Component from raw XML; return the raw XML response bytes.

        The Organization Component XML is treated as an **opaque** payload: it is
        sent exactly as provided and the response is returned byte-for-byte, with
        no parsing or conversion. Export an existing component via
        ``get_organization_component`` to use as a template.

        :param request_body: Raw Organization Component XML (``str`` or ``bytes``).
        :type request_body: Union[str, bytes]
        :raises UnsafeComponentXmlSerializationError: If a non-raw body is passed.
        :raises ApiError: If the request fails.
        :return: The raw XML response exactly as returned by the API.
        :rtype: bytes
        """

        body = require_raw_xml(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/OrganizationComponent",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_header("Accept", "application/xml")
            .serialize()
            .set_method("POST")
            .set_body(body, "application/xml")
        )

        response, status, _ = self.send_request_raw(serialized_request)
        if 200 <= status < 300:
            return response
        raise ApiError(
            f"Failed to create organization component: HTTP {status}",
            status,
            response,
        )

    def get_organization_component(self, id_: str) -> bytes:
        """Get an Organization Component as raw XML response bytes, without parsing.

        Preserves the exact XML structure returned by the API. A GET specifying
        the ID of a deleted Organization Component retrieves it (with
        ``deleted="true"``).

        :param id_: Organization component ID
        :type id_: str
        :raises ApiError: If the request fails.
        :return: The raw XML response exactly as returned by the API.
        :rtype: bytes
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/OrganizationComponent/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .add_header("Accept", "application/xml")
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request_raw(serialized_request)
        if 200 <= status < 300:
            return response
        raise ApiError(
            f"Failed to get organization component: HTTP {status}",
            status,
            response,
        )

    def update_organization_component(
        self, id_: str, request_body: Union[str, bytes] = None
    ) -> bytes:
        """Update an Organization Component with raw XML; return the raw XML response bytes.

        Full updates only: supply the complete component XML you want persisted.
        The body is sent exactly as provided. An UPDATE specifying the ID of a
        deleted component restores it.

        :param id_: Organization component ID
        :type id_: str
        :param request_body: Raw Organization Component XML (``str`` or ``bytes``).
        :type request_body: Union[str, bytes]
        :raises UnsafeComponentXmlSerializationError: If a non-raw body is passed.
        :raises ApiError: If the request fails.
        :return: The raw XML response exactly as returned by the API.
        :rtype: bytes
        """

        Validator(str).validate(id_)
        body = require_raw_xml(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/OrganizationComponent/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .add_header("Accept", "application/xml")
            .serialize()
            .set_method("POST")
            .set_body(body, "application/xml")
        )

        response, status, _ = self.send_request_raw(serialized_request)
        if 200 <= status < 300:
            return response
        raise ApiError(
            f"Failed to update organization component: HTTP {status}",
            status,
            response,
        )

    def create_organization_component_json(
        self, request_body: Union[OrganizationComponent, dict] = None
    ) -> Union[OrganizationComponent, str, dict]:
        """Create an Organization Component from JSON; return the typed model (or raw payload).

        JSON counterpart of ``create_organization_component`` (raw XML). The body
        may be a typed ``OrganizationComponent`` (serialized via ``_map()``) or a
        plain ``dict``, which is sent **as-is** for a lossless JSON write. The
        response hydrates to ``OrganizationComponent`` when possible, otherwise the
        raw ``dict``/``str`` payload is returned on a 2xx (see ``_deserialize_or_raw``).

        :param request_body: The Organization Component as a typed model or dict., defaults to None
        :type request_body: Union[OrganizationComponent, dict], optional
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        :return: The parsed response data.
        :rtype: Union[OrganizationComponent, str, dict]
        """

        Validator(Union[OrganizationComponent, dict]).is_optional().validate(request_body)
        self._require_model_or_dict(request_body, OrganizationComponent)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/OrganizationComponent",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_header("Accept", "application/json")
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        return self._deserialize_or_raw(OrganizationComponent, response, status, content)

    def get_organization_component_json(
        self, id_: str
    ) -> Union[OrganizationComponent, str, dict]:
        """Get an Organization Component as JSON; return the typed model (or raw payload).

        JSON counterpart of ``get_organization_component`` (raw XML). Sets
        ``Accept: application/json`` and hydrates to ``OrganizationComponent`` when
        possible; a sparse 2xx body (e.g. partial ``OrganizationContactInfo``)
        falls back to the raw ``dict`` rather than raising.

        :param id_: Organization component ID
        :type id_: str
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        :return: The parsed response data.
        :rtype: Union[OrganizationComponent, str, dict]
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/OrganizationComponent/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .add_header("Accept", "application/json")
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        return self._deserialize_or_raw(OrganizationComponent, response, status, content)

    def update_organization_component_json(
        self, id_: str, request_body: Union[OrganizationComponent, dict] = None
    ) -> Union[OrganizationComponent, str, dict]:
        """Update an Organization Component with JSON; return the typed model (or raw payload).

        JSON counterpart of ``update_organization_component`` (raw XML). Full
        updates only: supply the complete component. The body may be a typed
        ``OrganizationComponent`` or a plain ``dict`` (sent as-is for a lossless
        JSON write).

        :param id_: Organization component ID
        :type id_: str
        :param request_body: The Organization Component as a typed model or dict., defaults to None
        :type request_body: Union[OrganizationComponent, dict], optional
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        :return: The parsed response data.
        :rtype: Union[OrganizationComponent, str, dict]
        """

        Validator(str).validate(id_)
        Validator(Union[OrganizationComponent, dict]).is_optional().validate(request_body)
        self._require_model_or_dict(request_body, OrganizationComponent)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/OrganizationComponent/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .add_header("Accept", "application/json")
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        return self._deserialize_or_raw(OrganizationComponent, response, status, content)

    @cast_models
    def delete_organization_component(self, id_: str) -> None:
        """The DELETE operation deletes the Organization Component object with the specified component ID. A DELETE operation specifying the ID of a deleted Organization component returns a false response. If the component is deleted successfully, the response is `true`.

        :param id_: ID of the Organization component you are attempting to delete.
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/OrganizationComponent/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("DELETE")
        )

        response, status, _ = self.send_request(serialized_request)

    @cast_models
    def bulk_organization_component(
        self, request_body: OrganizationComponentBulkRequest = None
    ) -> bytes:
        """The bulk GET operation returns multiple Account objects based on the supplied account IDs, to a maximum of 100. To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

        Organization Component XML is opaque (it carries open-ended config
        subtrees), so the bulk response is returned as the whole raw XML envelope,
        byte-for-byte, with no splitting or per-component re-serialization (which
        would be lossy and would drop non-200 entries).

        :param request_body: The request body., defaults to None
        :type request_body: OrganizationComponentBulkRequest, optional
        :raises ApiError: If the request fails.
        :return: The raw XML bulk-response envelope exactly as returned by the API.
        :rtype: bytes
        """

        Validator(OrganizationComponentBulkRequest).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/OrganizationComponent/bulk",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_header("Accept", "application/xml")
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, _ = self.send_request_raw(serialized_request)
        if 200 <= status < 300:
            return response
        raise ApiError(
            f"Failed to bulk get organization components: HTTP {status}",
            status,
            response,
        )

    @cast_models
    def query_organization_component(
        self, request_body: OrganizationComponentQueryConfig = None
    ) -> Union[OrganizationComponentQueryResponse, str, dict]:
        """- Only the LIKE operator is allowed with a name filter. Likewise, only the EQUALS operator is permitted with a contactName, email, or phone filter.

         -   If the QUERY request includes multiple filters, you can connect the filters with a logical AND operator — the query does not support the logical OR operator .

         -   The QUERY results omit the folderName field.

         For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body., defaults to None
        :type request_body: OrganizationComponentQueryConfig, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[OrganizationComponentQueryResponse, str, dict]
        """

        Validator(OrganizationComponentQueryConfig).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/OrganizationComponent/query",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        return self._deserialize_or_raw(OrganizationComponentQueryResponse, response, status, content)

    @cast_models
    def query_more_organization_component(
        self, request_body: str
    ) -> Union[OrganizationComponentQueryResponse, str, dict]:
        """To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body.
        :type request_body: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[OrganizationComponentQueryResponse, str, dict]
        """

        Validator(str).validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/OrganizationComponent/queryMore",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body, "text/plain")
        )

        response, status, content = self.send_request(serialized_request)
        return self._deserialize_or_raw(OrganizationComponentQueryResponse, response, status, content)
