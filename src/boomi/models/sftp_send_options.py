
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


class SftpSendOptionsFtpAction(Enum):
    """An enumeration representing different categories.

    :cvar ACTIONPUTRENAME: "actionputrename"
    :vartype ACTIONPUTRENAME: str
    :cvar ACTIONPUTAPPEND: "actionputappend"
    :vartype ACTIONPUTAPPEND: str
    :cvar ACTIONPUTERROR: "actionputerror"
    :vartype ACTIONPUTERROR: str
    :cvar ACTIONPUTOVERWRITE: "actionputoverwrite"
    :vartype ACTIONPUTOVERWRITE: str
    """

    ACTIONPUTRENAME = "actionputrename"
    ACTIONPUTAPPEND = "actionputappend"
    ACTIONPUTERROR = "actionputerror"
    ACTIONPUTOVERWRITE = "actionputoverwrite"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, SftpSendOptionsFtpAction._member_map_.values())
        )


@JsonMap(
    {
        "ftp_action": "ftpAction",
        "move_to_directory": "moveToDirectory",
        "move_to_force_override": "moveToForceOverride",
        "remote_directory": "remoteDirectory",
        "use_default_send_options": "useDefaultSendOptions",
    }
)
class SftpSendOptions(BaseModel):
    """SftpSendOptions

    :param ftp_action: ftp_action, defaults to None
    :type ftp_action: SftpSendOptionsFtpAction, optional
    :param move_to_directory: move_to_directory, defaults to None
    :type move_to_directory: str, optional
    :param move_to_force_override: move_to_force_override, defaults to None
    :type move_to_force_override: bool, optional
    :param remote_directory: remote_directory, defaults to None
    :type remote_directory: str, optional
    :param use_default_send_options: use_default_send_options, defaults to None
    :type use_default_send_options: bool, optional
    """

    def __init__(
        self,
        ftp_action: SftpSendOptionsFtpAction = SENTINEL,
        move_to_directory: str = SENTINEL,
        move_to_force_override: bool = SENTINEL,
        remote_directory: str = SENTINEL,
        use_default_send_options: bool = SENTINEL,
        **kwargs
    ):
        """SftpSendOptions

        :param ftp_action: ftp_action, defaults to None
        :type ftp_action: SftpSendOptionsFtpAction, optional
        :param move_to_directory: move_to_directory, defaults to None
        :type move_to_directory: str, optional
        :param move_to_force_override: move_to_force_override, defaults to None
        :type move_to_force_override: bool, optional
        :param remote_directory: remote_directory, defaults to None
        :type remote_directory: str, optional
        :param use_default_send_options: use_default_send_options, defaults to None
        :type use_default_send_options: bool, optional
        """
        if ftp_action is not SENTINEL:
            self.ftp_action = self._enum_matching(
                ftp_action, SftpSendOptionsFtpAction.list(), "ftp_action"
            )
        if move_to_directory is not SENTINEL:
            self.move_to_directory = move_to_directory
        if move_to_force_override is not SENTINEL:
            self.move_to_force_override = move_to_force_override
        if remote_directory is not SENTINEL:
            self.remote_directory = remote_directory
        if use_default_send_options is not SENTINEL:
            self.use_default_send_options = use_default_send_options
        self._kwargs = kwargs
