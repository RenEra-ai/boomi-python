
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
    ) -> Awaitable[Union[ExecutionRecordQueryResponse, str]]:
        return to_async(super().query_execution_record)(request_body)

    def query_more_execution_record(
        self, request_body: str
    ) -> Awaitable[Union[ExecutionRecordQueryResponse, str]]:
        return to_async(super().query_more_execution_record)(request_body)

    def async_get_execution_record(
        self, id_: str
    ) -> Awaitable[Union[ExecutionRecord, str]]:
        return to_async(super().async_get_execution_record)(id_)
