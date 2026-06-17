
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..models import (
    IntegrationPackEnvironmentAttachment,
    IntegrationPackEnvironmentAttachmentQueryConfig,
    IntegrationPackEnvironmentAttachmentQueryResponse,
)


class IntegrationPackEnvironmentAttachmentService(BaseService):

    @cast_models
    def create_integration_pack_environment_attachment(
        self, request_body: IntegrationPackEnvironmentAttachment = None
    ) -> Union[IntegrationPackEnvironmentAttachment, str, dict]:
        """Attaches an integration pack instance having the specified ID to the environment having the specified ID.

        :param request_body: The request body., defaults to None
        :type request_body: IntegrationPackEnvironmentAttachment, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[IntegrationPackEnvironmentAttachment, str, dict]
        """

        Validator(IntegrationPackEnvironmentAttachment).is_optional().validate(
            request_body
        )

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/IntegrationPackEnvironmentAttachment",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        return self._deserialize_or_raw(IntegrationPackEnvironmentAttachment, response, status, content)

    @cast_models
    def query_integration_pack_environment_attachment(
        self, request_body: IntegrationPackEnvironmentAttachmentQueryConfig = None
    ) -> Union[IntegrationPackEnvironmentAttachmentQueryResponse, str, dict]:
        """For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body., defaults to None
        :type request_body: IntegrationPackEnvironmentAttachmentQueryConfig, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[IntegrationPackEnvironmentAttachmentQueryResponse, str, dict]
        """

        Validator(
            IntegrationPackEnvironmentAttachmentQueryConfig
        ).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/IntegrationPackEnvironmentAttachment/query",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        return self._deserialize_or_raw(IntegrationPackEnvironmentAttachmentQueryResponse, response, status, content)

    @cast_models
    def query_more_integration_pack_environment_attachment(
        self, request_body: str
    ) -> Union[IntegrationPackEnvironmentAttachmentQueryResponse, str, dict]:
        """To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body.
        :type request_body: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[IntegrationPackEnvironmentAttachmentQueryResponse, str, dict]
        """

        Validator(str).validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/IntegrationPackEnvironmentAttachment/queryMore",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body, "text/plain")
        )

        response, status, content = self.send_request(serialized_request)
        return self._deserialize_or_raw(IntegrationPackEnvironmentAttachmentQueryResponse, response, status, content)

    @cast_models
    def delete_integration_pack_environment_attachment(self, id_: str) -> None:
        """Detaches an integration pack instance from an environment where the conceptual Integration Pack Environment Attachment object ID specifies the attachment. If you successfully detach the integration pack instance from the environment, the response is `true`.

        :param id_: The conceptual Integration Pack Environment Attachment object ID
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/IntegrationPackEnvironmentAttachment/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("DELETE")
        )

        response, status, _ = self.send_request(serialized_request)
