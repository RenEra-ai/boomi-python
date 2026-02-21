
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap(
    {
        "gcp_client_email": "gcpClientEmail",
        "gcp_client_id": "gcpClientId",
        "gcp_private_key": "gcpPrivateKey",
        "gcp_private_key_id": "gcpPrivateKeyId",
        "gcp_project_id": "gcpProjectId",
    }
)
class CloudAttachmentGcpServiceAccountConfig(BaseModel):
    """CloudAttachmentGcpServiceAccountConfig

    :param gcp_client_email: gcp_client_email
    :type gcp_client_email: str
    :param gcp_client_id: gcp_client_id
    :type gcp_client_id: str
    :param gcp_private_key: gcp_private_key
    :type gcp_private_key: str
    :param gcp_private_key_id: gcp_private_key_id
    :type gcp_private_key_id: str
    :param gcp_project_id: gcp_project_id
    :type gcp_project_id: str
    """

    def __init__(
        self,
        gcp_client_email: str,
        gcp_client_id: str,
        gcp_private_key: str,
        gcp_private_key_id: str,
        gcp_project_id: str,
        **kwargs,
    ):
        """CloudAttachmentGcpServiceAccountConfig

        :param gcp_client_email: gcp_client_email
        :type gcp_client_email: str
        :param gcp_client_id: gcp_client_id
        :type gcp_client_id: str
        :param gcp_private_key: gcp_private_key
        :type gcp_private_key: str
        :param gcp_private_key_id: gcp_private_key_id
        :type gcp_private_key_id: str
        :param gcp_project_id: gcp_project_id
        :type gcp_project_id: str
        """
        self.gcp_client_email = gcp_client_email
        self.gcp_client_id = gcp_client_id
        self.gcp_private_key = gcp_private_key
        self.gcp_private_key_id = gcp_private_key_id
        self.gcp_project_id = gcp_project_id
        self._kwargs = kwargs
