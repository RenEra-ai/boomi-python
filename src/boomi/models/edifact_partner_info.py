
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .edifact_control_info import EdifactControlInfo
from .edifact_options import EdifactOptions


@JsonMap(
    {"edifact_control_info": "EdifactControlInfo", "edifact_options": "EdifactOptions"}
)
class EdifactPartnerInfo(BaseModel):
    """EdifactPartnerInfo

    :param edifact_control_info: edifact_control_info
    :type edifact_control_info: EdifactControlInfo
    :param edifact_options: edifact_options
    :type edifact_options: EdifactOptions
    """

    def __init__(
        self,
        edifact_control_info: EdifactControlInfo = SENTINEL,
        edifact_options: EdifactOptions = SENTINEL,
        **kwargs,
    ):
        """EdifactPartnerInfo

        :param edifact_control_info: edifact_control_info, defaults to None
        :type edifact_control_info: EdifactControlInfo, optional
        :param edifact_options: edifact_options, defaults to None
        :type edifact_options: EdifactOptions, optional
        """
        if edifact_control_info is not SENTINEL:
            self.edifact_control_info = self._define_object(
                edifact_control_info, EdifactControlInfo
            )
        if edifact_options is not SENTINEL:
            self.edifact_options = self._define_object(edifact_options, EdifactOptions)
        self._kwargs = kwargs
