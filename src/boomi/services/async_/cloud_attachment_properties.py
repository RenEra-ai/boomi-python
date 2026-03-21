
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..cloud_attachment_properties import (
    CloudAttachmentPropertiesService,
)
from ...models import (
    CloudAttachmentProperties,
    AsyncOperationTokenResult,
    CloudAttachmentPropertiesAsyncResponse,
)


class CloudAttachmentPropertiesServiceAsync(
    CloudAttachmentPropertiesService
):
    """
    Async Wrapper for CloudAttachmentPropertiesServiceAsync
    """

    def update_cloud_attachment_properties(
        self, id_: str, request_body: CloudAttachmentProperties
    ) -> Awaitable[Union[CloudAttachmentProperties, str]]:
        return to_async(super().update_cloud_attachment_properties)(
            id_, request_body
        )

    def async_get_cloud_attachment_properties(
        self, id_: str
    ) -> Awaitable[Union[AsyncOperationTokenResult, str]]:
        return to_async(super().async_get_cloud_attachment_properties)(id_)

    def async_token_cloud_attachment_properties(
        self, token: str
    ) -> Awaitable[Union[CloudAttachmentPropertiesAsyncResponse, str]]:
        return to_async(super().async_token_cloud_attachment_properties)(token)
