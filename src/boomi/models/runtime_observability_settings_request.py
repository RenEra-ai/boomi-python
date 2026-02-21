
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .general_settings import GeneralSettings
from .log_settings import LogSettings
from .metric_settings import MetricSettings
from .trace_settings import TraceSettings


@JsonMap(
    {
        "runtime_id": "runtimeId",
        "general_settings": "generalSettings",
        "log_settings": "logSettings",
        "metric_settings": "metricSettings",
        "trace_settings": "traceSettings",
        "should_restart_plugin": "shouldRestartPlugin",
    }
)
class RuntimeObservabilitySettingsRequest(BaseModel):
    """RuntimeObservabilitySettingsRequest

    :param general_settings: general_settings
    :type general_settings: GeneralSettings
    :param log_settings: log_settings
    :type log_settings: LogSettings
    :param metric_settings: metric_settings
    :type metric_settings: MetricSettings
    :param runtime_id: runtime_id
    :type runtime_id: str
    :param trace_settings: trace_settings
    :type trace_settings: TraceSettings
    :param should_restart_plugin: should_restart_plugin, defaults to None
    :type should_restart_plugin: bool, optional
    """

    def __init__(
        self,
        general_settings: GeneralSettings,
        log_settings: LogSettings,
        metric_settings: MetricSettings,
        runtime_id: str,
        trace_settings: TraceSettings,
        should_restart_plugin: bool = SENTINEL,
        **kwargs,
    ):
        """RuntimeObservabilitySettingsRequest

        :param general_settings: general_settings
        :type general_settings: GeneralSettings
        :param log_settings: log_settings
        :type log_settings: LogSettings
        :param metric_settings: metric_settings
        :type metric_settings: MetricSettings
        :param runtime_id: runtime_id
        :type runtime_id: str
        :param trace_settings: trace_settings
        :type trace_settings: TraceSettings
        :param should_restart_plugin: should_restart_plugin, defaults to None
        :type should_restart_plugin: bool, optional
        """
        self.general_settings = self._define_object(
            general_settings, GeneralSettings
        )
        self.log_settings = self._define_object(log_settings, LogSettings)
        self.metric_settings = self._define_object(
            metric_settings, MetricSettings
        )
        self.runtime_id = runtime_id
        self.trace_settings = self._define_object(
            trace_settings, TraceSettings
        )
        if should_restart_plugin is not SENTINEL:
            self.should_restart_plugin = should_restart_plugin
        self._kwargs = kwargs
