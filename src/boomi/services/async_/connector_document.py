
from typing import Awaitable, Union
from .utils.to_async import to_async
from ...net.transport.api_error import ApiError
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

    async def download_connector_document(
        self,
        request_body: ConnectorDocument = None,
        max_retries: int = 10,
        initial_delay: float = 2.0,
    ) -> bytes:
        # Await the async create_* override directly. Wrapping the sync
        # download orchestrator would re-dispatch self.create_* to that override
        # and leave an un-awaited coroutine, so the POST never fires. Poll the
        # (sync) download URL off-thread via to_async.
        result = await self.create_connector_document(request_body=request_body)
        if not hasattr(result, "url") or not result.url:
            raise ApiError("No download URL in response", 0, result)
        return await to_async(self._poll_download_url)(
            result.url, max_retries=max_retries, initial_delay=initial_delay
        )
