
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .observability_endpoint_authentication import ObservabilityEndpointAuthentication


@JsonMap({})
class ObservabilityEndpoint(BaseModel):
    """ObservabilityEndpoint

    :param authentication: authentication
    :type authentication: ObservabilityEndpointAuthentication
    :param url: url
    :type url: str
    """

    def __init__(
        self,
        authentication: ObservabilityEndpointAuthentication,
        url: str,
        **kwargs,
    ):
        """ObservabilityEndpoint

        :param authentication: authentication
        :type authentication: ObservabilityEndpointAuthentication
        :param url: url
        :type url: str
        """
        self.authentication = self._define_object(
            authentication, ObservabilityEndpointAuthentication
        )
        self.url = url
        self._kwargs = kwargs
