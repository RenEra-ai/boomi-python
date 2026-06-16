
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.api_error import ApiError
from ..net.transport.request_error import UnsafeComponentXmlSerializationError
from ..net.transport.utils import extract_component_xml_metadata, require_raw_xml
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..models import ComponentBulkRequest

__all__ = ["ComponentService", "extract_component_xml_metadata"]


class ComponentService(BaseService):
    """Service for Boomi Component XML operations.

    Component XML is treated as an **opaque** payload. ``create_component``,
    ``get_component``, ``update_component`` and ``bulk_component`` send and
    return raw ``bytes`` that are byte-for-byte identical to a direct Boomi API
    call. The SDK never parses, hydrates, normalizes, or re-serializes Component
    XML, because Boomi component objects are open-ended and cannot be losslessly
    represented by a generated Python model — doing so would silently corrupt
    integrations (namespaces, CDATA, comments, attribute order, unknown
    attributes).

    Write bodies must be raw ``str`` or ``bytes``; passing a ``Component`` model,
    ``dict``, ``ElementTree`` element, or any other object raises
    :class:`UnsafeComponentXmlSerializationError`. For read-only access to the
    root ``<Component>`` attributes use
    :func:`boomi.net.transport.utils.extract_component_xml_metadata` (re-exported
    here as ``extract_component_xml_metadata``).
    """

    @staticmethod
    def _require_raw_xml(body) -> Union[str, bytes]:
        """Validate a write body is raw XML and return it unchanged.

        Thin wrapper over :func:`boomi.net.transport.utils.require_raw_xml`,
        shared with the other component-family services.

        :raises UnsafeComponentXmlSerializationError: If ``body`` is not raw XML.
        :raises ValueError: If ``body`` is ``None`` or empty/whitespace-only.
        """
        return require_raw_xml(body)

    def create_component(self, request_body: Union[str, bytes] = None) -> bytes:
        """Create a component from raw XML and return the raw XML response bytes.

        The XML is sent exactly as provided and the response is returned
        byte-for-byte, with no parsing or conversion. Supply a valid component
        XML format for the given type (export an existing component via
        ``get_component`` to use as a template).

        :param request_body: Raw component XML (``str`` or ``bytes``).
        :type request_body: Union[str, bytes]
        :raises UnsafeComponentXmlSerializationError: If a non-raw body is passed.
        :raises ApiError: If the request fails.
        :return: The raw XML response exactly as returned by the API.
        :rtype: bytes
        """
        body = self._require_raw_xml(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/Component",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_header("Accept", "application/xml")
            .serialize()
            .set_method("POST")
            .set_body(body, "application/xml")
        )

        response, status, _ = self.send_request_raw(serialized_request)
        if 200 <= status < 300:
            return response
        raise ApiError(f"Failed to create component: HTTP {status}", status, response)

    def get_component(self, component_id: str) -> bytes:
        """Get a component as raw XML response bytes, without any parsing.

        Preserves the exact XML structure returned by the API (namespaces,
        element order, attributes, encoding). When no version is supplied the
        latest component is returned; use ``<componentId>~<version>`` for a
        specific version or ``<componentId>~<branchId>`` for a branch.

        :param component_id: The ID of the component.
        :type component_id: str
        :raises ApiError: If the request fails.
        :return: The raw XML response exactly as returned by the API.
        :rtype: bytes
        """
        Validator(str).validate(component_id)

        serializer = Serializer(
            f"{self.base_url or Environment.DEFAULT.url}/Component/{{componentId}}",
            [self.get_access_token(), self.get_basic_auth()],
        )
        serializer.add_header("Accept", "application/xml")
        serialized_request = (
            serializer.add_path("componentId", component_id)
            .serialize()
            .set_method("GET")
        )

        response, status, _ = self.send_request_raw(serialized_request)
        if 200 <= status < 300:
            return response
        raise ApiError(f"Failed to get component: HTTP {status}", status, response)

    def update_component(
        self, component_id: str, request_body: Union[str, bytes] = None
    ) -> bytes:
        """Update a component with raw XML and return the raw XML response bytes.

        Full updates only (no partial updates): supply the complete component
        XML you want persisted. The body is sent exactly as provided.

        :param component_id: The ID of the component.
        :type component_id: str
        :param request_body: Raw component XML (``str`` or ``bytes``).
        :type request_body: Union[str, bytes]
        :raises UnsafeComponentXmlSerializationError: If a non-raw body is passed.
        :raises ApiError: If the request fails.
        :return: The raw XML response exactly as returned by the API.
        :rtype: bytes
        """
        Validator(str).validate(component_id)
        body = self._require_raw_xml(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/Component/{{componentId}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("componentId", component_id)
            .add_header("Accept", "application/xml")
            .serialize()
            .set_method("POST")
            .set_body(body, "application/xml")
        )

        response, status, _ = self.send_request_raw(serialized_request)
        if 200 <= status < 300:
            return response
        raise ApiError(f"Failed to update component: HTTP {status}", status, response)

    @cast_models
    def bulk_component(self, request_body: ComponentBulkRequest = None) -> bytes:
        """Get multiple components as the raw XML bulk-response envelope bytes.

        The limit for the BULK GET operation is 5 requests. The request is a
        typed JSON query envelope (``ComponentBulkRequest``); the response is
        returned as the whole raw XML envelope, byte-for-byte, with no splitting
        or per-component re-serialization (which would be lossy and would drop
        non-200 entries).

        :param request_body: The bulk request envelope., defaults to None
        :type request_body: ComponentBulkRequest, optional
        :raises ApiError: If the request fails.
        :return: The raw XML bulk-response envelope exactly as returned by the API.
        :rtype: bytes
        """
        Validator(ComponentBulkRequest).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/Component/bulk",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_header("Accept", "application/xml")
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, _ = self.send_request_raw(serialized_request)
        if 200 <= status < 300:
            return response
        raise ApiError(
            f"Failed to bulk get components: HTTP {status}", status, response
        )

    # ========== Backward-compatible aliases ==========
    # The public methods are already raw/opaque, so the historical ``*_raw``
    # helpers are thin forwarders. They dispatch via the class (not ``self``) so
    # the async subclass overrides — which return coroutines — are bypassed when
    # a forwarder runs synchronously inside a worker thread.

    def create_component_raw(self, xml: Union[str, bytes] = None) -> bytes:
        """Alias for :meth:`create_component` (raw XML in, raw XML bytes out)."""
        return ComponentService.create_component(self, xml)

    def get_component_raw(self, component_id: str) -> bytes:
        """Alias for :meth:`get_component` (raw XML bytes out)."""
        return ComponentService.get_component(self, component_id)

    def update_component_raw(
        self, component_id: str, xml: Union[str, bytes] = None
    ) -> bytes:
        """Alias for :meth:`update_component` (raw XML in, raw XML bytes out)."""
        return ComponentService.update_component(self, component_id, xml)

    def bulk_component_raw(self, request_body: ComponentBulkRequest = None) -> bytes:
        """Alias for :meth:`bulk_component` (raw XML bulk envelope bytes out)."""
        return ComponentService.bulk_component(self, request_body)
