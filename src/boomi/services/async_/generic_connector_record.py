
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..generic_connector_record import GenericConnectorRecordService
from ...models import (
    GenericConnectorRecord,
    GenericConnectorRecordBulkResponse,
    GenericConnectorRecordBulkRequest,
    GenericConnectorRecordQueryResponse,
    GenericConnectorRecordQueryConfig,
)


class GenericConnectorRecordServiceAsync(GenericConnectorRecordService):
    """
    Async Wrapper for GenericConnectorRecordServiceAsync
    """

    def get_generic_connector_record(
        self, id_: str
    ) -> Awaitable[Union[GenericConnectorRecord, str, dict]]:
        return to_async(super().get_generic_connector_record)(id_)

    def bulk_generic_connector_record(
        self, request_body: GenericConnectorRecordBulkRequest = None
    ) -> Awaitable[Union[GenericConnectorRecordBulkResponse, str, dict]]:
        return to_async(super().bulk_generic_connector_record)(request_body)

    def query_generic_connector_record(
        self, request_body: GenericConnectorRecordQueryConfig = None
    ) -> Awaitable[Union[GenericConnectorRecordQueryResponse, str, dict]]:
        return to_async(super().query_generic_connector_record)(request_body)

    def query_more_generic_connector_record(
        self, request_body: str
    ) -> Awaitable[Union[GenericConnectorRecordQueryResponse, str, dict]]:
        return to_async(super().query_more_generic_connector_record)(request_body)
