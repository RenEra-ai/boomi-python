
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap(
    {
        "attachment_account_id": "attachmentAccountId",
        "attachment_creation_date": "attachmentCreationDate",
        "attachment_instance_id": "attachmentInstanceId",
        "cloud_cluster_id": "cloudClusterId",
        "cloud_id": "cloudId",
        "runtime_id": "runtimeId",
    }
)
class AccountCloudAttachmentSummary(BaseModel):
    """AccountCloudAttachmentSummary

    :param attachment_account_id: attachment_account_id, defaults to None
    :type attachment_account_id: str, optional
    :param attachment_creation_date: attachment_creation_date, defaults to None
    :type attachment_creation_date: str, optional
    :param attachment_instance_id: attachment_instance_id, defaults to None
    :type attachment_instance_id: str, optional
    :param cloud_cluster_id: cloud_cluster_id, defaults to None
    :type cloud_cluster_id: str, optional
    :param cloud_id: cloud_id, defaults to None
    :type cloud_id: str, optional
    :param runtime_id: runtime_id, defaults to None
    :type runtime_id: str, optional
    """

    def __init__(
        self,
        attachment_account_id: str = SENTINEL,
        attachment_creation_date: str = SENTINEL,
        attachment_instance_id: str = SENTINEL,
        cloud_cluster_id: str = SENTINEL,
        cloud_id: str = SENTINEL,
        runtime_id: str = SENTINEL,
        **kwargs,
    ):
        """AccountCloudAttachmentSummary

        :param attachment_account_id: attachment_account_id, defaults to None
        :type attachment_account_id: str, optional
        :param attachment_creation_date: attachment_creation_date, defaults to None
        :type attachment_creation_date: str, optional
        :param attachment_instance_id: attachment_instance_id, defaults to None
        :type attachment_instance_id: str, optional
        :param cloud_cluster_id: cloud_cluster_id, defaults to None
        :type cloud_cluster_id: str, optional
        :param cloud_id: cloud_id, defaults to None
        :type cloud_id: str, optional
        :param runtime_id: runtime_id, defaults to None
        :type runtime_id: str, optional
        """
        if attachment_account_id is not SENTINEL:
            self.attachment_account_id = attachment_account_id
        if attachment_creation_date is not SENTINEL:
            self.attachment_creation_date = attachment_creation_date
        if attachment_instance_id is not SENTINEL:
            self.attachment_instance_id = attachment_instance_id
        if cloud_cluster_id is not SENTINEL:
            self.cloud_cluster_id = cloud_cluster_id
        if cloud_id is not SENTINEL:
            self.cloud_id = cloud_id
        if runtime_id is not SENTINEL:
            self.runtime_id = runtime_id
        self._kwargs = kwargs
