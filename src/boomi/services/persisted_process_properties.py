
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..models import (
    PersistedProcessProperties,
    AsyncOperationTokenResult,
    PersistedProcessPropertiesAsyncResponse
)


class PersistedProcessPropertiesService(BaseService):

    @cast_models
    def update_persisted_process_properties(
        self, id_: str, request_body: PersistedProcessProperties = None
    ) -> Union[PersistedProcessProperties, str, dict]:
        """The UPDATE operation updates Persisted Process Property values for the specified Runtime. Using the UPDATE operation overrides all current property settings. Therefore, strongly recommends that you include a complete list of all Persisted Process properties you want to keep or update. If you do not list a current persisted process property in the Persisted Process properties object, the UPDATE operation deletes those properties.

        >**Note:** You can update the Persisted Process properties if you have either the Runtime Management privilege or the Runtime Management Read Access, along with the Persisted Process Property Read and Write Access privilege.

        :param request_body: The request body., defaults to None
        :type request_body: PersistedProcessProperties, optional
        :param id_: A unique ID assigned by the system to the Runtime.
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[PersistedProcessProperties, str, dict]
        """

        Validator(PersistedProcessProperties).is_optional().validate(request_body)
        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/PersistedProcessProperties/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        return self._deserialize_or_raw(PersistedProcessProperties, response, status, content)

    @cast_models
    def async_get_persisted_process_properties(
        self, id_: str
    ) -> Union[AsyncOperationTokenResult, str, dict]:
        """The GET operation returns the current state of the Persisted Process properties names and values for the specified Runtime.
        The initial GET operation returns a token for the specified Runtime.

        :param id_: A unique ID assigned by the system to the Runtime.
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
                f"{self.base_url or Environment.DEFAULT.url}/async/PersistedProcessProperties/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        return self._deserialize_or_raw(AsyncOperationTokenResult, response, status, content)

    @cast_models
    def async_token_persisted_process_properties(
        self, token: str
    ) -> Union[PersistedProcessPropertiesAsyncResponse, str, dict]:
        """For a response, use the token from the response in a new request.

        :param token: Takes in the token from a previous call to return a result.
        :type token: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[PersistedProcessPropertiesAsyncResponse, str, dict]
        """

        Validator(str).validate(token)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/async/PersistedProcessProperties/response/{{token}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("token", token)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        return self._deserialize_or_raw(PersistedProcessPropertiesAsyncResponse, response, status, content)
