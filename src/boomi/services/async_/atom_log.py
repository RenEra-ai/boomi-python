
from typing import Awaitable, Union
from .utils.to_async import to_async
from ...net.transport.api_error import ApiError
from ..atom_log import AtomLogService
from ...models import LogDownload, AtomLog


class AtomLogServiceAsync(AtomLogService):
    """
    Async Wrapper for AtomLogServiceAsync
    """

    def create_atom_log(
        self, request_body: AtomLog = None
    ) -> Awaitable[Union[LogDownload, str, dict]]:
        return to_async(super().create_atom_log)(request_body)

    async def download_atom_log(
        self,
        request_body: AtomLog = None,
        max_retries: int = 10,
        initial_delay: float = 2.0,
    ) -> bytes:
        # Await the async create_* override directly. Wrapping the sync
        # download orchestrator would re-dispatch self.create_* to that override
        # and leave an un-awaited coroutine, so the POST never fires. Poll the
        # (sync) download URL off-thread via to_async.
        result = await self.create_atom_log(request_body=request_body)
        if hasattr(result, "status_code") and str(result.status_code) == "504":
            raise ApiError("Runtime unavailable for log download", 504, result)
        if not hasattr(result, "url") or not result.url:
            raise ApiError("No download URL in response", 0, result)
        return await to_async(self._poll_download_url)(
            result.url, max_retries=max_retries, initial_delay=initial_delay
        )
