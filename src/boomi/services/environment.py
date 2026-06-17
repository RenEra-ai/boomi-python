
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..models import (
    Environment,
    EnvironmentBulkRequest,
    EnvironmentBulkResponse,
    EnvironmentMapExtension,
    EnvironmentQueryConfig,
    EnvironmentQueryResponse,
)


class EnvironmentService(BaseService):

    @cast_models
    def create_environment(
        self, request_body: Environment = None
    ) -> Union[Environment, str, dict]:
        """Creates an environment having the specified name. Environment names must be unique.

        :param request_body: The request body., defaults to None
        :type request_body: Environment, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[Environment, str, dict]
        """

        Validator(Environment).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/Environment",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        return self._deserialize_or_raw(Environment, response, status, content)

    @cast_models
    def get_environment(self, id_: str) -> Union[Environment, str, dict]:
        """Retrieves the properties of the environment with a specified ID.

        :param id_: A unique ID assigned by the system to the environment.
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[Environment, str, dict]
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/Environment/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        return self._deserialize_or_raw(Environment, response, status, content)

    @cast_models
    def update_environment(
        self, id_: str, request_body: Environment = None
    ) -> Union[Environment, str, dict]:
        """Updates the Environment object having the specified ID. You can edit the name field only.

        :param request_body: The request body., defaults to None
        :type request_body: Environment, optional
        :param id_: A unique ID assigned by the system to the environment.
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[Environment, str, dict]
        """

        Validator(Environment).is_optional().validate(request_body)
        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/Environment/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        return self._deserialize_or_raw(Environment, response, status, content)

    @cast_models
    def delete_environment(self, id_: str) -> None:
        """Deletes the Environment object with a specified ID. It is not possible to delete an environment that has attached Runtimes or integration packs.

        :param id_: A unique ID assigned by the system to the environment.
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/Environment/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("DELETE")
        )

        response, status, _ = self.send_request(serialized_request)

    @cast_models
    def bulk_environment(
        self, request_body: EnvironmentBulkRequest = None
    ) -> Union[EnvironmentBulkResponse, str, dict]:
        """To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

        :param request_body: The request body., defaults to None
        :type request_body: EnvironmentBulkRequest, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[EnvironmentBulkResponse, str, dict]
        """

        Validator(EnvironmentBulkRequest).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/Environment/bulk",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        return self._deserialize_or_raw(EnvironmentBulkResponse, response, status, content)

    @cast_models
    def query_environment(
        self, request_body: EnvironmentQueryConfig = None
    ) -> Union[EnvironmentQueryResponse, str, dict]:
        """For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body., defaults to None
        :type request_body: EnvironmentQueryConfig, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[EnvironmentQueryResponse, str, dict]
        """

        Validator(EnvironmentQueryConfig).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/Environment/query",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        return self._deserialize_or_raw(EnvironmentQueryResponse, response, status, content)

    @cast_models
    def query_more_environment(
        self, request_body: str
    ) -> Union[EnvironmentQueryResponse, str, dict]:
        """To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body.
        :type request_body: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[EnvironmentQueryResponse, str, dict]
        """

        Validator(str).validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/Environment/queryMore",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body, "text/plain")
        )

        response, status, content = self.send_request(serialized_request)
        return self._deserialize_or_raw(EnvironmentQueryResponse, response, status, content)

    @cast_models
    def update_environment_map_extension(
        self, id_: str, request_body: EnvironmentMapExtension = None
    ) -> Union[EnvironmentMapExtension, str, dict]:
        """Updates the extended mapping configuration for the specified Environment Map Extension object ID.

        :param request_body: The request body., defaults to None
        :type request_body: EnvironmentMapExtension, optional
        :param id_: id_
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[EnvironmentMapExtension, str, dict]
        """

        Validator(EnvironmentMapExtension).is_optional().validate(request_body)
        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/EnvironmentMapExtension/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        return self._deserialize_or_raw(EnvironmentMapExtension, response, status, content)
