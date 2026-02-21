
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .cloud_attachment_secrets_manager_provider import CloudAttachmentSecretsManagerProvider


@JsonMap(
    {
        "container_id": "containerId",
        "secrets_manager_provider": "secretsManagerProvider",
    }
)
class CloudAttachmentSecretsConfigurationRequest(BaseModel):
    """CloudAttachmentSecretsConfigurationRequest

    :param container_id: container_id
    :type container_id: str
    :param secrets_manager_provider: secrets_manager_provider
    :type secrets_manager_provider: CloudAttachmentSecretsManagerProvider
    """

    def __init__(
        self,
        container_id: str,
        secrets_manager_provider: CloudAttachmentSecretsManagerProvider,
        **kwargs,
    ):
        """CloudAttachmentSecretsConfigurationRequest

        :param container_id: container_id
        :type container_id: str
        :param secrets_manager_provider: secrets_manager_provider
        :type secrets_manager_provider: CloudAttachmentSecretsManagerProvider
        """
        self.container_id = container_id
        self.secrets_manager_provider = self._define_object(
            secrets_manager_provider, CloudAttachmentSecretsManagerProvider
        )
        self._kwargs = kwargs
