
from typing import Awaitable, Union
from .utils.to_async import to_async
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

    def download_atom_as2_artifacts(
        self,
        request_body: AtomAs2Artifacts = None,
        max_retries: int = 10,
        initial_delay: float = 2.0,
    ) -> Awaitable[bytes]:
        return to_async(super().download_atom_as2_artifacts)(
            request_body, max_retries, initial_delay
        )
