
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..execution_record import ExecutionRecordService
from ...models import ExecutionRecord, ExecutionRecordQueryResponse, ExecutionRecordQueryConfig


class ExecutionRecordServiceAsync(ExecutionRecordService):
    """
    Async Wrapper for ExecutionRecordServiceAsync
    """

    def query_execution_record(
        self, request_body: ExecutionRecordQueryConfig = None
    ) -> Awaitable[Union[ExecutionRecordQueryResponse, str, dict]]:
        return to_async(super().query_execution_record)(request_body)

    def query_more_execution_record(
        self, request_body: str
    ) -> Awaitable[Union[ExecutionRecordQueryResponse, str, dict]]:
        return to_async(super().query_more_execution_record)(request_body)

    def async_get_execution_record(
        self, id_: str
    ) -> Awaitable[Union[ExecutionRecord, str, None]]:
        return to_async(super().async_get_execution_record)(id_)

    def get_execution_record(
        self, id_: str
    ) -> Awaitable[Union[ExecutionRecord, str, None]]:
        # Wrap the real underlying method directly. Wrapping the sync
        # ``get_execution_record`` convenience forwarder would re-dispatch through
        # ``self.async_get_execution_record`` (the async override) and return an
        # un-awaited coroutine. Mirror ``async_get_response_execution_record`` below.
        return to_async(super().async_get_execution_record)(id_)

    def async_get_response_execution_record(
        self, id_: str
    ) -> Awaitable[Union[ExecutionRecord, str, None]]:
        return to_async(super().async_get_execution_record)(id_)
