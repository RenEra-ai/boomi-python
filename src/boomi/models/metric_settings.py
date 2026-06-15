
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .observability_endpoint import ObservabilityEndpoint


@JsonMap(
    {
        "metric_interval_seconds": "metricIntervalSeconds",
        "metric_timeout_seconds": "metricTimeoutSeconds",
        "observability_endpoint": "observabilityEndpoint",
        "override_general_observability_endpoint": "overrideGeneralObservabilityEndpoint",
    }
)
class MetricSettings(BaseModel):
    """MetricSettings

    :param metric_interval_seconds: metric_interval_seconds, defaults to None
    :type metric_interval_seconds: int, optional
    :param metric_timeout_seconds: metric_timeout_seconds, defaults to None
    :type metric_timeout_seconds: int, optional
    :param observability_endpoint: observability_endpoint, defaults to None
    :type observability_endpoint: ObservabilityEndpoint, optional
    :param enabled: enabled, defaults to None
    :type enabled: bool, optional
    :param override_general_observability_endpoint: override_general_observability_endpoint, defaults to None
    :type override_general_observability_endpoint: bool, optional
    """

    def __init__(
        self,
        metric_interval_seconds: int = SENTINEL,
        metric_timeout_seconds: int = SENTINEL,
        observability_endpoint: ObservabilityEndpoint = SENTINEL,
        enabled: bool = SENTINEL,
        override_general_observability_endpoint: bool = SENTINEL,
        **kwargs,
    ):
        """MetricSettings

        :param metric_interval_seconds: metric_interval_seconds, defaults to None
        :type metric_interval_seconds: int, optional
        :param metric_timeout_seconds: metric_timeout_seconds, defaults to None
        :type metric_timeout_seconds: int, optional
        :param observability_endpoint: observability_endpoint, defaults to None
        :type observability_endpoint: ObservabilityEndpoint, optional
        :param enabled: enabled, defaults to None
        :type enabled: bool, optional
        :param override_general_observability_endpoint: override_general_observability_endpoint, defaults to None
        :type override_general_observability_endpoint: bool, optional
        """
        if metric_interval_seconds is not SENTINEL:
            self.metric_interval_seconds = metric_interval_seconds
        if metric_timeout_seconds is not SENTINEL:
            self.metric_timeout_seconds = metric_timeout_seconds
        if observability_endpoint is not SENTINEL:
            self.observability_endpoint = self._define_object(
                observability_endpoint, ObservabilityEndpoint
            )
        if enabled is not SENTINEL:
            self.enabled = enabled
        if override_general_observability_endpoint is not SENTINEL:
            self.override_general_observability_endpoint = (
                override_general_observability_endpoint
            )
        self._kwargs = kwargs
