
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.api_error import ApiError
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..net.transport.utils import parse_xml_to_dict
from ..models import (
    RuntimeObservabilitySettings,
    RuntimeObservabilitySettingsRequest,
    RuntimeObservabilitySettingsAsyncResponse,
    AsyncOperationTokenResult,
)


class RuntimeObservabilitySettingsService(BaseService):

    @cast_models
    def update_runtime_observability_settings(
        self, id_: str, request_body: RuntimeObservabilitySettingsRequest = None
    ) -> Union[RuntimeObservabilitySettings, str]:
        """Updates the RuntimeObservabilitySettings object having the specified ID.

        :param request_body: The request body., defaults to None
        :type request_body: RuntimeObservabilitySettingsRequest, optional
        :param id_: id_
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[RuntimeObservabilitySettings, str]
        """

        Validator(RuntimeObservabilitySettingsRequest).is_optional().validate(request_body)
        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/RuntimeObservabilitySettings/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return RuntimeObservabilitySettings._unmap(response)
        if content == "application/xml":
            return RuntimeObservabilitySettings._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def async_get_runtime_observability_settings(
        self, id_: str
    ) -> Union[AsyncOperationTokenResult, str]:
        """Returns a token for the specified RuntimeObservabilitySettings.

        :param id_: id_
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[AsyncOperationTokenResult, str]
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/async/RuntimeObservabilitySettings/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return AsyncOperationTokenResult._unmap(response)
        if content == "application/xml":
            return AsyncOperationTokenResult._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def async_token_runtime_observability_settings(
        self, token: str
    ) -> Union[RuntimeObservabilitySettingsAsyncResponse, str]:
        """For a response, use the token from the initial GET response in a new request.

        :param token: Takes in the token from a previous call to return a result.
        :type token: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[RuntimeObservabilitySettingsAsyncResponse, str]
        """

        Validator(str).validate(token)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/async/RuntimeObservabilitySettings/response/{{token}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("token", token)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return RuntimeObservabilitySettingsAsyncResponse._unmap(response)
        if content == "application/xml":
            return RuntimeObservabilitySettingsAsyncResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)
