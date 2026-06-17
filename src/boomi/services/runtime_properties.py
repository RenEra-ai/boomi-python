
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..models import (
    RuntimeProperties,
    RuntimePropertiesAsyncResponse,
    AsyncOperationTokenResult,
)


class RuntimePropertiesService(BaseService):

    @cast_models
    def update_runtime_properties(
        self, id_: str, request_body: RuntimeProperties = None
    ) -> Union[RuntimeProperties, str, dict]:
        """Updates the RuntimeProperties object having the specified ID.

        :param request_body: The request body., defaults to None
        :type request_body: RuntimeProperties, optional
        :param id_: id_
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[RuntimeProperties, str, dict]
        """

        Validator(RuntimeProperties).is_optional().validate(request_body)
        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/RuntimeProperties/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        return self._deserialize_or_raw(RuntimeProperties, response, status, content)

    @cast_models
    def async_get_runtime_properties(
        self, id_: str
    ) -> Union[AsyncOperationTokenResult, str, dict]:
        """Returns a token for the specified RuntimeProperties.

        :param id_: id_
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[AsyncOperationTokenResult, str, dict]
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/async/RuntimeProperties/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        return self._deserialize_or_raw(AsyncOperationTokenResult, response, status, content)

    @cast_models
    def async_token_runtime_properties(
        self, token: str
    ) -> Union[RuntimePropertiesAsyncResponse, str, dict]:
        """For a response, use the token from the initial GET response in a new request.

        :param token: Takes in the token from a previous call to return a result.
        :type token: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[RuntimePropertiesAsyncResponse, str, dict]
        """

        Validator(str).validate(token)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/async/RuntimeProperties/response/{{token}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("token", token)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        return self._deserialize_or_raw(RuntimePropertiesAsyncResponse, response, status, content)
