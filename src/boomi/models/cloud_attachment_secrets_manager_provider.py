
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .cloud_attachment_aws_secrets_config import CloudAttachmentAwsSecretsConfig
from .cloud_attachment_azure_secrets_config import CloudAttachmentAzureSecretsConfig
from .cloud_attachment_gcp_secrets_config import CloudAttachmentGcpSecretsConfig


@JsonMap(
    {
        "aws": "AWS",
        "azure": "AZURE",
        "gcp": "GCP",
    }
)
class CloudAttachmentSecretsManagerProvider(BaseModel):
    """CloudAttachmentSecretsManagerProvider

    :param aws: aws, defaults to None
    :type aws: CloudAttachmentAwsSecretsConfig, optional
    :param azure: azure, defaults to None
    :type azure: CloudAttachmentAzureSecretsConfig, optional
    :param gcp: gcp, defaults to None
    :type gcp: CloudAttachmentGcpSecretsConfig, optional
    """

    def __init__(
        self,
        aws: CloudAttachmentAwsSecretsConfig = SENTINEL,
        azure: CloudAttachmentAzureSecretsConfig = SENTINEL,
        gcp: CloudAttachmentGcpSecretsConfig = SENTINEL,
        **kwargs,
    ):
        """CloudAttachmentSecretsManagerProvider

        :param aws: aws, defaults to None
        :type aws: CloudAttachmentAwsSecretsConfig, optional
        :param azure: azure, defaults to None
        :type azure: CloudAttachmentAzureSecretsConfig, optional
        :param gcp: gcp, defaults to None
        :type gcp: CloudAttachmentGcpSecretsConfig, optional
        """
        if aws is not SENTINEL:
            self.aws = self._define_object(aws, CloudAttachmentAwsSecretsConfig)
        if azure is not SENTINEL:
            self.azure = self._define_object(azure, CloudAttachmentAzureSecretsConfig)
        if gcp is not SENTINEL:
            self.gcp = self._define_object(gcp, CloudAttachmentGcpSecretsConfig)
        self._kwargs = kwargs
