
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


class OutboundValidationOptionCustom(Enum):
    """An enumeration representing different categories.

    :cvar FILTERERROR: "filterError"
    :vartype FILTERERROR: str
    :cvar FAILALL: "failAll"
    :vartype FAILALL: str
    """

    FILTERERROR = "filterError"
    FAILALL = "failAll"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(
                lambda x: x.value,
                OutboundValidationOptionCustom._member_map_.values(),
            )
        )


@JsonMap(
    {
        "outbound_message_validation": "outboundMessageValidation",
        "outbound_validation_option": "outboundValidationOption",
        "reject_duplicate_message": "rejectDuplicateMessage",
    }
)
class CustomOptions(BaseModel):
    """CustomOptions

    :param outbound_message_validation: outbound_message_validation, defaults to None
    :type outbound_message_validation: bool, optional
    :param outbound_validation_option: outbound_validation_option, defaults to None
    :type outbound_validation_option: OutboundValidationOptionCustom, optional
    :param reject_duplicate_message: reject_duplicate_message, defaults to None
    :type reject_duplicate_message: bool, optional
    """

    def __init__(
        self,
        outbound_message_validation: bool = SENTINEL,
        outbound_validation_option: OutboundValidationOptionCustom = SENTINEL,
        reject_duplicate_message: bool = SENTINEL,
        **kwargs,
    ):
        """CustomOptions

        :param outbound_message_validation: outbound_message_validation, defaults to None
        :type outbound_message_validation: bool, optional
        :param outbound_validation_option: outbound_validation_option, defaults to None
        :type outbound_validation_option: OutboundValidationOptionCustom, optional
        :param reject_duplicate_message: reject_duplicate_message, defaults to None
        :type reject_duplicate_message: bool, optional
        """
        if outbound_message_validation is not SENTINEL:
            self.outbound_message_validation = outbound_message_validation
        if outbound_validation_option is not SENTINEL:
            self.outbound_validation_option = self._enum_matching(
                outbound_validation_option,
                OutboundValidationOptionCustom.list(),
                "outbound_validation_option",
            )
        if reject_duplicate_message is not SENTINEL:
            self.reject_duplicate_message = reject_duplicate_message
        self._kwargs = kwargs
