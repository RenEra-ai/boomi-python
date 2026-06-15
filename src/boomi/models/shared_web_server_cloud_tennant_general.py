
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .listener_port_configuration import ListenerPortConfiguration


@JsonMap(
    {
        "api_type": "apiType",
        "auth_type": "authType",
        "base_url": "baseUrl",
        "listener_ports": "listenerPorts",
    }
)
class SharedWebServerCloudTennantGeneral(BaseModel):
    """SharedWebServerCloudTennantGeneral

    :param api_type: api_type, defaults to None
    :type api_type: str, optional
    :param auth_type: auth_type, defaults to None
    :type auth_type: str, optional
    :param base_url: base_url, defaults to None
    :type base_url: str, optional
    :param listener_ports: listener_ports, defaults to None
    :type listener_ports: ListenerPortConfiguration, optional
    """

    def __init__(
        self,
        api_type: str = SENTINEL,
        auth_type: str = SENTINEL,
        base_url: str = SENTINEL,
        listener_ports: ListenerPortConfiguration = SENTINEL,
        **kwargs,
    ):
        """SharedWebServerCloudTennantGeneral

        :param api_type: api_type, defaults to None
        :type api_type: str, optional
        :param auth_type: auth_type, defaults to None
        :type auth_type: str, optional
        :param base_url: base_url, defaults to None
        :type base_url: str, optional
        :param listener_ports: listener_ports, defaults to None
        :type listener_ports: ListenerPortConfiguration, optional
        """
        if api_type is not SENTINEL:
            self.api_type = api_type
        if auth_type is not SENTINEL:
            self.auth_type = auth_type
        if base_url is not SENTINEL:
            self.base_url = base_url
        if listener_ports is not SENTINEL:
            self.listener_ports = self._define_object(
                listener_ports, ListenerPortConfiguration
            )
        self._kwargs = kwargs
