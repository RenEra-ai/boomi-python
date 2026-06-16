
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

    :param observability_endpoint: observability_endpoint
    :type observability_endpoint: ObservabilityEndpoint
    :param trace_batch_size: trace_batch_size
    :type trace_batch_size: int
    :param trace_flush_interval: trace_flush_interval
    :type trace_flush_interval: int
    :param trace_max_queue_size: trace_max_queue_size
    :type trace_max_queue_size: int
    :param trace_timeout_seconds: trace_timeout_seconds
    :type trace_timeout_seconds: int
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
        observability_endpoint: ObservabilityEndpoint,
        trace_batch_size: int,
        trace_flush_interval: int,
        trace_max_queue_size: int,
        trace_timeout_seconds: int,
        enabled: bool = SENTINEL,
        override_general_observability_endpoint: bool = SENTINEL,
        process_filter_enabled: bool = SENTINEL,
        process_filter_ids: List[str] = SENTINEL,
        **kwargs,
    ):
        """TraceSettings

        :param observability_endpoint: observability_endpoint
        :type observability_endpoint: ObservabilityEndpoint
        :param trace_batch_size: trace_batch_size
        :type trace_batch_size: int
        :param trace_flush_interval: trace_flush_interval
        :type trace_flush_interval: int
        :param trace_max_queue_size: trace_max_queue_size
        :type trace_max_queue_size: int
        :param trace_timeout_seconds: trace_timeout_seconds
        :type trace_timeout_seconds: int
        :param enabled: enabled, defaults to None
        :type enabled: bool, optional
        :param override_general_observability_endpoint: override_general_observability_endpoint, defaults to None
        :type override_general_observability_endpoint: bool, optional
        :param process_filter_enabled: process_filter_enabled, defaults to None
        :type process_filter_enabled: bool, optional
        :param process_filter_ids: process_filter_ids, defaults to None
        :type process_filter_ids: List[str], optional
        """
        self.observability_endpoint = self._define_object(
            observability_endpoint, ObservabilityEndpoint
        )
        self.trace_batch_size = trace_batch_size
        self.trace_flush_interval = trace_flush_interval
        self.trace_max_queue_size = trace_max_queue_size
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
