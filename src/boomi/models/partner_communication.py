
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .as2_communication_options import As2CommunicationOptions
from .disk_communication_options import DiskCommunicationOptions
from .ftp_communication_options import FtpCommunicationOptions
from .http_communication_options import HttpCommunicationOptions
from .mllp_communication_options import MllpCommunicationOptions
from .oftp_communication_options import OftpCommunicationOptions
from .sftp_communication_options import SftpCommunicationOptions


@JsonMap(
    {
        "as2_communication_options": "AS2CommunicationOptions",
        "disk_communication_options": "DiskCommunicationOptions",
        "ftp_communication_options": "FTPCommunicationOptions",
        "http_communication_options": "HTTPCommunicationOptions",
        "mllp_communication_options": "MLLPCommunicationOptions",
        "oftp_communication_options": "OFTPCommunicationOptions",
        "sftp_communication_options": "SFTPCommunicationOptions",
    }
)
class PartnerCommunication(BaseModel):
    """PartnerCommunication

    :param as2_communication_options: as2_communication_options, defaults to None
    :type as2_communication_options: As2CommunicationOptions, optional
    :param disk_communication_options: disk_communication_options, defaults to None
    :type disk_communication_options: DiskCommunicationOptions, optional
    :param ftp_communication_options: ftp_communication_options, defaults to None
    :type ftp_communication_options: FtpCommunicationOptions, optional
    :param http_communication_options: http_communication_options, defaults to None
    :type http_communication_options: HttpCommunicationOptions, optional
    :param mllp_communication_options: mllp_communication_options, defaults to None
    :type mllp_communication_options: MllpCommunicationOptions, optional
    :param oftp_communication_options: oftp_communication_options, defaults to None
    :type oftp_communication_options: OftpCommunicationOptions, optional
    :param sftp_communication_options: sftp_communication_options, defaults to None
    :type sftp_communication_options: SftpCommunicationOptions, optional
    """

    def __init__(
        self,
        as2_communication_options: As2CommunicationOptions = SENTINEL,
        disk_communication_options: DiskCommunicationOptions = SENTINEL,
        ftp_communication_options: FtpCommunicationOptions = SENTINEL,
        http_communication_options: HttpCommunicationOptions = SENTINEL,
        mllp_communication_options: MllpCommunicationOptions = SENTINEL,
        oftp_communication_options: OftpCommunicationOptions = SENTINEL,
        sftp_communication_options: SftpCommunicationOptions = SENTINEL,
        **kwargs,
    ):
        """PartnerCommunication

        :param as2_communication_options: as2_communication_options, defaults to None
        :type as2_communication_options: As2CommunicationOptions, optional
        :param disk_communication_options: disk_communication_options, defaults to None
        :type disk_communication_options: DiskCommunicationOptions, optional
        :param ftp_communication_options: ftp_communication_options, defaults to None
        :type ftp_communication_options: FtpCommunicationOptions, optional
        :param http_communication_options: http_communication_options, defaults to None
        :type http_communication_options: HttpCommunicationOptions, optional
        :param mllp_communication_options: mllp_communication_options, defaults to None
        :type mllp_communication_options: MllpCommunicationOptions, optional
        :param oftp_communication_options: oftp_communication_options, defaults to None
        :type oftp_communication_options: OftpCommunicationOptions, optional
        :param sftp_communication_options: sftp_communication_options, defaults to None
        :type sftp_communication_options: SftpCommunicationOptions, optional
        """
        if as2_communication_options is not SENTINEL:
            self.as2_communication_options = self._define_object(
                as2_communication_options, As2CommunicationOptions
            )
        if disk_communication_options is not SENTINEL:
            self.disk_communication_options = self._define_object(
                disk_communication_options, DiskCommunicationOptions
            )
        if ftp_communication_options is not SENTINEL:
            self.ftp_communication_options = self._define_object(
                ftp_communication_options, FtpCommunicationOptions
            )
        if http_communication_options is not SENTINEL:
            self.http_communication_options = self._define_object(
                http_communication_options, HttpCommunicationOptions
            )
        if mllp_communication_options is not SENTINEL:
            self.mllp_communication_options = self._define_object(
                mllp_communication_options, MllpCommunicationOptions
            )
        if oftp_communication_options is not SENTINEL:
            self.oftp_communication_options = self._define_object(
                oftp_communication_options, OftpCommunicationOptions
            )
        if sftp_communication_options is not SENTINEL:
            self.sftp_communication_options = self._define_object(
                sftp_communication_options, SftpCommunicationOptions
            )
        self._kwargs = kwargs

    def _map(self):
        """
        Convert to dict for API operations, producing minimal structure for UPDATE compatibility.

        The Boomi API returns extra fields on GET (CommunicationSetting, *GetOptions,
        *SendOptions, *SSLOptions, useDefault*) that it rejects on UPDATE with
        "Unable to read message body" error.

        This method produces a minimal structure that both CREATE and UPDATE accept.
        """
        result = {}

        # Helper to extract minimal settings for each protocol
        def extract_ftp_settings(ftp_opts):
            if not ftp_opts:
                return None
            mapped = ftp_opts._map() if hasattr(ftp_opts, '_map') else ftp_opts
            settings = mapped.get('FTPSettings', {})
            # Keep only essential fields, ensuring port is integer
            port = settings.get('port')
            if port is not None:
                port = int(port)
            result = {
                'FTPSettings': {
                    'host': settings.get('host'),
                    'port': port,
                    'user': settings.get('user'),
                    'password': settings.get('password', ''),
                    'connectionMode': settings.get('connectionMode', 'passive')
                }
            }
            # Include SSL options if present
            if 'FTPSSLOptions' in settings:
                result['FTPSettings']['FTPSSLOptions'] = settings['FTPSSLOptions']
            # Include Get/Send options if present (for remote_directory and action preservation)
            if 'FTPGetOptions' in mapped:
                get_opts = mapped['FTPGetOptions'].copy()
                # Ensure maxFileCount is int (API returns string, but requires int on update)
                if 'maxFileCount' in get_opts and get_opts['maxFileCount'] is not None:
                    get_opts['maxFileCount'] = int(get_opts['maxFileCount'])
                result['FTPGetOptions'] = get_opts
            if 'FTPSendOptions' in mapped:
                result['FTPSendOptions'] = mapped['FTPSendOptions']
            return result

        def extract_sftp_settings(sftp_opts):
            if not sftp_opts:
                return None
            mapped = sftp_opts._map() if hasattr(sftp_opts, '_map') else sftp_opts
            settings = mapped.get('SFTPSettings', {})
            # Ensure port is integer
            port = settings.get('port')
            if port is not None:
                port = int(port)
            result = {
                'SFTPSettings': {
                    'host': settings.get('host'),
                    'port': port,
                    'user': settings.get('user'),
                    'password': settings.get('password', '')
                }
            }
            # Include SSH options if present
            if 'SFTPSSHOptions' in settings:
                result['SFTPSettings']['SFTPSSHOptions'] = settings['SFTPSSHOptions']
            # Include Get/Send options if present (for remote_directory preservation)
            if 'SFTPGetOptions' in mapped:
                get_opts = mapped['SFTPGetOptions'].copy()
                # Ensure maxFileCount is int (API returns string, but requires int on update)
                if 'maxFileCount' in get_opts and get_opts['maxFileCount'] is not None:
                    get_opts['maxFileCount'] = int(get_opts['maxFileCount'])
                result['SFTPGetOptions'] = get_opts
            if 'SFTPSendOptions' in mapped:
                result['SFTPSendOptions'] = mapped['SFTPSendOptions']
            return result

        def extract_http_settings(http_opts):
            if not http_opts:
                return None
            mapped = http_opts._map() if hasattr(http_opts, '_map') else http_opts
            settings = mapped.get('HTTPSettings', {})
            minimal = {
                'HTTPSettings': {
                    'url': settings.get('url'),
                    'authenticationType': settings.get('authenticationType', 'NONE')
                }
            }
            # Include auth info if present
            if 'HTTPAuthSettings' in settings:
                minimal['HTTPSettings']['HTTPAuthSettings'] = settings['HTTPAuthSettings']
            # Include SSL options if present
            if 'HTTPSSLOptions' in settings:
                minimal['HTTPSettings']['HTTPSSLOptions'] = settings['HTTPSSLOptions']
            # Include timeouts if present
            if 'connectTimeout' in settings:
                minimal['HTTPSettings']['connectTimeout'] = settings['connectTimeout']
            if 'readTimeout' in settings:
                minimal['HTTPSettings']['readTimeout'] = settings['readTimeout']
            # Include Get/Send options if present
            if 'HTTPGetOptions' in mapped:
                minimal['HTTPGetOptions'] = mapped['HTTPGetOptions']
            if 'HTTPSendOptions' in mapped:
                minimal['HTTPSendOptions'] = mapped['HTTPSendOptions']
            return minimal

        def extract_disk_settings(disk_opts):
            if not disk_opts:
                return None
            mapped = disk_opts._map() if hasattr(disk_opts, '_map') else disk_opts
            result = {}
            if 'DiskGetOptions' in mapped:
                get_opts = mapped['DiskGetOptions']
                result['DiskGetOptions'] = {
                    'getDirectory': get_opts.get('getDirectory'),
                    'fileFilter': get_opts.get('fileFilter', '*')
                }
            if 'DiskSendOptions' in mapped:
                send_opts = mapped['DiskSendOptions']
                result['DiskSendOptions'] = {
                    'sendDirectory': send_opts.get('sendDirectory')
                }
            return result if result else None

        def extract_as2_settings(as2_opts):
            if not as2_opts:
                return None
            mapped = as2_opts._map() if hasattr(as2_opts, '_map') else as2_opts
            result = {}
            if 'AS2SendSettings' in mapped:
                settings = mapped['AS2SendSettings']
                result['AS2SendSettings'] = {
                    'url': settings.get('url'),
                    'authenticationType': settings.get('authenticationType', 'NONE')
                }
            # AS2SendOptions with required nested objects
            result['AS2SendOptions'] = {
                'AS2MDNOptions': mapped.get('AS2SendOptions', {}).get('AS2MDNOptions', {}),
                'AS2MessageOptions': mapped.get('AS2SendOptions', {}).get('AS2MessageOptions', {})
            }
            if 'AS2PartnerInfo' in mapped.get('AS2SendOptions', {}):
                result['AS2SendOptions']['AS2PartnerInfo'] = mapped['AS2SendOptions']['AS2PartnerInfo']
            return result

        # Extract each protocol if present
        if hasattr(self, 'ftp_communication_options'):
            ftp = extract_ftp_settings(self.ftp_communication_options)
            if ftp:
                result['FTPCommunicationOptions'] = ftp

        if hasattr(self, 'sftp_communication_options'):
            sftp = extract_sftp_settings(self.sftp_communication_options)
            if sftp:
                result['SFTPCommunicationOptions'] = sftp

        if hasattr(self, 'http_communication_options'):
            http = extract_http_settings(self.http_communication_options)
            if http:
                result['HTTPCommunicationOptions'] = http

        if hasattr(self, 'disk_communication_options'):
            disk = extract_disk_settings(self.disk_communication_options)
            if disk:
                result['DiskCommunicationOptions'] = disk

        if hasattr(self, 'as2_communication_options'):
            as2 = extract_as2_settings(self.as2_communication_options)
            if as2:
                result['AS2CommunicationOptions'] = as2

        # MLLP - pass through directly
        if hasattr(self, 'mllp_communication_options') and self.mllp_communication_options:
            mllp = self.mllp_communication_options
            mapped = mllp._map() if hasattr(mllp, '_map') else mllp
            if mapped:
                result['MLLPCommunicationOptions'] = mapped

        # OFTP - pass through directly
        if hasattr(self, 'oftp_communication_options') and self.oftp_communication_options:
            oftp = self.oftp_communication_options
            mapped = oftp._map() if hasattr(oftp, '_map') else oftp
            if mapped:
                result['OFTPCommunicationOptions'] = mapped

        return result
