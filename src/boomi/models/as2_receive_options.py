
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .as2_partner_info import As2PartnerInfo
from .as2_mdn_options import As2MdnOptions
from .as2_message_options import As2MessageOptions
from .as2_my_company_info import As2MyCompanyInfo


@JsonMap(
    {
        "as2_default_partner_info": "AS2DefaultPartnerInfo",
        "as2_default_partner_mdn_options": "AS2DefaultPartnerMDNOptions",
        "as2_default_partner_message_options": "AS2DefaultPartnerMessageOptions",
        "as2_my_company_info": "AS2MyCompanyInfo",
    }
)
class As2ReceiveOptions(BaseModel):
    """As2ReceiveOptions

    :param as2_default_partner_info: as2_default_partner_info, defaults to None
    :type as2_default_partner_info: As2PartnerInfo, optional
    :param as2_default_partner_mdn_options: as2_default_partner_mdn_options, defaults to None
    :type as2_default_partner_mdn_options: As2MdnOptions, optional
    :param as2_default_partner_message_options: as2_default_partner_message_options, defaults to None
    :type as2_default_partner_message_options: As2MessageOptions, optional
    :param as2_my_company_info: as2_my_company_info, defaults to None
    :type as2_my_company_info: As2MyCompanyInfo, optional
    """

    def __init__(
        self,
        as2_default_partner_info: As2PartnerInfo = SENTINEL,
        as2_default_partner_mdn_options: As2MdnOptions = SENTINEL,
        as2_default_partner_message_options: As2MessageOptions = SENTINEL,
        as2_my_company_info: As2MyCompanyInfo = SENTINEL,
        **kwargs,
    ):
        """As2ReceiveOptions

        :param as2_default_partner_info: as2_default_partner_info, defaults to None
        :type as2_default_partner_info: As2PartnerInfo, optional
        :param as2_default_partner_mdn_options: as2_default_partner_mdn_options, defaults to None
        :type as2_default_partner_mdn_options: As2MdnOptions, optional
        :param as2_default_partner_message_options: as2_default_partner_message_options, defaults to None
        :type as2_default_partner_message_options: As2MessageOptions, optional
        :param as2_my_company_info: as2_my_company_info, defaults to None
        :type as2_my_company_info: As2MyCompanyInfo, optional
        """
        if as2_default_partner_info is not SENTINEL:
            self.as2_default_partner_info = self._define_object(
                as2_default_partner_info, As2PartnerInfo
            )
        if as2_default_partner_mdn_options is not SENTINEL:
            self.as2_default_partner_mdn_options = self._define_object(
                as2_default_partner_mdn_options, As2MdnOptions
            )
        if as2_default_partner_message_options is not SENTINEL:
            self.as2_default_partner_message_options = self._define_object(
                as2_default_partner_message_options, As2MessageOptions
            )
        if as2_my_company_info is not SENTINEL:
            self.as2_my_company_info = self._define_object(
                as2_my_company_info, As2MyCompanyInfo
            )
        self._kwargs = kwargs
