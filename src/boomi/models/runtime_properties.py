
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .standard_properties import StandardProperties
from .system_properties import SystemProperties
from .custom_runtime_properties import CustomRuntimeProperties
from .custom_system_properties import CustomSystemProperties


@JsonMap(
    {
        "partial_update": "partialUpdate",
        "runtime_id": "runtimeId",
        "standard_properties": "standardProperties",
        "system_properties": "systemProperties",
        "custom_runtime_properties": "customRuntimeProperties",
        "custom_system_properties": "customSystemProperties",
        "should_restart_runtime": "shouldRestartRuntime",
    }
)
class RuntimeProperties(BaseModel):
    """RuntimeProperties

    :param standard_properties: standard_properties
    :type standard_properties: StandardProperties
    :param system_properties: system_properties
    :type system_properties: SystemProperties
    :param custom_runtime_properties: custom_runtime_properties
    :type custom_runtime_properties: CustomRuntimeProperties
    :param custom_system_properties: custom_system_properties
    :type custom_system_properties: CustomSystemProperties
    :param partial_update: partial_update, defaults to None
    :type partial_update: bool, optional
    :param runtime_id: runtime_id, defaults to None
    :type runtime_id: str, optional
    :param should_restart_runtime: should_restart_runtime, defaults to None
    :type should_restart_runtime: bool, optional
    """

    def __init__(
        self,
        standard_properties: StandardProperties,
        system_properties: SystemProperties,
        custom_runtime_properties: CustomRuntimeProperties,
        custom_system_properties: CustomSystemProperties,
        partial_update: bool = SENTINEL,
        runtime_id: str = SENTINEL,
        should_restart_runtime: bool = SENTINEL,
        **kwargs,
    ):
        """RuntimeProperties

        :param standard_properties: standard_properties
        :type standard_properties: StandardProperties
        :param system_properties: system_properties
        :type system_properties: SystemProperties
        :param custom_runtime_properties: custom_runtime_properties
        :type custom_runtime_properties: CustomRuntimeProperties
        :param custom_system_properties: custom_system_properties
        :type custom_system_properties: CustomSystemProperties
        :param partial_update: partial_update, defaults to None
        :type partial_update: bool, optional
        :param runtime_id: runtime_id, defaults to None
        :type runtime_id: str, optional
        :param should_restart_runtime: should_restart_runtime, defaults to None
        :type should_restart_runtime: bool, optional
        """
        self.standard_properties = self._define_object(
            standard_properties, StandardProperties
        )
        self.system_properties = self._define_object(
            system_properties, SystemProperties
        )
        self.custom_runtime_properties = self._define_object(
            custom_runtime_properties, CustomRuntimeProperties
        )
        self.custom_system_properties = self._define_object(
            custom_system_properties, CustomSystemProperties
        )
        if partial_update is not SENTINEL:
            self.partial_update = partial_update
        if runtime_id is not SENTINEL:
            self.runtime_id = runtime_id
        if should_restart_runtime is not SENTINEL:
            self.should_restart_runtime = should_restart_runtime
        self._kwargs = kwargs
