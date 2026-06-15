
from __future__ import annotations
from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .observability_endpoint import ObservabilityEndpoint


class LogFilterType(Enum):
    """An enumeration representing different categories.

    :cvar RUNTIME: "RUNTIME"
    :vartype RUNTIME: str
    :cvar RUNNER: "RUNNER"
    :vartype RUNNER: str
    :cvar WORKER: "WORKER"
    :vartype WORKER: str
    :cvar BROWSER: "BROWSER"
    :vartype BROWSER: str
    :cvar PROCESS: "PROCESS"
    :vartype PROCESS: str
    :cvar DOCUMENT: "DOCUMENT"
    :vartype DOCUMENT: str
    """

    RUNTIME = "RUNTIME"
    RUNNER = "RUNNER"
    WORKER = "WORKER"
    BROWSER = "BROWSER"
    PROCESS = "PROCESS"
    DOCUMENT = "DOCUMENT"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, LogFilterType._member_map_.values()))


@JsonMap(
    {
        "log_batch_size": "logBatchSize",
        "log_flush_interval": "logFlushInterval",
        "log_max_queue_size": "logMaxQueueSize",
        "log_timeout_seconds": "logTimeoutSeconds",
        "observability_endpoint": "observabilityEndpoint",
        "log_filter_enabled": "logFilterEnabled",
        "log_filter_types": "logFilterTypes",
        "override_general_observability_endpoint": "overrideGeneralObservabilityEndpoint",
    }
)
class LogSettings(BaseModel):
    """LogSettings

    :param log_batch_size: log_batch_size, defaults to None
    :type log_batch_size: int, optional
    :param log_flush_interval: log_flush_interval, defaults to None
    :type log_flush_interval: int, optional
    :param log_max_queue_size: log_max_queue_size, defaults to None
    :type log_max_queue_size: int, optional
    :param log_timeout_seconds: log_timeout_seconds, defaults to None
    :type log_timeout_seconds: int, optional
    :param observability_endpoint: observability_endpoint, defaults to None
    :type observability_endpoint: ObservabilityEndpoint, optional
    :param enabled: enabled, defaults to None
    :type enabled: bool, optional
    :param log_filter_enabled: log_filter_enabled, defaults to None
    :type log_filter_enabled: bool, optional
    :param log_filter_types: log_filter_types, defaults to None
    :type log_filter_types: List[str], optional
    :param override_general_observability_endpoint: override_general_observability_endpoint, defaults to None
    :type override_general_observability_endpoint: bool, optional
    """

    def __init__(
        self,
        log_batch_size: int = SENTINEL,
        log_flush_interval: int = SENTINEL,
        log_max_queue_size: int = SENTINEL,
        log_timeout_seconds: int = SENTINEL,
        observability_endpoint: ObservabilityEndpoint = SENTINEL,
        enabled: bool = SENTINEL,
        log_filter_enabled: bool = SENTINEL,
        log_filter_types: List[str] = SENTINEL,
        override_general_observability_endpoint: bool = SENTINEL,
        **kwargs,
    ):
        """LogSettings

        :param log_batch_size: log_batch_size, defaults to None
        :type log_batch_size: int, optional
        :param log_flush_interval: log_flush_interval, defaults to None
        :type log_flush_interval: int, optional
        :param log_max_queue_size: log_max_queue_size, defaults to None
        :type log_max_queue_size: int, optional
        :param log_timeout_seconds: log_timeout_seconds, defaults to None
        :type log_timeout_seconds: int, optional
        :param observability_endpoint: observability_endpoint, defaults to None
        :type observability_endpoint: ObservabilityEndpoint, optional
        :param enabled: enabled, defaults to None
        :type enabled: bool, optional
        :param log_filter_enabled: log_filter_enabled, defaults to None
        :type log_filter_enabled: bool, optional
        :param log_filter_types: log_filter_types, defaults to None
        :type log_filter_types: List[str], optional
        :param override_general_observability_endpoint: override_general_observability_endpoint, defaults to None
        :type override_general_observability_endpoint: bool, optional
        """
        if log_batch_size is not SENTINEL:
            self.log_batch_size = log_batch_size
        if log_flush_interval is not SENTINEL:
            self.log_flush_interval = log_flush_interval
        if log_max_queue_size is not SENTINEL:
            self.log_max_queue_size = log_max_queue_size
        if log_timeout_seconds is not SENTINEL:
            self.log_timeout_seconds = log_timeout_seconds
        if observability_endpoint is not SENTINEL:
            self.observability_endpoint = self._define_object(
                observability_endpoint, ObservabilityEndpoint
            )
        if enabled is not SENTINEL:
            self.enabled = enabled
        if log_filter_enabled is not SENTINEL:
            self.log_filter_enabled = log_filter_enabled
        if log_filter_types is not SENTINEL:
            self.log_filter_types = log_filter_types
        if override_general_observability_endpoint is not SENTINEL:
            self.override_general_observability_endpoint = (
                override_general_observability_endpoint
            )
        self._kwargs = kwargs
