
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.api_error import ApiError
from ..net.transport.utils import parse_xml_to_dict, require_raw_xml
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..models import (
    SharedCommunicationChannelComponentBulkRequest,
    SharedCommunicationChannelComponentBulkResponse,
    SharedCommunicationChannelComponentQueryConfig,
    SharedCommunicationChannelComponentQueryResponse,
)


class SharedCommunicationChannelComponentService(BaseService):

    def create_shared_communication_channel_component(
        self, request_body: Union[str, bytes] = None
    ) -> bytes:
        """Create a Shared Communication Channel Component from raw XML; return raw XML response bytes.

        The component XML (with its open-ended communication-config subtree) is
        treated as an **opaque** payload: it is sent exactly as provided and the
        response is returned byte-for-byte, with no parsing or conversion. Export
        an existing component via ``get_shared_communication_channel_component``
        to use as a template.

        :param request_body: Raw component XML (``str`` or ``bytes``).
        :type request_body: Union[str, bytes]
        :raises UnsafeComponentXmlSerializationError: If a non-raw body is passed.
        :raises ApiError: If the request fails.
        :return: The raw XML response exactly as returned by the API.
        :rtype: bytes
        """

        body = require_raw_xml(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/SharedCommunicationChannelComponent",
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
            f"Failed to create shared communication channel component: HTTP {status}",
            status,
            response,
        )

    def get_shared_communication_channel_component(self, id_: str) -> bytes:
        """Get a Shared Communication Channel Component as raw XML response bytes, without parsing.

        Preserves the exact XML structure returned by the API.

        :param id_: ID of the component being retrieved.
        :type id_: str
        :raises ApiError: If the request fails.
        :return: The raw XML response exactly as returned by the API.
        :rtype: bytes
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/SharedCommunicationChannelComponent/{{id}}",
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
            f"Failed to get shared communication channel component: HTTP {status}",
            status,
            response,
        )

    def update_shared_communication_channel_component(
        self, id_: str, request_body: Union[str, bytes] = None
    ) -> bytes:
        """Update a Shared Communication Channel Component with raw XML; return raw XML response bytes.

        Full updates only: supply the complete component XML you want persisted.
        The body is sent exactly as provided.

        :param id_: ID of the component that needs updating.
        :type id_: str
        :param request_body: Raw component XML (``str`` or ``bytes``).
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
                f"{self.base_url or Environment.DEFAULT.url}/SharedCommunicationChannelComponent/{{id}}",
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
            f"Failed to update shared communication channel component: HTTP {status}",
            status,
            response,
        )

    @cast_models
    def delete_shared_communication_channel_component(self, id_: str) -> None:
        """If the Shared Communication Channel component is deleted successfully, the response is `true`.

        :param id_: ID of the component that you want to delete.
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/SharedCommunicationChannelComponent/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("DELETE")
        )

        response, status, _ = self.send_request(serialized_request)

    @cast_models
    def bulk_shared_communication_channel_component(
        self, request_body: SharedCommunicationChannelComponentBulkRequest = None
    ) -> Union[SharedCommunicationChannelComponentBulkResponse, str]:
        """To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

        :param request_body: The request body., defaults to None
        :type request_body: SharedCommunicationChannelComponentBulkRequest, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[SharedCommunicationChannelComponentBulkResponse, str]
        """

        Validator(
            SharedCommunicationChannelComponentBulkRequest
        ).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/SharedCommunicationChannelComponent/bulk",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return SharedCommunicationChannelComponentBulkResponse._unmap(response)
        if content == "application/xml":
            return SharedCommunicationChannelComponentBulkResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def query_shared_communication_channel_component(
        self, request_body: SharedCommunicationChannelComponentQueryConfig = None
    ) -> Union[SharedCommunicationChannelComponentQueryResponse, str]:
        """For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

         The sample request query returns the Shared Communication Channel components using the AS2 standard for the authenticating account.

         >**Note:** The name field in a QUERY filter represents the object's `componentName` field.

        :param request_body: The request body., defaults to None
        :type request_body: SharedCommunicationChannelComponentQueryConfig, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[SharedCommunicationChannelComponentQueryResponse, str]
        """

        Validator(
            SharedCommunicationChannelComponentQueryConfig
        ).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/SharedCommunicationChannelComponent/query",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return SharedCommunicationChannelComponentQueryResponse._unmap(response)
        if content == "application/xml":
            # For XML responses, parse the XML and convert to dict structure
            import xml.etree.ElementTree as ET
            try:
                root = ET.fromstring(response)
                # Extract query results from XML
                result_data = {
                    'numberOfResults': 0,
                    'result': []
                }

                # Get number of results if present
                num_results = root.get('numberOfResults')
                if num_results:
                    result_data['numberOfResults'] = int(num_results)

                # Get query token if present
                query_token = root.get('queryToken')
                if query_token:
                    result_data['queryToken'] = query_token

                # Parse each result element
                for item in root.findall('.//{http://api.platform.boomi.com/}result'):
                    channel_data = {}
                    # Get attributes
                    for attr, value in item.attrib.items():
                        channel_data[attr] = value
                    # Get child elements
                    for child in item:
                        tag = child.tag.replace('{http://api.platform.boomi.com/}', '')
                        channel_data[tag] = child.text
                    if channel_data:
                        result_data['result'].append(channel_data)

                result_data['numberOfResults'] = len(result_data['result'])
                return SharedCommunicationChannelComponentQueryResponse._unmap(result_data)
            except ET.ParseError:
                # If XML parsing fails, return empty result
                return SharedCommunicationChannelComponentQueryResponse._unmap({
                    'numberOfResults': 0,
                    'result': []
                })
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def query_more_shared_communication_channel_component(
        self, request_body: str
    ) -> Union[SharedCommunicationChannelComponentQueryResponse, str]:
        """To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body.
        :type request_body: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[SharedCommunicationChannelComponentQueryResponse, str]
        """

        Validator(str).validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/SharedCommunicationChannelComponent/queryMore",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body, "text/plain")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return SharedCommunicationChannelComponentQueryResponse._unmap(response)
        if content == "application/xml":
            # For XML responses, parse the XML and convert to dict structure
            import xml.etree.ElementTree as ET
            try:
                root = ET.fromstring(response)
                # Extract query results from XML
                result_data = {
                    'numberOfResults': 0,
                    'result': []
                }

                # Get number of results if present
                num_results = root.get('numberOfResults')
                if num_results:
                    result_data['numberOfResults'] = int(num_results)

                # Get query token if present
                query_token = root.get('queryToken')
                if query_token:
                    result_data['queryToken'] = query_token

                # Parse each result element
                for item in root.findall('.//{http://api.platform.boomi.com/}result'):
                    channel_data = {}
                    # Get attributes
                    for attr, value in item.attrib.items():
                        channel_data[attr] = value
                    # Get child elements
                    for child in item:
                        tag = child.tag.replace('{http://api.platform.boomi.com/}', '')
                        channel_data[tag] = child.text
                    if channel_data:
                        result_data['result'].append(channel_data)

                result_data['numberOfResults'] = len(result_data['result'])
                return SharedCommunicationChannelComponentQueryResponse._unmap(result_data)
            except ET.ParseError:
                # If XML parsing fails, return empty result
                return SharedCommunicationChannelComponentQueryResponse._unmap({
                    'numberOfResults': 0,
                    'result': []
                })
        raise ApiError("Error on deserializing the response.", status, response)
