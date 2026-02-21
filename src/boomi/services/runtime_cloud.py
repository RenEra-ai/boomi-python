
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.api_error import ApiError
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..net.transport.utils import parse_xml_to_dict
from ..models import (
    RuntimeCloud,
    RuntimeCloudBulkRequest,
    RuntimeCloudBulkResponse,
    RuntimeCloudQueryConfig,
    RuntimeCloudQueryResponse,
)


class RuntimeCloudService(BaseService):

    @cast_models
    def create_runtime_cloud(
        self, request_body: RuntimeCloud = None
    ) -> Union[RuntimeCloud, str]:
        """Creates a new RuntimeCloud object.

        :param request_body: The request body., defaults to None
        :type request_body: RuntimeCloud, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[RuntimeCloud, str]
        """

        Validator(RuntimeCloud).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/RuntimeCloud",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return RuntimeCloud._unmap(response)
        if content == "application/xml":
            return RuntimeCloud._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def get_runtime_cloud(self, id_: str) -> Union[RuntimeCloud, str]:
        """Retrieves the properties of the RuntimeCloud having the specified ID.

        :param id_: A unique ID assigned by the system to the RuntimeCloud.
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[RuntimeCloud, str]
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/RuntimeCloud/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return RuntimeCloud._unmap(response)
        if content == "application/xml":
            return RuntimeCloud._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def update_runtime_cloud(
        self, id_: str, request_body: RuntimeCloud = None
    ) -> Union[RuntimeCloud, str]:
        """Updates the RuntimeCloud object having the specified ID.

        :param request_body: The request body., defaults to None
        :type request_body: RuntimeCloud, optional
        :param id_: A unique ID assigned by the system to the RuntimeCloud.
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[RuntimeCloud, str]
        """

        Validator(RuntimeCloud).is_optional().validate(request_body)
        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/RuntimeCloud/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return RuntimeCloud._unmap(response)
        if content == "application/xml":
            return RuntimeCloud._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def delete_runtime_cloud(self, id_: str) -> None:
        """Deletes the RuntimeCloud object with the specified ID.

        :param id_: A unique ID assigned by the system to the RuntimeCloud.
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/RuntimeCloud/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("DELETE")
        )

        response, status, _ = self.send_request(serialized_request)

    @cast_models
    def bulk_runtime_cloud(
        self, request_body: RuntimeCloudBulkRequest = None
    ) -> Union[RuntimeCloudBulkResponse, str]:
        """To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

        :param request_body: The request body., defaults to None
        :type request_body: RuntimeCloudBulkRequest, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[RuntimeCloudBulkResponse, str]
        """

        Validator(RuntimeCloudBulkRequest).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/RuntimeCloud/bulk",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return RuntimeCloudBulkResponse._unmap(response)
        if content == "application/xml":
            return RuntimeCloudBulkResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def query_runtime_cloud(
        self, request_body: RuntimeCloudQueryConfig = None
    ) -> Union[RuntimeCloudQueryResponse, str]:
        """For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body., defaults to None
        :type request_body: RuntimeCloudQueryConfig, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[RuntimeCloudQueryResponse, str]
        """

        Validator(RuntimeCloudQueryConfig).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/RuntimeCloud/query",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return RuntimeCloudQueryResponse._unmap(response)
        if content == "application/xml":
            return RuntimeCloudQueryResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def query_more_runtime_cloud(
        self, request_body: str
    ) -> Union[RuntimeCloudQueryResponse, str]:
        """To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body.
        :type request_body: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[RuntimeCloudQueryResponse, str]
        """

        Validator(str).validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/RuntimeCloud/queryMore",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body, "text/plain")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return RuntimeCloudQueryResponse._unmap(response)
        if content == "application/xml":
            return RuntimeCloudQueryResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)
