
from typing import Awaitable
from .utils.to_async import to_async
from ..cancel_execution import CancelExecutionService


class CancelExecutionServiceAsync(CancelExecutionService):
    """
    Async Wrapper for CancelExecutionServiceAsync
    """

    def cancel_execution(self, execution_id: str) -> Awaitable[None]:
        return to_async(super().cancel_execution)(execution_id)
