
from typing import Awaitable, Union
from xml.etree import ElementTree as ET
from .utils.to_async import to_async
from ..component import ComponentService
from ...models import Component, ComponentBulkResponse, ComponentBulkRequest


class ComponentServiceAsync(ComponentService):
    """
    Async Wrapper for ComponentServiceAsync
    """

    def create_component(
        self, request_body: str = None
    ) -> Awaitable[Union[Component, str]]:
        return to_async(super().create_component)(request_body)

    def get_component(self, component_id: str) -> Awaitable[Union[Component, str]]:
        return to_async(super().get_component)(component_id)

    def update_component(
        self, component_id: str, request_body: str = None
    ) -> Awaitable[Union[Component, str]]:
        return to_async(super().update_component)(component_id, request_body)

    def bulk_component(
        self, request_body: ComponentBulkRequest = None
    ) -> Awaitable[str]:
        return to_async(super().bulk_component)(request_body)

    def create_component_raw(self, xml: str) -> Awaitable[str]:
        return to_async(super().create_component_raw)(xml)

    def get_component_raw(self, component_id: str) -> Awaitable[str]:
        return to_async(super().get_component_raw)(component_id)

    def update_component_raw(self, component_id: str, xml: str) -> Awaitable[str]:
        return to_async(super().update_component_raw)(component_id, xml)

    def bulk_component_raw(
        self, request_body: ComponentBulkRequest = None
    ) -> Awaitable[str]:
        return to_async(super().bulk_component_raw)(request_body)

    def get_component_etree(self, component_id: str) -> Awaitable[ET.Element]:
        return to_async(super().get_component_etree)(component_id)

    def update_component_etree(
        self, component_id: str, element: ET.Element
    ) -> Awaitable[str]:
        return to_async(super().update_component_etree)(component_id, element)
