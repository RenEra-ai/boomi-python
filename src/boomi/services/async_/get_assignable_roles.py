
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..get_assignable_roles import GetAssignableRolesService
from ...models import Roles


class GetAssignableRolesServiceAsync(GetAssignableRolesService):
    """
    Async Wrapper for GetAssignableRolesServiceAsync
    """

    def get_get_assignable_roles(self) -> Awaitable[Union[Roles, str, dict]]:
        return to_async(super().get_get_assignable_roles)()

    def list_assignable_roles(self) -> Awaitable[Union[Roles, str, dict]]:
        return to_async(super().get_get_assignable_roles)()
