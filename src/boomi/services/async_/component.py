
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..component import ComponentService
from ...models import ComponentBulkRequest


class ComponentServiceAsync(ComponentService):
    """
    Async Wrapper for ComponentServiceAsync.

    Component XML is opaque: every method mirrors the sync raw-only contract and
    resolves to raw ``bytes`` (byte-for-byte identical to a direct API call).
    The lossy ``get_component_etree`` / ``update_component_etree`` helpers have
    been removed.
    """

    def create_component(
        self, request_body: Union[str, bytes] = None
    ) -> Awaitable[bytes]:
        return to_async(super().create_component)(request_body)

    def get_component(self, component_id: str) -> Awaitable[bytes]:
        return to_async(super().get_component)(component_id)

    def update_component(
        self, component_id: str, request_body: Union[str, bytes] = None
    ) -> Awaitable[bytes]:
        return to_async(super().update_component)(component_id, request_body)

    def bulk_component(
        self, request_body: ComponentBulkRequest = None
    ) -> Awaitable[bytes]:
        return to_async(super().bulk_component)(request_body)

    def create_component_raw(self, xml: Union[str, bytes] = None) -> Awaitable[bytes]:
        return to_async(super().create_component_raw)(xml)

    def get_component_raw(self, component_id: str) -> Awaitable[bytes]:
        return to_async(super().get_component_raw)(component_id)

    def update_component_raw(
        self, component_id: str, xml: Union[str, bytes] = None
    ) -> Awaitable[bytes]:
        return to_async(super().update_component_raw)(component_id, xml)

    def bulk_component_raw(
        self, request_body: ComponentBulkRequest = None
    ) -> Awaitable[bytes]:
        return to_async(super().bulk_component_raw)(request_body)
