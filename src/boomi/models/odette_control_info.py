
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .odette_unb_control_info import OdetteUnbControlInfo
from .odette_unh_control_info import OdetteUnhControlInfo


@JsonMap(
    {
        "odette_unb_control_info": "OdetteUNBControlInfo",
        "odette_unh_control_info": "OdetteUNHControlInfo",
    }
)
class OdetteControlInfo(BaseModel):
    """OdetteControlInfo

    :param odette_unb_control_info: odette_unb_control_info, defaults to None
    :type odette_unb_control_info: OdetteUnbControlInfo, optional
    :param odette_unh_control_info: odette_unh_control_info, defaults to None
    :type odette_unh_control_info: OdetteUnhControlInfo, optional
    """

    def __init__(
        self,
        odette_unb_control_info: OdetteUnbControlInfo = SENTINEL,
        odette_unh_control_info: OdetteUnhControlInfo = SENTINEL,
        **kwargs,
    ):
        """OdetteControlInfo

        :param odette_unb_control_info: odette_unb_control_info, defaults to None
        :type odette_unb_control_info: OdetteUnbControlInfo, optional
        :param odette_unh_control_info: odette_unh_control_info, defaults to None
        :type odette_unh_control_info: OdetteUnhControlInfo, optional
        """
        if odette_unb_control_info is not SENTINEL:
            self.odette_unb_control_info = self._define_object(
                odette_unb_control_info, OdetteUnbControlInfo
            )
        if odette_unh_control_info is not SENTINEL:
            self.odette_unh_control_info = self._define_object(
                odette_unh_control_info, OdetteUnhControlInfo
            )
        self._kwargs = kwargs
