
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .account_cloud_attachment_summary import AccountCloudAttachmentSummary


@JsonMap({"number_of_results": "numberOfResults", "query_token": "queryToken"})
class AccountCloudAttachmentSummaryQueryResponse(BaseModel):
    """AccountCloudAttachmentSummaryQueryResponse

    :param number_of_results: number_of_results, defaults to None
    :type number_of_results: int, optional
    :param query_token: query_token, defaults to None
    :type query_token: str, optional
    :param result: result, defaults to None
    :type result: List[AccountCloudAttachmentSummary], optional
    """

    def __init__(
        self,
        number_of_results: int = SENTINEL,
        query_token: str = SENTINEL,
        result: List[AccountCloudAttachmentSummary] = SENTINEL,
        **kwargs,
    ):
        """AccountCloudAttachmentSummaryQueryResponse

        :param number_of_results: number_of_results, defaults to None
        :type number_of_results: int, optional
        :param query_token: query_token, defaults to None
        :type query_token: str, optional
        :param result: result, defaults to None
        :type result: List[AccountCloudAttachmentSummary], optional
        """
        if number_of_results is not SENTINEL:
            self.number_of_results = number_of_results
        if query_token is not SENTINEL:
            self.query_token = query_token
        if result is not SENTINEL:
            self.result = self._define_list(result, AccountCloudAttachmentSummary)
        self._kwargs = kwargs
