
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap(
    {
        "gcp_client_id": "gcpClientId",
        "gcp_client_secret": "gcpClientSecret",
        "gcp_refresh_token": "gcpRefreshToken",
    }
)
class CloudAttachmentGcpUserAccountConfig(BaseModel):
    """CloudAttachmentGcpUserAccountConfig

    :param gcp_client_id: gcp_client_id
    :type gcp_client_id: str
    :param gcp_client_secret: gcp_client_secret
    :type gcp_client_secret: str
    :param gcp_refresh_token: gcp_refresh_token
    :type gcp_refresh_token: str
    """

    def __init__(
        self,
        gcp_client_id: str,
        gcp_client_secret: str,
        gcp_refresh_token: str,
        **kwargs,
    ):
        """CloudAttachmentGcpUserAccountConfig

        :param gcp_client_id: gcp_client_id
        :type gcp_client_id: str
        :param gcp_client_secret: gcp_client_secret
        :type gcp_client_secret: str
        :param gcp_refresh_token: gcp_refresh_token
        :type gcp_refresh_token: str
        """
        self.gcp_client_id = gcp_client_id
        self.gcp_client_secret = gcp_client_secret
        self.gcp_refresh_token = gcp_refresh_token
        self._kwargs = kwargs
