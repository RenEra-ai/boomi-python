
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


class SecretsManagerType(Enum):
    """An enumeration representing different categories.

    :cvar AWS: "AWS"
    :vartype AWS: str
    :cvar AZURE: "AZURE"
    :vartype AZURE: str
    :cvar GCP: "GCP"
    :vartype GCP: str
    """

    AWS = "AWS"
    AZURE = "AZURE"
    GCP = "GCP"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, SecretsManagerType._member_map_.values())
        )


@JsonMap(
    {
        "secret_reference": "secretReference",
        "secrets_manager_type": "secretsManagerType",
        "uses_remote_secrets_manager": "usesRemoteSecretsManager",
    }
)
class CloudManagedSecretConfig(BaseModel):
    """CloudManagedSecretConfig

    :param secret_reference: secret_reference, defaults to None
    :type secret_reference: str, optional
    :param secrets_manager_type: secrets_manager_type, defaults to None
    :type secrets_manager_type: SecretsManagerType, optional
    :param uses_remote_secrets_manager: uses_remote_secrets_manager, defaults to None
    :type uses_remote_secrets_manager: bool, optional
    """

    def __init__(
        self,
        secret_reference: str = SENTINEL,
        secrets_manager_type: SecretsManagerType = SENTINEL,
        uses_remote_secrets_manager: bool = SENTINEL,
        **kwargs,
    ):
        """CloudManagedSecretConfig

        :param secret_reference: secret_reference, defaults to None
        :type secret_reference: str, optional
        :param secrets_manager_type: secrets_manager_type, defaults to None
        :type secrets_manager_type: SecretsManagerType, optional
        :param uses_remote_secrets_manager: uses_remote_secrets_manager, defaults to None
        :type uses_remote_secrets_manager: bool, optional
        """
        if secret_reference is not SENTINEL:
            self.secret_reference = secret_reference
        if secrets_manager_type is not SENTINEL:
            self.secrets_manager_type = self._enum_matching(
                secrets_manager_type,
                SecretsManagerType.list(),
                "secrets_manager_type",
            )
        if uses_remote_secrets_manager is not SENTINEL:
            self.uses_remote_secrets_manager = uses_remote_secrets_manager
        self._kwargs = kwargs
