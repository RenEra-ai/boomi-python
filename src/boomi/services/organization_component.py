
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.api_error import ApiError
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..net.transport.utils import parse_xml_to_dict, require_raw_xml
from ..models import (
    OrganizationComponentBulkRequest,
    OrganizationComponentBulkResponse,
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
    ) -> Union[str, OrganizationComponentBulkResponse]:
        """The bulk GET operation returns multiple Account objects based on the supplied account IDs, to a maximum of 100. To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

        :param request_body: The request body., defaults to None
        :type request_body: OrganizationComponentBulkRequest, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[str, OrganizationComponentBulkResponse]
        """

        Validator(OrganizationComponentBulkRequest).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/OrganizationComponent/bulk",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/xml":
            return OrganizationComponentBulkResponse._unmap(parse_xml_to_dict(response))
        if content == "application/json":
            return OrganizationComponentBulkResponse._unmap(response)
        raise ApiError("Error on deserializing the response.", status, response)

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
