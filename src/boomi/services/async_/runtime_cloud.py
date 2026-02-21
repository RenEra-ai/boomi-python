
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..runtime_cloud import RuntimeCloudService
from ...models import (
    RuntimeCloud,
    RuntimeCloudBulkResponse,
    RuntimeCloudBulkRequest,
    RuntimeCloudQueryResponse,
    RuntimeCloudQueryConfig,
)


class RuntimeCloudServiceAsync(RuntimeCloudService):
    """
    Async Wrapper for RuntimeCloudServiceAsync
    """

    def create_runtime_cloud(
        self, request_body: RuntimeCloud = None
    ) -> Awaitable[Union[RuntimeCloud, str]]:
        return to_async(super().create_runtime_cloud)(request_body)

    def get_runtime_cloud(self, id_: str) -> Awaitable[Union[RuntimeCloud, str]]:
        return to_async(super().get_runtime_cloud)(id_)

    def update_runtime_cloud(
        self, id_: str, request_body: RuntimeCloud = None
    ) -> Awaitable[Union[RuntimeCloud, str]]:
        return to_async(super().update_runtime_cloud)(id_, request_body)

    def delete_runtime_cloud(self, id_: str) -> Awaitable[None]:
        return to_async(super().delete_runtime_cloud)(id_)

    def bulk_runtime_cloud(
        self, request_body: RuntimeCloudBulkRequest = None
    ) -> Awaitable[Union[RuntimeCloudBulkResponse, str]]:
        return to_async(super().bulk_runtime_cloud)(request_body)

    def query_runtime_cloud(
        self, request_body: RuntimeCloudQueryConfig = None
    ) -> Awaitable[Union[RuntimeCloudQueryResponse, str]]:
        return to_async(super().query_runtime_cloud)(request_body)

    def query_more_runtime_cloud(
        self, request_body: str
    ) -> Awaitable[Union[RuntimeCloudQueryResponse, str]]:
        return to_async(super().query_more_runtime_cloud)(request_body)
