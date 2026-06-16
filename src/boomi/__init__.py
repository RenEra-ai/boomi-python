
"""SDK top level package."""

__all__ = [
    "Boomi",
    "BoomiAsync",
    "Environment",
    "UnsafeComponentXmlSerializationError",
    "extract_component_xml_metadata",
]

def __getattr__(name):
    if name == "Boomi":
        from .sdk import Boomi as _Boomi
        return _Boomi
    if name == "BoomiAsync":
        from .sdk_async import BoomiAsync as _BoomiAsync
        return _BoomiAsync
    if name == "Environment":
        from .net.environment import Environment as _Environment
        return _Environment
    if name == "UnsafeComponentXmlSerializationError":
        from .net.transport.request_error import (
            UnsafeComponentXmlSerializationError as _Err,
        )
        return _Err
    if name == "extract_component_xml_metadata":
        from .net.transport.utils import extract_component_xml_metadata as _meta
        return _meta
    raise AttributeError(name)
