
from typing import Awaitable, Union
from .utils.to_async import to_async
from ...net.transport.api_error import ApiError
from ..atom_as2_artifacts import AtomAs2ArtifactsService
from ...models import LogDownload, AtomAs2Artifacts


class AtomAs2ArtifactsServiceAsync(AtomAs2ArtifactsService):
    """
    Async Wrapper for AtomAs2ArtifactsServiceAsync
    """

    def create_atom_as2_artifacts(
        self, request_body: AtomAs2Artifacts = None
    ) -> Awaitable[Union[LogDownload, str]]:
        return to_async(super().create_atom_as2_artifacts)(request_body)

    async def download_atom_as2_artifacts(
        self,
        request_body: AtomAs2Artifacts = None,
        max_retries: int = 10,
        initial_delay: float = 2.0,
    ) -> bytes:
        # Await the async create_* override directly. Wrapping the sync
        # download orchestrator would re-dispatch self.create_* to that override
        # and leave an un-awaited coroutine, so the POST never fires. Poll the
        # (sync) download URL off-thread via to_async.
        result = await self.create_atom_as2_artifacts(request_body=request_body)
        if hasattr(result, "status_code") and str(result.status_code) == "504":
            raise ApiError("Runtime unavailable for artifact download", 504, result)
        if not hasattr(result, "url") or not result.url:
            raise ApiError("No download URL in response", 0, result)
        return await to_async(self._poll_download_url)(
            result.url, max_retries=max_retries, initial_delay=initial_delay
        )
