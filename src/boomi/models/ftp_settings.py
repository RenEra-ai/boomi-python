
from __future__ import annotations
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .ftpssl_options import FtpsslOptions


class ConnectionMode(Enum):
    """An enumeration representing different categories.

    :cvar ACTIVE: "active"
    :vartype ACTIVE: str
    :cvar PASSIVE: "passive"
    :vartype PASSIVE: str
    """

    ACTIVE = "active"
    PASSIVE = "passive"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, ConnectionMode._member_map_.values()))


@JsonMap(
    {
        "ftpssl_options": "FTPSSLOptions",
        "connection_mode": "connectionMode",
        "use_default_settings": "useDefaultSettings",
    }
)
class FtpSettings(BaseModel):
    """FtpSettings

    :param ftpssl_options: ftpssl_options, defaults to None
    :type ftpssl_options: FtpsslOptions, optional
    :param connection_mode: connection_mode, defaults to None
    :type connection_mode: ConnectionMode, optional
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
        connection_mode: ConnectionMode = SENTINEL,
        ftpssl_options: FtpsslOptions = SENTINEL,
        host: str = SENTINEL,
        password: str = SENTINEL,
        port: int = SENTINEL,
        use_default_settings: bool = SENTINEL,
        user: str = SENTINEL,
        **kwargs,
    ):
        """FtpSettings

        :param ftpssl_options: ftpssl_options, defaults to None
        :type ftpssl_options: FtpsslOptions, optional
        :param connection_mode: connection_mode, defaults to None
        :type connection_mode: ConnectionMode, optional
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
        if ftpssl_options is not SENTINEL:
            self.ftpssl_options = self._define_object(ftpssl_options, FtpsslOptions)
        if connection_mode is not SENTINEL:
            self.connection_mode = self._enum_matching(
                connection_mode, ConnectionMode.list(), "connection_mode"
            )
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
