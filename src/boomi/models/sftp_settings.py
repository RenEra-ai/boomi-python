
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .sftp_proxy_settings import SftpProxySettings
from .sftpssh_options import SftpsshOptions


@JsonMap(
    {
        "host": "host",
        "password": "password",
        "port": "port",
        "sftp_proxy_settings": "SFTPProxySettings",
        "sftpssh_options": "SFTPSSHOptions",
        "use_default_settings": "useDefaultSettings",
        "user": "user",
    }
)
class SftpSettings(BaseModel):
    """SftpSettings

    :param sftp_proxy_settings: sftp_proxy_settings, defaults to None
    :type sftp_proxy_settings: SftpProxySettings, optional
    :param sftpssh_options: sftpssh_options, defaults to None
    :type sftpssh_options: SftpsshOptions, optional
    :param host: host, defaults to None
    :type host: str, optional
    :param password: password, defaults to None
    :type password: str, optional
    :param port: port, defaults to None
    :type port: int, optional
    :param use_default_settings: use_default_settings, defaults to None
    :type use_default_settings: bool, optional
    :param user: user, defaults to None
    :type user: str, optional
    """

    def __init__(
        self,
        host: str = SENTINEL,
        password: str = SENTINEL,
        port: int = SENTINEL,
        sftp_proxy_settings: SftpProxySettings = SENTINEL,
        sftpssh_options: SftpsshOptions = SENTINEL,
        use_default_settings: bool = SENTINEL,
        user: str = SENTINEL,
        **kwargs,
    ):
        """SftpSettings

        :param sftp_proxy_settings: sftp_proxy_settings, defaults to None
        :type sftp_proxy_settings: SftpProxySettings, optional
        :param sftpssh_options: sftpssh_options, defaults to None
        :type sftpssh_options: SftpsshOptions, optional
        :param host: host, defaults to None
        :type host: str, optional
        :param password: password, defaults to None
        :type password: str, optional
        :param port: port, defaults to None
        :type port: int, optional
        :param use_default_settings: use_default_settings, defaults to None
        :type use_default_settings: bool, optional
        :param user: user, defaults to None
        :type user: str, optional
        """
        if sftp_proxy_settings is not SENTINEL:
            self.sftp_proxy_settings = self._define_object(
                sftp_proxy_settings, SftpProxySettings
            )
        if sftpssh_options is not SENTINEL:
            self.sftpssh_options = self._define_object(sftpssh_options, SftpsshOptions)
        if host is not SENTINEL:
            self.host = host
        if password is not SENTINEL:
            self.password = password
        if port is not SENTINEL:
            self.port = port
        if use_default_settings is not SENTINEL:
            self.use_default_settings = use_default_settings
        if user is not SENTINEL:
            self.user = user
        self._kwargs = kwargs
