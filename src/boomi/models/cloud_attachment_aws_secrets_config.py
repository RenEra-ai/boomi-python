
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap(
    {
        "aws_access_key_id": "awsAccessKeyId",
        "aws_region": "awsRegion",
        "aws_secret_access_key": "awsSecretAccessKey",
    }
)
class CloudAttachmentAwsSecretsConfig(BaseModel):
    """CloudAttachmentAwsSecretsConfig

    :param aws_access_key_id: aws_access_key_id
    :type aws_access_key_id: str
    :param aws_region: aws_region
    :type aws_region: str
    :param aws_secret_access_key: aws_secret_access_key
    :type aws_secret_access_key: str
    """

    def __init__(
        self,
        aws_access_key_id: str,
        aws_region: str,
        aws_secret_access_key: str,
        **kwargs,
    ):
        """CloudAttachmentAwsSecretsConfig

        :param aws_access_key_id: aws_access_key_id
        :type aws_access_key_id: str
        :param aws_region: aws_region
        :type aws_region: str
        :param aws_secret_access_key: aws_secret_access_key
        :type aws_secret_access_key: str
        """
        self.aws_access_key_id = aws_access_key_id
        self.aws_region = aws_region
        self.aws_secret_access_key = aws_secret_access_key
        self._kwargs = kwargs
