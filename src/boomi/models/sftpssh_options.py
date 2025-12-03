
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap(
    {"dh_key_size_max1024": "dhKeySizeMax1024", "known_host_entry": "knownHostEntry"}
)
class SftpsshOptions(BaseModel):
    """SftpsshOptions

    :param dh_key_size_max1024: dh_key_size_max1024, defaults to None
    :type dh_key_size_max1024: bool, optional
    :param known_host_entry: known_host_entry, defaults to None
    :type known_host_entry: str, optional
    :param sshkeyauth: sshkeyauth, defaults to None
    :type sshkeyauth: bool, optional
    :param sshkeypassword: sshkeypassword, defaults to None
    :type sshkeypassword: str, optional
    :param sshkeypath: sshkeypath, defaults to None
    :type sshkeypath: str, optional
    """

    def __init__(
        self,
        dh_key_size_max1024: bool = SENTINEL,
        known_host_entry: str = SENTINEL,
        sshkeyauth: bool = SENTINEL,
        sshkeypassword: str = SENTINEL,
        sshkeypath: str = SENTINEL,
        **kwargs
    ):
        """SftpsshOptions

        :param dh_key_size_max1024: dh_key_size_max1024, defaults to None
        :type dh_key_size_max1024: bool, optional
        :param known_host_entry: known_host_entry, defaults to None
        :type known_host_entry: str, optional
        :param sshkeyauth: sshkeyauth, defaults to None
        :type sshkeyauth: bool, optional
        :param sshkeypassword: sshkeypassword, defaults to None
        :type sshkeypassword: str, optional
        :param sshkeypath: sshkeypath, defaults to None
        :type sshkeypath: str, optional
        """
        if dh_key_size_max1024 is not SENTINEL:
            self.dh_key_size_max1024 = dh_key_size_max1024
        if known_host_entry is not SENTINEL:
            self.known_host_entry = known_host_entry
        if sshkeyauth is not SENTINEL:
            self.sshkeyauth = sshkeyauth
        if sshkeypassword is not SENTINEL:
            self.sshkeypassword = sshkeypassword
        if sshkeypath is not SENTINEL:
            self.sshkeypath = sshkeypath
        self._kwargs = kwargs
