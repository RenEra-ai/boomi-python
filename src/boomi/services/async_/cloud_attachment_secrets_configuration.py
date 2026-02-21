
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..cloud_attachment_secrets_configuration import (
    CloudAttachmentSecretsConfigurationService,
)
from ...models import (
    CloudAttachmentSecretsConfigurationRequest,
    CloudAttachmentSecretsConfigurationResponse,
)


class CloudAttachmentSecretsConfigurationServiceAsync(
    CloudAttachmentSecretsConfigurationService
):
    """
    Async Wrapper for CloudAttachmentSecretsConfigurationServiceAsync
    """

    def create_cloud_attachment_secrets_configuration(
        self,
        container_id: str,
        request_body: CloudAttachmentSecretsConfigurationRequest = None,
    ) -> Awaitable[Union[CloudAttachmentSecretsConfigurationResponse, str]]:
        return to_async(super().create_cloud_attachment_secrets_configuration)(
            container_id, request_body
        )
