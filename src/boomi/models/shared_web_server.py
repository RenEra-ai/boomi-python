
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .shared_web_server_cloud_tennant_general import SharedWebServerCloudTennantGeneral
from .shared_web_server_cors import SharedWebServerCors
from .shared_web_server_general import SharedWebServerGeneral
from .shared_web_server_user_management import SharedWebServerUserManagement


@JsonMap(
    {
        "atom_id": "atomId",
        "cloud_tennant_general": "cloudTennantGeneral",
        "cors_configuration": "corsConfiguration",
        "general_settings": "generalSettings",
        "should_restart_plugin": "shouldRestartPlugin",
        "user_management": "userManagement",
    }
)
class SharedWebServer(BaseModel):
    """SharedWebServer

    :param atom_id: atom_id
    :type atom_id: str
    :param cloud_tennant_general: cloud_tennant_general, defaults to None
    :type cloud_tennant_general: SharedWebServerCloudTennantGeneral, optional
    :param cors_configuration: cors_configuration, defaults to None
    :type cors_configuration: SharedWebServerCors, optional
    :param general_settings: general_settings, defaults to None
    :type general_settings: SharedWebServerGeneral, optional
    :param should_restart_plugin: should_restart_plugin, defaults to None
    :type should_restart_plugin: bool, optional
    :param user_management: user_management, defaults to None
    :type user_management: SharedWebServerUserManagement, optional
    """

    def __init__(
        self,
        atom_id: str,
        cloud_tennant_general: SharedWebServerCloudTennantGeneral = SENTINEL,
        cors_configuration: SharedWebServerCors = SENTINEL,
        general_settings: SharedWebServerGeneral = SENTINEL,
        user_management: SharedWebServerUserManagement = SENTINEL,
        should_restart_plugin: bool = SENTINEL,
        **kwargs,
    ):
        """SharedWebServer

        :param atom_id: atom_id
        :type atom_id: str
        :param cloud_tennant_general: cloud_tennant_general, defaults to None
        :type cloud_tennant_general: SharedWebServerCloudTennantGeneral, optional
        :param cors_configuration: cors_configuration, defaults to None
        :type cors_configuration: SharedWebServerCors, optional
        :param general_settings: general_settings, defaults to None
        :type general_settings: SharedWebServerGeneral, optional
        :param should_restart_plugin: should_restart_plugin, defaults to None
        :type should_restart_plugin: bool, optional
        :param user_management: user_management, defaults to None
        :type user_management: SharedWebServerUserManagement, optional
        """
        self.atom_id = atom_id
        if cloud_tennant_general is not SENTINEL:
            self.cloud_tennant_general = self._define_object(
                cloud_tennant_general, SharedWebServerCloudTennantGeneral
            )
        if cors_configuration is not SENTINEL:
            self.cors_configuration = self._define_object(
                cors_configuration, SharedWebServerCors
            )
        if general_settings is not SENTINEL:
            self.general_settings = self._define_object(
                general_settings, SharedWebServerGeneral
            )
        if should_restart_plugin is not SENTINEL:
            self.should_restart_plugin = should_restart_plugin
        if user_management is not SENTINEL:
            self.user_management = self._define_object(
                user_management, SharedWebServerUserManagement
            )
        self._kwargs = kwargs
