
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.api_error import ApiError
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..net.transport.utils import parse_xml_to_dict, require_raw_xml
from ..models import (
    TradingPartnerComponentBulkRequest,
    TradingPartnerComponentBulkResponse,
    TradingPartnerComponentQueryConfig,
    TradingPartnerComponentQueryResponse,
)


class TradingPartnerComponentService(BaseService):

    def create_trading_partner_component(
        self, request_body: Union[str, bytes] = None
    ) -> bytes:
        """Create a Trading Partner Component from raw XML; return the raw XML response bytes.

        The Trading Partner Component XML (with its open-ended communication /
        EDI configuration subtrees) is treated as an **opaque** payload: the XML
        is sent exactly as provided and the response is returned byte-for-byte,
        with no parsing or conversion. Export an existing component via
        ``get_trading_partner_component`` to use as a template.

        :param request_body: Raw Trading Partner Component XML (``str`` or ``bytes``).
        :type request_body: Union[str, bytes]
        :raises UnsafeComponentXmlSerializationError: If a non-raw body is passed.
        :raises ApiError: If the request fails.
        :return: The raw XML response exactly as returned by the API.
        :rtype: bytes
        """

        body = require_raw_xml(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/TradingPartnerComponent",
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
            f"Failed to create trading partner component: HTTP {status}",
            status,
            response,
        )

    def get_trading_partner_component(self, id_: str) -> bytes:
        """Get a Trading Partner Component as raw XML response bytes, without parsing.

        Preserves the exact XML structure returned by the API. A GET specifying
        the ID of a deleted Trading Partner component retrieves it (with
        ``deleted="true"``).

        :param id_: id_
        :type id_: str
        :raises ApiError: If the request fails.
        :return: The raw XML response exactly as returned by the API.
        :rtype: bytes
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/TradingPartnerComponent/{{id}}",
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
            f"Failed to get trading partner component: HTTP {status}",
            status,
            response,
        )

    def update_trading_partner_component(
        self, id_: str, request_body: Union[str, bytes] = None
    ) -> bytes:
        """Update a Trading Partner Component with raw XML; return the raw XML response bytes.

        Full updates only: supply the complete component XML you want persisted.
        The body is sent exactly as provided. An UPDATE specifying the ID of a
        deleted component restores it.

        :param id_: id_
        :type id_: str
        :param request_body: Raw Trading Partner Component XML (``str`` or ``bytes``).
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
                f"{self.base_url or Environment.DEFAULT.url}/TradingPartnerComponent/{{id}}",
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
            f"Failed to update trading partner component: HTTP {status}",
            status,
            response,
        )

    @cast_models
    def delete_trading_partner_component(self, id_: str) -> None:
        """The DELETE operation deletes the Trading Partner Component object with a specific component ID.
         A DELETE operation specifying the ID of a deleted Trading Partner component returns a false response.

        :param id_: id_
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/TradingPartnerComponent/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("DELETE")
        )

        response, status, _ = self.send_request(serialized_request)

    @cast_models
    def bulk_trading_partner_component(
        self, request_body: TradingPartnerComponentBulkRequest = None
    ) -> Union[TradingPartnerComponentBulkResponse, str]:
        """The bulk GET operation returns multiple Trading Partner Component objects based on the supplied IDs, to a maximum of 100.

        :param request_body: The request body., defaults to None
        :type request_body: TradingPartnerComponentBulkRequest, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[TradingPartnerComponentBulkResponse, str]
        """

        Validator(TradingPartnerComponentBulkRequest).is_optional().validate(
            request_body
        )

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/TradingPartnerComponent/bulk",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return TradingPartnerComponentBulkResponse._unmap(response)
        if content == "application/xml":
            return TradingPartnerComponentBulkResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def query_trading_partner_component(
        self, request_body: TradingPartnerComponentQueryConfig = None
    ) -> Union[TradingPartnerComponentQueryResponse, str]:
        """The QUERY operation returns each Trading Partner component that meets the specified filtering criteria.

         - The name field in a QUERY filter represents the object’s componentName field.
         - Only the LIKE operator is allowed with a name filter. Likewise, you can only use the EQUALS operator with a classification, standard, identifier filter, or a communication method filter (as2, disk, ftp, http, mllp, sftp). Filtering on a communication method field requests Trading Partner components by defining the communication method.
         - If the QUERY request includes multiple filters, you can connect the filters with a logical AND operator. The QUERY request does not support the logical OR operator.
         - The QUERY results omit the folderName field.

         For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body., defaults to None
        :type request_body: TradingPartnerComponentQueryConfig, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[TradingPartnerComponentQueryResponse, str]
        """

        Validator(TradingPartnerComponentQueryConfig).is_optional().validate(
            request_body
        )

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/TradingPartnerComponent/query",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return TradingPartnerComponentQueryResponse._unmap(response)
        if content == "application/xml":
            return TradingPartnerComponentQueryResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def query_more_trading_partner_component(
        self, request_body: str
    ) -> Union[TradingPartnerComponentQueryResponse, str]:
        """To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body.
        :type request_body: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[TradingPartnerComponentQueryResponse, str]
        """

        Validator(str).validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/TradingPartnerComponent/queryMore",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body, "text/plain")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return TradingPartnerComponentQueryResponse._unmap(response)
        if content == "application/xml":
            return TradingPartnerComponentQueryResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)
