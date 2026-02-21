
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({"status_code": "statusCode"})
class CloudAttachmentSecretsConfigurationResponse(BaseModel):
    """CloudAttachmentSecretsConfigurationResponse

    :param message: message, defaults to None
    :type message: str, optional
    :param status_code: status_code, defaults to None
    :type status_code: int, optional
    """

    def __init__(
        self,
        message: str = SENTINEL,
        status_code: int = SENTINEL,
        **kwargs,
    ):
        """CloudAttachmentSecretsConfigurationResponse

        :param message: message, defaults to None
        :type message: str, optional
        :param status_code: status_code, defaults to None
        :type status_code: int, optional
        """
        if message is not SENTINEL:
            self.message = message
        if status_code is not SENTINEL:
            self.status_code = status_code
        self._kwargs = kwargs
