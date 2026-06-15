
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .shared_web_server_login_module_configuration import (
    SharedWebServerLoginModuleConfiguration,
)


@JsonMap(
    {
        "auth_type": "authType",
        "cache_authentication_timeout": "cacheAuthenticationTimeout",
        "cache_authorization_credentials": "cacheAuthorizationCredentials",
        "client_certificate_header_name": "clientCertificateHeaderName",
        "login_module_class_name": "loginModuleClassName",
        "login_module_options": "loginModuleOptions",
    }
)
class SharedWebServerAuthentication(BaseModel):
    """SharedWebServerAuthentication

    :param auth_type: auth_type, defaults to None
    :type auth_type: str, optional
    :param cache_authentication_timeout: cache_authentication_timeout, defaults to None
    :type cache_authentication_timeout: int, optional
    :param cache_authorization_credentials: cache_authorization_credentials, defaults to None
    :type cache_authorization_credentials: bool, optional
    :param client_certificate_header_name: client_certificate_header_name, defaults to None
    :type client_certificate_header_name: str, optional
    :param login_module_class_name: login_module_class_name, defaults to None
    :type login_module_class_name: str, optional
    :param login_module_options: login_module_options, defaults to None
    :type login_module_options: SharedWebServerLoginModuleConfiguration, optional
    """

    def __init__(
        self,
        auth_type: str = SENTINEL,
        client_certificate_header_name: str = SENTINEL,
        login_module_class_name: str = SENTINEL,
        login_module_options: SharedWebServerLoginModuleConfiguration = SENTINEL,
        cache_authentication_timeout: int = SENTINEL,
        cache_authorization_credentials: bool = SENTINEL,
        **kwargs,
    ):
        """SharedWebServerAuthentication

        :param auth_type: auth_type, defaults to None
        :type auth_type: str, optional
        :param cache_authentication_timeout: cache_authentication_timeout, defaults to None
        :type cache_authentication_timeout: int, optional
        :param cache_authorization_credentials: cache_authorization_credentials, defaults to None
        :type cache_authorization_credentials: bool, optional
        :param client_certificate_header_name: client_certificate_header_name, defaults to None
        :type client_certificate_header_name: str, optional
        :param login_module_class_name: login_module_class_name, defaults to None
        :type login_module_class_name: str, optional
        :param login_module_options: login_module_options, defaults to None
        :type login_module_options: SharedWebServerLoginModuleConfiguration, optional
        """
        if auth_type is not SENTINEL:
            self.auth_type = auth_type
        if cache_authentication_timeout is not SENTINEL:
            self.cache_authentication_timeout = cache_authentication_timeout
        if cache_authorization_credentials is not SENTINEL:
            self.cache_authorization_credentials = cache_authorization_credentials
        if client_certificate_header_name is not SENTINEL:
            self.client_certificate_header_name = client_certificate_header_name
        if login_module_class_name is not SENTINEL:
            self.login_module_class_name = login_module_class_name
        if login_module_options is not SENTINEL:
            self.login_module_options = self._define_object(
                login_module_options, SharedWebServerLoginModuleConfiguration
            )
        self._kwargs = kwargs
