
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
class RuntimeObservabilitySettings(BaseModel):
    """RuntimeObservabilitySettings

    :param runtime_id: runtime_id
    :type runtime_id: str
    :param general_settings: general_settings, defaults to None
    :type general_settings: GeneralSettings, optional
    :param log_settings: log_settings, defaults to None
    :type log_settings: LogSettings, optional
    :param metric_settings: metric_settings, defaults to None
    :type metric_settings: MetricSettings, optional
    :param trace_settings: trace_settings, defaults to None
    :type trace_settings: TraceSettings, optional
    :param should_restart_plugin: should_restart_plugin, defaults to None
    :type should_restart_plugin: bool, optional
    """

    def __init__(
        self,
        runtime_id: str,
        general_settings: GeneralSettings = SENTINEL,
        log_settings: LogSettings = SENTINEL,
        metric_settings: MetricSettings = SENTINEL,
        trace_settings: TraceSettings = SENTINEL,
        should_restart_plugin: bool = SENTINEL,
        **kwargs,
    ):
        """RuntimeObservabilitySettings

        :param runtime_id: runtime_id
        :type runtime_id: str
        :param general_settings: general_settings, defaults to None
        :type general_settings: GeneralSettings, optional
        :param log_settings: log_settings, defaults to None
        :type log_settings: LogSettings, optional
        :param metric_settings: metric_settings, defaults to None
        :type metric_settings: MetricSettings, optional
        :param trace_settings: trace_settings, defaults to None
        :type trace_settings: TraceSettings, optional
        :param should_restart_plugin: should_restart_plugin, defaults to None
        :type should_restart_plugin: bool, optional
        """
        self.runtime_id = runtime_id
        if general_settings is not SENTINEL:
            self.general_settings = self._define_object(
                general_settings, GeneralSettings
            )
        if log_settings is not SENTINEL:
            self.log_settings = self._define_object(log_settings, LogSettings)
        if metric_settings is not SENTINEL:
            self.metric_settings = self._define_object(
                metric_settings, MetricSettings
            )
        if trace_settings is not SENTINEL:
            self.trace_settings = self._define_object(
                trace_settings, TraceSettings
            )
        if should_restart_plugin is not SENTINEL:
            self.should_restart_plugin = should_restart_plugin
        self._kwargs = kwargs
