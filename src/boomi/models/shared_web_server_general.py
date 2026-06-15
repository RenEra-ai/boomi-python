
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .shared_web_server_authentication import SharedWebServerAuthentication
from .listener_port_configuration import ListenerPortConfiguration
from .shared_web_server_protected_headers import SharedWebServerProtectedHeaders


@JsonMap(
    {
        "api_type": "apiType",
        "base_url": "baseUrl",
        "examine_forward_headers": "examineForwardHeaders",
        "external_host": "externalHost",
        "internal_host": "internalHost",
        "listener_ports": "listenerPorts",
        "max_number_of_threads": "maxNumberOfThreads",
        "override_url": "overrideUrl",
        "protected_headers": "protectedHeaders",
        "ssl_certificate": "sslCertificate",
    }
)
class SharedWebServerGeneral(BaseModel):
    """SharedWebServerGeneral

    :param api_type: api_type, defaults to None
    :type api_type: str, optional
    :param authentication: authentication, defaults to None
    :type authentication: SharedWebServerAuthentication, optional
    :param base_url: base_url, defaults to None
    :type base_url: str, optional
    :param examine_forward_headers: examine_forward_headers, defaults to None
    :type examine_forward_headers: bool, optional
    :param external_host: external_host, defaults to None
    :type external_host: str, optional
    :param internal_host: internal_host, defaults to None
    :type internal_host: str, optional
    :param listener_ports: listener_ports, defaults to None
    :type listener_ports: ListenerPortConfiguration, optional
    :param max_number_of_threads: max_number_of_threads, defaults to None
    :type max_number_of_threads: int, optional
    :param override_url: override_url, defaults to None
    :type override_url: bool, optional
    :param protected_headers: protected_headers, defaults to None
    :type protected_headers: SharedWebServerProtectedHeaders, optional
    :param ssl_certificate: ssl_certificate, defaults to None
    :type ssl_certificate: str, optional
    """

    def __init__(
        self,
        api_type: str = SENTINEL,
        authentication: SharedWebServerAuthentication = SENTINEL,
        base_url: str = SENTINEL,
        external_host: str = SENTINEL,
        internal_host: str = SENTINEL,
        listener_ports: ListenerPortConfiguration = SENTINEL,
        protected_headers: SharedWebServerProtectedHeaders = SENTINEL,
        ssl_certificate: str = SENTINEL,
        examine_forward_headers: bool = SENTINEL,
        max_number_of_threads: int = SENTINEL,
        override_url: bool = SENTINEL,
        **kwargs,
    ):
        """SharedWebServerGeneral

        :param api_type: api_type, defaults to None
        :type api_type: str, optional
        :param authentication: authentication, defaults to None
        :type authentication: SharedWebServerAuthentication, optional
        :param base_url: base_url, defaults to None
        :type base_url: str, optional
        :param examine_forward_headers: examine_forward_headers, defaults to None
        :type examine_forward_headers: bool, optional
        :param external_host: external_host, defaults to None
        :type external_host: str, optional
        :param internal_host: internal_host, defaults to None
        :type internal_host: str, optional
        :param listener_ports: listener_ports, defaults to None
        :type listener_ports: ListenerPortConfiguration, optional
        :param max_number_of_threads: max_number_of_threads, defaults to None
        :type max_number_of_threads: int, optional
        :param override_url: override_url, defaults to None
        :type override_url: bool, optional
        :param protected_headers: protected_headers, defaults to None
        :type protected_headers: SharedWebServerProtectedHeaders, optional
        :param ssl_certificate: ssl_certificate, defaults to None
        :type ssl_certificate: str, optional
        """
        if api_type is not SENTINEL:
            self.api_type = api_type
        if authentication is not SENTINEL:
            self.authentication = self._define_object(
                authentication, SharedWebServerAuthentication
            )
        if base_url is not SENTINEL:
            self.base_url = base_url
        if examine_forward_headers is not SENTINEL:
            self.examine_forward_headers = examine_forward_headers
        if external_host is not SENTINEL:
            self.external_host = external_host
        if internal_host is not SENTINEL:
            self.internal_host = internal_host
        if listener_ports is not SENTINEL:
            self.listener_ports = self._define_object(
                listener_ports, ListenerPortConfiguration
            )
        if max_number_of_threads is not SENTINEL:
            self.max_number_of_threads = max_number_of_threads
        if override_url is not SENTINEL:
            self.override_url = override_url
        if protected_headers is not SENTINEL:
            self.protected_headers = self._define_object(
                protected_headers, SharedWebServerProtectedHeaders
            )
        if ssl_certificate is not SENTINEL:
            self.ssl_certificate = ssl_certificate
        self._kwargs = kwargs
