
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({
    "allow_browsing": "allowBrowsing",
    "allow_deployments": "allowDeployments",
    "allow_test_executions": "allowTestExecutions",
    "created_by": "createdBy",
    "created_date": "createdDate",
    "id_": "id",
    "max_attachments_per_account": "maxAttachmentsPerAccount",
    "modified_by": "modifiedBy",
    "modified_date": "modifiedDate",
})
class RuntimeCloud(BaseModel):
    """RuntimeCloud

    :param classification: classification
    :type classification: str
    :param name: name
    :type name: str
    :param allow_browsing: allow_browsing, defaults to None
    :type allow_browsing: bool, optional
    :param allow_deployments: allow_deployments, defaults to None
    :type allow_deployments: bool, optional
    :param allow_test_executions: allow_test_executions, defaults to None
    :type allow_test_executions: bool, optional
    :param created_by: created_by, defaults to None
    :type created_by: str, optional
    :param created_date: created_date, defaults to None
    :type created_date: str, optional
    :param id_: id_, defaults to None
    :type id_: str, optional
    :param max_attachments_per_account: max_attachments_per_account, defaults to None
    :type max_attachments_per_account: int, optional
    :param modified_by: modified_by, defaults to None
    :type modified_by: str, optional
    :param modified_date: modified_date, defaults to None
    :type modified_date: str, optional
    """

    def __init__(
        self,
        classification: str,
        name: str,
        allow_browsing: bool = SENTINEL,
        allow_deployments: bool = SENTINEL,
        allow_test_executions: bool = SENTINEL,
        created_by: str = SENTINEL,
        created_date: str = SENTINEL,
        id_: str = SENTINEL,
        max_attachments_per_account: int = SENTINEL,
        modified_by: str = SENTINEL,
        modified_date: str = SENTINEL,
        **kwargs,
    ):
        """RuntimeCloud"""
        self.classification = classification
        self.name = name
        if allow_browsing is not SENTINEL:
            self.allow_browsing = allow_browsing
        if allow_deployments is not SENTINEL:
            self.allow_deployments = allow_deployments
        if allow_test_executions is not SENTINEL:
            self.allow_test_executions = allow_test_executions
        if created_by is not SENTINEL:
            self.created_by = created_by
        if created_date is not SENTINEL:
            self.created_date = created_date
        if id_ is not SENTINEL:
            self.id_ = id_
        if max_attachments_per_account is not SENTINEL:
            self.max_attachments_per_account = max_attachments_per_account
        if modified_by is not SENTINEL:
            self.modified_by = modified_by
        if modified_date is not SENTINEL:
            self.modified_date = modified_date
        self._kwargs = kwargs
