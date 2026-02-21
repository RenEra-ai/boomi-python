
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..account_cloud_attachment_summary import AccountCloudAttachmentSummaryService
from ...models import (
    AccountCloudAttachmentSummary,
    AccountCloudAttachmentSummaryBulkResponse,
    AccountCloudAttachmentSummaryBulkRequest,
    AccountCloudAttachmentSummaryQueryResponse,
    AccountCloudAttachmentSummaryQueryConfig,
)


class AccountCloudAttachmentSummaryServiceAsync(AccountCloudAttachmentSummaryService):
    """
    Async Wrapper for AccountCloudAttachmentSummaryServiceAsync
    """

    def get_account_cloud_attachment_summary(
        self, id_: str
    ) -> Awaitable[Union[AccountCloudAttachmentSummary, str]]:
        return to_async(super().get_account_cloud_attachment_summary)(id_)

    def bulk_account_cloud_attachment_summary(
        self, request_body: AccountCloudAttachmentSummaryBulkRequest = None
    ) -> Awaitable[Union[AccountCloudAttachmentSummaryBulkResponse, str]]:
        return to_async(super().bulk_account_cloud_attachment_summary)(request_body)

    def query_account_cloud_attachment_summary(
        self, request_body: AccountCloudAttachmentSummaryQueryConfig = None
    ) -> Awaitable[Union[AccountCloudAttachmentSummaryQueryResponse, str]]:
        return to_async(super().query_account_cloud_attachment_summary)(request_body)

    def query_more_account_cloud_attachment_summary(
        self, request_body: str
    ) -> Awaitable[Union[AccountCloudAttachmentSummaryQueryResponse, str]]:
        return to_async(super().query_more_account_cloud_attachment_summary)(request_body)
