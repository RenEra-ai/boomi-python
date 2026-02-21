
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..runtime_observability_settings import RuntimeObservabilitySettingsService
from ...models import (
    RuntimeObservabilitySettings,
    RuntimeObservabilitySettingsRequest,
    AsyncOperationTokenResult,
    RuntimeObservabilitySettingsAsyncResponse,
)


class RuntimeObservabilitySettingsServiceAsync(RuntimeObservabilitySettingsService):
    """
    Async Wrapper for RuntimeObservabilitySettingsServiceAsync
    """

    def update_runtime_observability_settings(
        self, id_: str, request_body: RuntimeObservabilitySettingsRequest = None
    ) -> Awaitable[Union[RuntimeObservabilitySettings, str]]:
        return to_async(super().update_runtime_observability_settings)(
            id_, request_body
        )

    def async_get_runtime_observability_settings(
        self, id_: str
    ) -> Awaitable[Union[AsyncOperationTokenResult, str]]:
        return to_async(super().async_get_runtime_observability_settings)(id_)

    def async_token_runtime_observability_settings(
        self, token: str
    ) -> Awaitable[Union[RuntimeObservabilitySettingsAsyncResponse, str]]:
        return to_async(super().async_token_runtime_observability_settings)(token)
