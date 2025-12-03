
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .attachment_info import AttachmentInfo
from .as2_basic_auth_info import As2BasicAuthInfo
from .public_certificate import PublicCertificate


@JsonMap(
    {
        "listen_attachment_settings": "ListenAttachmentSettings",
        "listen_auth_settings": "ListenAuthSettings",
        "as2_id": "as2Id",
        "basic_auth_enabled": "basicAuthEnabled",
        "client_ssl_certificate": "clientSSLCertificate",
        "enabled_legacy_smime": "enabledLegacySMIME",
        "encryption_public_certificate": "encryptionPublicCertificate",
        "mdn_signature_public_certificate": "mdnSignaturePublicCertificate",
        "messages_to_check_for_duplicates": "messagesToCheckForDuplicates",
        "reject_duplicate_messages": "rejectDuplicateMessages",
        "signing_public_certificate": "signingPublicCertificate",
    }
)
class As2PartnerInfo(BaseModel):
    """As2PartnerInfo

    :param listen_attachment_settings: listen_attachment_settings, defaults to None
    :type listen_attachment_settings: AttachmentInfo, optional
    :param listen_auth_settings: listen_auth_settings, defaults to None
    :type listen_auth_settings: As2BasicAuthInfo, optional
    :param as2_id: as2_id, defaults to None
    :type as2_id: str, optional
    :param basic_auth_enabled: basic_auth_enabled, defaults to None
    :type basic_auth_enabled: bool, optional
    :param client_ssl_certificate: client_ssl_certificate, defaults to None
    :type client_ssl_certificate: PublicCertificate, optional
    :param enabled_legacy_smime: enabled_legacy_smime, defaults to None
    :type enabled_legacy_smime: bool, optional
    :param encryption_public_certificate: encryption_public_certificate, defaults to None
    :type encryption_public_certificate: PublicCertificate, optional
    :param mdn_signature_public_certificate: mdn_signature_public_certificate, defaults to None
    :type mdn_signature_public_certificate: PublicCertificate, optional
    :param messages_to_check_for_duplicates: messages_to_check_for_duplicates, defaults to None
    :type messages_to_check_for_duplicates: int, optional
    :param reject_duplicate_messages: reject_duplicate_messages, defaults to None
    :type reject_duplicate_messages: bool, optional
    :param signing_public_certificate: signing_public_certificate, defaults to None
    :type signing_public_certificate: PublicCertificate, optional
    """

    def __init__(
        self,
        as2_id: str = SENTINEL,
        basic_auth_enabled: bool = SENTINEL,
        client_ssl_certificate: PublicCertificate = SENTINEL,
        enabled_legacy_smime: bool = SENTINEL,
        encryption_public_certificate: PublicCertificate = SENTINEL,
        listen_attachment_settings: AttachmentInfo = SENTINEL,
        listen_auth_settings: As2BasicAuthInfo = SENTINEL,
        mdn_signature_public_certificate: PublicCertificate = SENTINEL,
        messages_to_check_for_duplicates: int = SENTINEL,
        reject_duplicate_messages: bool = SENTINEL,
        signing_public_certificate: PublicCertificate = SENTINEL,
        **kwargs,
    ):
        """As2PartnerInfo

        :param as2_id: as2_id, defaults to None
        :type as2_id: str, optional
        :param basic_auth_enabled: basic_auth_enabled, defaults to None
        :type basic_auth_enabled: bool, optional
        :param client_ssl_certificate: client_ssl_certificate, defaults to None
        :type client_ssl_certificate: PublicCertificate, optional
        :param enabled_legacy_smime: enabled_legacy_smime, defaults to None
        :type enabled_legacy_smime: bool, optional
        :param encryption_public_certificate: encryption_public_certificate, defaults to None
        :type encryption_public_certificate: PublicCertificate, optional
        :param listen_attachment_settings: listen_attachment_settings, defaults to None
        :type listen_attachment_settings: AttachmentInfo, optional
        :param listen_auth_settings: listen_auth_settings, defaults to None
        :type listen_auth_settings: As2BasicAuthInfo, optional
        :param mdn_signature_public_certificate: mdn_signature_public_certificate, defaults to None
        :type mdn_signature_public_certificate: PublicCertificate, optional
        :param messages_to_check_for_duplicates: messages_to_check_for_duplicates, defaults to None
        :type messages_to_check_for_duplicates: int, optional
        :param reject_duplicate_messages: reject_duplicate_messages, defaults to None
        :type reject_duplicate_messages: bool, optional
        :param signing_public_certificate: signing_public_certificate, defaults to None
        :type signing_public_certificate: PublicCertificate, optional
        """
        if as2_id is not SENTINEL:
            self.as2_id = as2_id
        if basic_auth_enabled is not SENTINEL:
            self.basic_auth_enabled = basic_auth_enabled
        if client_ssl_certificate is not SENTINEL:
            self.client_ssl_certificate = self._define_object(
                client_ssl_certificate, PublicCertificate
            )
        if enabled_legacy_smime is not SENTINEL:
            self.enabled_legacy_smime = enabled_legacy_smime
        if encryption_public_certificate is not SENTINEL:
            self.encryption_public_certificate = self._define_object(
                encryption_public_certificate, PublicCertificate
            )
        if listen_attachment_settings is not SENTINEL:
            self.listen_attachment_settings = self._define_object(
                listen_attachment_settings, AttachmentInfo
            )
        if listen_auth_settings is not SENTINEL:
            self.listen_auth_settings = self._define_object(
                listen_auth_settings, As2BasicAuthInfo
            )
        if mdn_signature_public_certificate is not SENTINEL:
            self.mdn_signature_public_certificate = self._define_object(
                mdn_signature_public_certificate, PublicCertificate
            )
        if messages_to_check_for_duplicates is not SENTINEL:
            self.messages_to_check_for_duplicates = messages_to_check_for_duplicates
        if reject_duplicate_messages is not SENTINEL:
            self.reject_duplicate_messages = reject_duplicate_messages
        if signing_public_certificate is not SENTINEL:
            self.signing_public_certificate = self._define_object(
                signing_public_certificate, PublicCertificate
            )
        self._kwargs = kwargs
