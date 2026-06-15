
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .observability_endpoint import ObservabilityEndpoint


@JsonMap(
    {
        "observability_endpoint": "observabilityEndpoint",
        "trace_batch_size": "traceBatchSize",
        "trace_flush_interval": "traceFlushInterval",
        "trace_max_queue_size": "traceMaxQueueSize",
        "trace_timeout_seconds": "traceTimeoutSeconds",
        "override_general_observability_endpoint": "overrideGeneralObservabilityEndpoint",
        "process_filter_enabled": "processFilterEnabled",
        "process_filter_ids": "processFilterIds",
    }
)
class TraceSettings(BaseModel):
    """TraceSettings

    :param observability_endpoint: observability_endpoint, defaults to None
    :type observability_endpoint: ObservabilityEndpoint, optional
    :param trace_batch_size: trace_batch_size, defaults to None
    :type trace_batch_size: int, optional
    :param trace_flush_interval: trace_flush_interval, defaults to None
    :type trace_flush_interval: int, optional
    :param trace_max_queue_size: trace_max_queue_size, defaults to None
    :type trace_max_queue_size: int, optional
    :param trace_timeout_seconds: trace_timeout_seconds, defaults to None
    :type trace_timeout_seconds: int, optional
    :param enabled: enabled, defaults to None
    :type enabled: bool, optional
    :param override_general_observability_endpoint: override_general_observability_endpoint, defaults to None
    :type override_general_observability_endpoint: bool, optional
    :param process_filter_enabled: process_filter_enabled, defaults to None
    :type process_filter_enabled: bool, optional
    :param process_filter_ids: process_filter_ids, defaults to None
    :type process_filter_ids: List[str], optional
    """

    def __init__(
        self,
        observability_endpoint: ObservabilityEndpoint = SENTINEL,
        trace_batch_size: int = SENTINEL,
        trace_flush_interval: int = SENTINEL,
        trace_max_queue_size: int = SENTINEL,
        trace_timeout_seconds: int = SENTINEL,
        enabled: bool = SENTINEL,
        override_general_observability_endpoint: bool = SENTINEL,
        process_filter_enabled: bool = SENTINEL,
        process_filter_ids: List[str] = SENTINEL,
        **kwargs,
    ):
        """TraceSettings

        :param observability_endpoint: observability_endpoint, defaults to None
        :type observability_endpoint: ObservabilityEndpoint, optional
        :param trace_batch_size: trace_batch_size, defaults to None
        :type trace_batch_size: int, optional
        :param trace_flush_interval: trace_flush_interval, defaults to None
        :type trace_flush_interval: int, optional
        :param trace_max_queue_size: trace_max_queue_size, defaults to None
        :type trace_max_queue_size: int, optional
        :param trace_timeout_seconds: trace_timeout_seconds, defaults to None
        :type trace_timeout_seconds: int, optional
        :param enabled: enabled, defaults to None
        :type enabled: bool, optional
        :param override_general_observability_endpoint: override_general_observability_endpoint, defaults to None
        :type override_general_observability_endpoint: bool, optional
        :param process_filter_enabled: process_filter_enabled, defaults to None
        :type process_filter_enabled: bool, optional
        :param process_filter_ids: process_filter_ids, defaults to None
        :type process_filter_ids: List[str], optional
        """
        if observability_endpoint is not SENTINEL:
            self.observability_endpoint = self._define_object(
                observability_endpoint, ObservabilityEndpoint
            )
        if trace_batch_size is not SENTINEL:
            self.trace_batch_size = trace_batch_size
        if trace_flush_interval is not SENTINEL:
            self.trace_flush_interval = trace_flush_interval
        if trace_max_queue_size is not SENTINEL:
            self.trace_max_queue_size = trace_max_queue_size
        if trace_timeout_seconds is not SENTINEL:
            self.trace_timeout_seconds = trace_timeout_seconds
        if enabled is not SENTINEL:
            self.enabled = enabled
        if override_general_observability_endpoint is not SENTINEL:
            self.override_general_observability_endpoint = (
                override_general_observability_endpoint
            )
        if process_filter_enabled is not SENTINEL:
            self.process_filter_enabled = process_filter_enabled
        if process_filter_ids is not SENTINEL:
            self.process_filter_ids = process_filter_ids
        self._kwargs = kwargs
