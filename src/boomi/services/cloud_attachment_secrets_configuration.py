
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.api_error import ApiError
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..net.transport.utils import parse_xml_to_dict
from ..models import (
    CloudAttachmentSecretsConfigurationRequest,
    CloudAttachmentSecretsConfigurationResponse,
)


class CloudAttachmentSecretsConfigurationService(BaseService):

    @cast_models
    def create_cloud_attachment_secrets_configuration(
        self, container_id: str, request_body: CloudAttachmentSecretsConfigurationRequest = None
    ) -> Union[CloudAttachmentSecretsConfigurationResponse, str]:
        """Creates a CloudAttachmentSecretsConfiguration for the specified container.

        :param request_body: The request body., defaults to None
        :type request_body: CloudAttachmentSecretsConfigurationRequest, optional
        :param container_id: The container ID.
        :type container_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[CloudAttachmentSecretsConfigurationResponse, str]
        """

        Validator(CloudAttachmentSecretsConfigurationRequest).is_optional().validate(request_body)
        Validator(str).validate(container_id)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/CloudAttachmentSecretsConfiguration/{{containerId}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("containerId", container_id)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return CloudAttachmentSecretsConfigurationResponse._unmap(response)
        if content == "application/xml":
            return CloudAttachmentSecretsConfigurationResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)
