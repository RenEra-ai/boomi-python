
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap(
    {
        "azure_client_id": "azureClientId",
        "azure_client_secret": "azureClientSecret",
        "azure_tenant_id": "azureTenantId",
    }
)
class CloudAttachmentAzureSecretsConfig(BaseModel):
    """CloudAttachmentAzureSecretsConfig

    :param azure_client_id: azure_client_id
    :type azure_client_id: str
    :param azure_client_secret: azure_client_secret
    :type azure_client_secret: str
    :param azure_tenant_id: azure_tenant_id
    :type azure_tenant_id: str
    """

    def __init__(
        self,
        azure_client_id: str,
        azure_client_secret: str,
        azure_tenant_id: str,
        **kwargs,
    ):
        """CloudAttachmentAzureSecretsConfig

        :param azure_client_id: azure_client_id
        :type azure_client_id: str
        :param azure_client_secret: azure_client_secret
        :type azure_client_secret: str
        :param azure_tenant_id: azure_tenant_id
        :type azure_tenant_id: str
        """
        self.azure_client_id = azure_client_id
        self.azure_client_secret = azure_client_secret
        self.azure_tenant_id = azure_tenant_id
        self._kwargs = kwargs
