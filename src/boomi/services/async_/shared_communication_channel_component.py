
from typing import Awaitable, Union
from .utils.to_async import to_async
from ..shared_communication_channel_component import (
    SharedCommunicationChannelComponentService,
)
from ...models import (
    SharedCommunicationChannelComponent,
    SharedCommunicationChannelComponentBulkRequest,
    SharedCommunicationChannelComponentQueryResponse,
    SharedCommunicationChannelComponentQueryConfig,
)


class SharedCommunicationChannelComponentServiceAsync(
    SharedCommunicationChannelComponentService
):
    """
    Async Wrapper for SharedCommunicationChannelComponentServiceAsync
    """

    def create_shared_communication_channel_component(
        self, request_body: Union[str, bytes] = None
    ) -> Awaitable[bytes]:
        return to_async(super().create_shared_communication_channel_component)(
            request_body
        )

    def get_shared_communication_channel_component(
        self, id_: str
    ) -> Awaitable[bytes]:
        return to_async(super().get_shared_communication_channel_component)(id_)

    def update_shared_communication_channel_component(
        self, id_: str, request_body: Union[str, bytes] = None
    ) -> Awaitable[bytes]:
        return to_async(super().update_shared_communication_channel_component)(
            id_, request_body
        )

    def create_shared_communication_channel_component_json(
        self, request_body: Union[SharedCommunicationChannelComponent, dict] = None
    ) -> Awaitable[Union[SharedCommunicationChannelComponent, str, dict]]:
        return to_async(
            super().create_shared_communication_channel_component_json
        )(request_body)

    def get_shared_communication_channel_component_json(
        self, id_: str
    ) -> Awaitable[Union[SharedCommunicationChannelComponent, str, dict]]:
        return to_async(super().get_shared_communication_channel_component_json)(id_)

    def update_shared_communication_channel_component_json(
        self, id_: str, request_body: Union[SharedCommunicationChannelComponent, dict] = None
    ) -> Awaitable[Union[SharedCommunicationChannelComponent, str, dict]]:
        return to_async(
            super().update_shared_communication_channel_component_json
        )(id_, request_body)

    def delete_shared_communication_channel_component(
        self, id_: str
    ) -> Awaitable[None]:
        return to_async(super().delete_shared_communication_channel_component)(id_)

    def bulk_shared_communication_channel_component(
        self, request_body: SharedCommunicationChannelComponentBulkRequest = None
    ) -> Awaitable[bytes]:
        return to_async(super().bulk_shared_communication_channel_component)(
            request_body
        )

    def query_shared_communication_channel_component(
        self, request_body: SharedCommunicationChannelComponentQueryConfig = None
    ) -> Awaitable[Union[SharedCommunicationChannelComponentQueryResponse, str, dict]]:
        return to_async(super().query_shared_communication_channel_component)(
            request_body
        )

    def query_more_shared_communication_channel_component(
        self, request_body: str
    ) -> Awaitable[Union[SharedCommunicationChannelComponentQueryResponse, str, dict]]:
        return to_async(super().query_more_shared_communication_channel_component)(
            request_body
        )
