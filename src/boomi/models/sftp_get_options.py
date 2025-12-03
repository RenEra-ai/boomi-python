
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


class SftpGetOptionsFtpAction(Enum):
    """An enumeration representing different categories.

    :cvar ACTIONGET: "actionget"
    :vartype ACTIONGET: str
    :cvar ACTIONGETDELETE: "actiongetdelete"
    :vartype ACTIONGETDELETE: str
    :cvar ACTIONGETMOVE: "actiongetmove"
    :vartype ACTIONGETMOVE: str
    """

    ACTIONGET = "actionget"
    ACTIONGETDELETE = "actiongetdelete"
    ACTIONGETMOVE = "actiongetmove"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, SftpGetOptionsFtpAction._member_map_.values())
        )


@JsonMap(
    {
        "file_to_move": "fileToMove",
        "ftp_action": "ftpAction",
        "max_file_count": "maxFileCount",
        "move_to_directory": "moveToDirectory",
        "move_to_force_override": "moveToForceOverride",
        "remote_directory": "remoteDirectory",
        "use_default_get_options": "useDefaultGetOptions",
    }
)
class SftpGetOptions(BaseModel):
    """SftpGetOptions

    :param file_to_move: file_to_move, defaults to None
    :type file_to_move: str, optional
    :param ftp_action: ftp_action, defaults to None
    :type ftp_action: SftpGetOptionsFtpAction, optional
    :param max_file_count: max_file_count, defaults to None
    :type max_file_count: int, optional
    :param move_to_directory: move_to_directory, defaults to None
    :type move_to_directory: str, optional
    :param move_to_force_override: move_to_force_override, defaults to None
    :type move_to_force_override: bool, optional
    :param remote_directory: remote_directory, defaults to None
    :type remote_directory: str, optional
    :param use_default_get_options: use_default_get_options, defaults to None
    :type use_default_get_options: bool, optional
    """

    def __init__(
        self,
        file_to_move: str = SENTINEL,
        ftp_action: SftpGetOptionsFtpAction = SENTINEL,
        max_file_count: int = SENTINEL,
        move_to_directory: str = SENTINEL,
        move_to_force_override: bool = SENTINEL,
        remote_directory: str = SENTINEL,
        use_default_get_options: bool = SENTINEL,
        **kwargs
    ):
        """SftpGetOptions

        :param file_to_move: file_to_move, defaults to None
        :type file_to_move: str, optional
        :param ftp_action: ftp_action, defaults to None
        :type ftp_action: SftpGetOptionsFtpAction, optional
        :param max_file_count: max_file_count, defaults to None
        :type max_file_count: int, optional
        :param move_to_directory: move_to_directory, defaults to None
        :type move_to_directory: str, optional
        :param move_to_force_override: move_to_force_override, defaults to None
        :type move_to_force_override: bool, optional
        :param remote_directory: remote_directory, defaults to None
        :type remote_directory: str, optional
        :param use_default_get_options: use_default_get_options, defaults to None
        :type use_default_get_options: bool, optional
        """
        if file_to_move is not SENTINEL:
            self.file_to_move = file_to_move
        if ftp_action is not SENTINEL:
            self.ftp_action = self._enum_matching(
                ftp_action, SftpGetOptionsFtpAction.list(), "ftp_action"
            )
        if max_file_count is not SENTINEL:
            self.max_file_count = max_file_count
        if move_to_directory is not SENTINEL:
            self.move_to_directory = move_to_directory
        if move_to_force_override is not SENTINEL:
            self.move_to_force_override = move_to_force_override
        if remote_directory is not SENTINEL:
            self.remote_directory = remote_directory
        if use_default_get_options is not SENTINEL:
            self.use_default_get_options = use_default_get_options
        self._kwargs = kwargs
