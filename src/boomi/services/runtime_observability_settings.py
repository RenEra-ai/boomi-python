
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
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
    ) -> Union[RuntimeObservabilitySettings, str, dict]:
        """Updates the RuntimeObservabilitySettings object having the specified ID.

        :param request_body: The request body., defaults to None
        :type request_body: RuntimeObservabilitySettingsRequest, optional
        :param id_: id_
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[RuntimeObservabilitySettings, str, dict]
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
        return self._deserialize_or_raw(
            RuntimeObservabilitySettings, response, status, content
        )

    @cast_models
    def async_get_runtime_observability_settings(
        self, id_: str
    ) -> Union[AsyncOperationTokenResult, str, dict]:
        """Returns a token for the specified RuntimeObservabilitySettings.

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
                f"{self.base_url or Environment.DEFAULT.url}/async/RuntimeObservabilitySettings/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        return self._deserialize_or_raw(AsyncOperationTokenResult, response, status, content)

    @cast_models
    def async_token_runtime_observability_settings(
        self, token: str
    ) -> Union[RuntimeObservabilitySettingsAsyncResponse, str, dict, None]:
        """For a response, use the token from the initial GET response in a new request.

        :param token: Takes in the token from a previous call to return a result.
        :type token: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[RuntimeObservabilitySettingsAsyncResponse, str, dict, None]
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
        # A 204 / empty body (e.g. the runtime has no observability settings
        # configured) must not be forced through _unmap, which rejects a
        # non-dict (bytes/str) body and would raise instead of returning a
        # usable result. Treat it as "no settings available".
        if response is None or response == b"" or response == "":
            return None
        return self._deserialize_or_raw(RuntimeObservabilitySettingsAsyncResponse, response, status, content)
