
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .observability_endpoint_authentication import ObservabilityEndpointAuthentication


@JsonMap({})
class ObservabilityEndpoint(BaseModel):
    """ObservabilityEndpoint

    :param authentication: authentication, defaults to None
    :type authentication: ObservabilityEndpointAuthentication, optional
    :param url: url, defaults to None
    :type url: str, optional
    """

    def __init__(
        self,
        authentication: ObservabilityEndpointAuthentication = SENTINEL,
        url: str = SENTINEL,
        **kwargs,
    ):
        """ObservabilityEndpoint

        :param authentication: authentication, defaults to None
        :type authentication: ObservabilityEndpointAuthentication, optional
        :param url: url, defaults to None
        :type url: str, optional
        """
        if authentication is not SENTINEL:
            self.authentication = self._define_object(
                authentication, ObservabilityEndpointAuthentication
            )
        if url is not SENTINEL:
            self.url = url
        self._kwargs = kwargs
