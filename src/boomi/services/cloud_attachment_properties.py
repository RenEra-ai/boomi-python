import copy
from typing import Union

from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.api_error import ApiError
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..net.transport.utils import parse_xml_to_dict
from ..models import (
    CloudAttachmentProperties,
    CloudAttachmentPropertiesAsyncResponse,
    AsyncOperationTokenResult,
)


class CloudAttachmentPropertiesService(BaseService):

    @cast_models
    def update_cloud_attachment_properties(
        self, id_: str, request_body: CloudAttachmentProperties
    ) -> Union[CloudAttachmentProperties, str]:
        """Modifies one or more Cloud attachment properties.

        :param request_body: The request body. Must include container_name.
        :type request_body: CloudAttachmentProperties
        :param id_: id_
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[CloudAttachmentProperties, str]
        """

        Validator(CloudAttachmentProperties).validate(request_body)
        if not getattr(request_body, "container_name", None):
            raise ValueError("request_body.container_name is required")
        Validator(str).validate(id_)

        body = request_body
        if not getattr(request_body, "runtime_id", None):
            body = copy.copy(request_body)
            body.runtime_id = id_

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/CloudAttachmentProperties/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("POST")
            .set_body(body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return CloudAttachmentProperties._unmap(response)
        if content == "application/xml":
            return CloudAttachmentProperties._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def async_get_cloud_attachment_properties(
        self, id_: str
    ) -> Union[AsyncOperationTokenResult, str]:
        """Use the GET operation to return and view Cloud attachment properties.

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
                f"{self.base_url or Environment.DEFAULT.url}/async/CloudAttachmentProperties/{{id}}",
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
    def async_token_cloud_attachment_properties(
        self, token: str
    ) -> Union[CloudAttachmentPropertiesAsyncResponse, str]:
        """Send a second GET request with the token returned in the first GET request.

        :param token: Takes in the token from a previous call to return a result.
        :type token: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[CloudAttachmentPropertiesAsyncResponse, str]
        """

        Validator(str).validate(token)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/async/CloudAttachmentProperties/response/{{token}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("token", token)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return CloudAttachmentPropertiesAsyncResponse._unmap(response)
        if content == "application/xml":
            return CloudAttachmentPropertiesAsyncResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)
