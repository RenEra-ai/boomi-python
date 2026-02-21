
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..account_cloud_attachment_properties_default import (
    AccountCloudAttachmentPropertiesDefaultService,
)
from ...models import (
    AccountCloudAttachmentPropertiesDefault,
    AsyncOperationTokenResult,
    AccountCloudAttachmentPropertiesDefaultAsyncResponse,
)


class AccountCloudAttachmentPropertiesDefaultServiceAsync(
    AccountCloudAttachmentPropertiesDefaultService
):
    """
    Async Wrapper for AccountCloudAttachmentPropertiesDefaultServiceAsync
    """

    def update_account_cloud_attachment_properties_default(
        self, id_: str, request_body: AccountCloudAttachmentPropertiesDefault = None
    ) -> Awaitable[Union[AccountCloudAttachmentPropertiesDefault, str]]:
        return to_async(super().update_account_cloud_attachment_properties_default)(
            id_, request_body
        )

    def async_get_account_cloud_attachment_properties_default(
        self, id_: str
    ) -> Awaitable[Union[AsyncOperationTokenResult, str]]:
        return to_async(super().async_get_account_cloud_attachment_properties_default)(
            id_
        )

    def async_token_account_cloud_attachment_properties_default(
        self, token: str
    ) -> Awaitable[Union[AccountCloudAttachmentPropertiesDefaultAsyncResponse, str]]:
        return to_async(
            super().async_token_account_cloud_attachment_properties_default
        )(token)
