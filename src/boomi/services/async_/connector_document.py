
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..connector_document import ConnectorDocumentService
from ...models import ConnectorDocumentDownload, ConnectorDocument


class ConnectorDocumentServiceAsync(ConnectorDocumentService):
    """
    Async Wrapper for ConnectorDocumentServiceAsync
    """

    def create_connector_document(
        self, request_body: ConnectorDocument = None
    ) -> Awaitable[Union[ConnectorDocumentDownload, str]]:
        return to_async(super().create_connector_document)(request_body)

    def download_connector_document(
        self,
        request_body: ConnectorDocument = None,
        max_retries: int = 10,
        initial_delay: float = 2.0,
    ) -> Awaitable[bytes]:
        return to_async(super().download_connector_document)(
            request_body, max_retries, initial_delay
        )
