
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .custom_control_info import CustomControlInfo
from .custom_options import CustomOptions


@JsonMap(
    {
        "custom_control_info": "CustomControlInfo",
        "custom_options": "CustomOptions",
        "custom_standard_id": "customStandardId",
    }
)
class CustomPartnerInfo(BaseModel):
    """CustomPartnerInfo

    :param custom_control_info: custom_control_info
    :type custom_control_info: CustomControlInfo
    :param custom_options: custom_options
    :type custom_options: CustomOptions
    :param custom_standard_id: ID of the Custom Document Standard., defaults to None
    :type custom_standard_id: str, optional
    """

    def __init__(
        self,
        custom_control_info: CustomControlInfo,
        custom_options: CustomOptions,
        custom_standard_id: str = SENTINEL,
        **kwargs,
    ):
        """CustomPartnerInfo

        :param custom_control_info: custom_control_info
        :type custom_control_info: CustomControlInfo
        :param custom_options: custom_options
        :type custom_options: CustomOptions
        :param custom_standard_id: ID of the Custom Document Standard., defaults to None
        :type custom_standard_id: str, optional
        """
        self.custom_control_info = self._define_object(
            custom_control_info, CustomControlInfo
        )
        self.custom_options = self._define_object(custom_options, CustomOptions)
        if custom_standard_id is not SENTINEL:
            self.custom_standard_id = custom_standard_id
        self._kwargs = kwargs
