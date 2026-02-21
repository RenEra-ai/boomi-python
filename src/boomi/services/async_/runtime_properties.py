
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..runtime_properties import RuntimePropertiesService
from ...models import (
    RuntimeProperties,
    AsyncOperationTokenResult,
    RuntimePropertiesAsyncResponse,
)


class RuntimePropertiesServiceAsync(RuntimePropertiesService):
    """
    Async Wrapper for RuntimePropertiesServiceAsync
    """

    def update_runtime_properties(
        self, id_: str, request_body: RuntimeProperties = None
    ) -> Awaitable[Union[RuntimeProperties, str]]:
        return to_async(super().update_runtime_properties)(id_, request_body)

    def async_get_runtime_properties(
        self, id_: str
    ) -> Awaitable[Union[AsyncOperationTokenResult, str]]:
        return to_async(super().async_get_runtime_properties)(id_)

    def async_token_runtime_properties(
        self, token: str
    ) -> Awaitable[Union[RuntimePropertiesAsyncResponse, str]]:
        return to_async(super().async_token_runtime_properties)(token)
