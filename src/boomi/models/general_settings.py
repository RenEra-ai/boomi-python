
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .observability_endpoint import ObservabilityEndpoint


@JsonMap({"observability_endpoint": "observabilityEndpoint"})
class GeneralSettings(BaseModel):
    """GeneralSettings

    :param observability_endpoint: observability_endpoint
    :type observability_endpoint: ObservabilityEndpoint
    :param enabled: enabled, defaults to None
    :type enabled: bool, optional
    """

    def __init__(
        self,
        observability_endpoint: ObservabilityEndpoint,
        enabled: bool = SENTINEL,
        **kwargs,
    ):
        """GeneralSettings

        :param observability_endpoint: observability_endpoint
        :type observability_endpoint: ObservabilityEndpoint
        :param enabled: enabled, defaults to None
        :type enabled: bool, optional
        """
        self.observability_endpoint = self._define_object(
            observability_endpoint, ObservabilityEndpoint
        )
        if enabled is not SENTINEL:
            self.enabled = enabled
        self._kwargs = kwargs
