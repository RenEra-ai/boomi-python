
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .cloud_attachment_gcp_service_account_config import CloudAttachmentGcpServiceAccountConfig
from .cloud_attachment_gcp_user_account_config import CloudAttachmentGcpUserAccountConfig


@JsonMap(
    {
        "gcp_account_type": "gcpAccountType",
        "service_account": "serviceAccount",
        "user_account": "userAccount",
    }
)
class CloudAttachmentGcpSecretsConfig(BaseModel):
    """CloudAttachmentGcpSecretsConfig

    :param gcp_account_type: gcp_account_type
    :type gcp_account_type: str
    :param service_account: service_account, defaults to None
    :type service_account: CloudAttachmentGcpServiceAccountConfig, optional
    :param user_account: user_account, defaults to None
    :type user_account: CloudAttachmentGcpUserAccountConfig, optional
    """

    def __init__(
        self,
        gcp_account_type: str,
        service_account: CloudAttachmentGcpServiceAccountConfig = SENTINEL,
        user_account: CloudAttachmentGcpUserAccountConfig = SENTINEL,
        **kwargs,
    ):
        """CloudAttachmentGcpSecretsConfig

        :param gcp_account_type: gcp_account_type
        :type gcp_account_type: str
        :param service_account: service_account, defaults to None
        :type service_account: CloudAttachmentGcpServiceAccountConfig, optional
        :param user_account: user_account, defaults to None
        :type user_account: CloudAttachmentGcpUserAccountConfig, optional
        """
        self.gcp_account_type = gcp_account_type
        if service_account is not SENTINEL:
            self.service_account = self._define_object(
                service_account, CloudAttachmentGcpServiceAccountConfig
            )
        if user_account is not SENTINEL:
            self.user_account = self._define_object(
                user_account, CloudAttachmentGcpUserAccountConfig
            )
        self._kwargs = kwargs
