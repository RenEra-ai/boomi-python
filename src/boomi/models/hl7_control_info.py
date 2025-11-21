
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .msh_control_info import MshControlInfo


@JsonMap({"msh_control_info": "MSHControlInfo"})
class Hl7ControlInfo(BaseModel):
    """Hl7ControlInfo

    :param msh_control_info: msh_control_info, defaults to None
    :type msh_control_info: MshControlInfo, optional
    """

    def __init__(self, msh_control_info: MshControlInfo = SENTINEL, **kwargs):
        """Hl7ControlInfo

        :param msh_control_info: msh_control_info, defaults to None
        :type msh_control_info: MshControlInfo, optional
        """
        if msh_control_info is not SENTINEL:
            self.msh_control_info = self._define_object(msh_control_info, MshControlInfo)
        self._kwargs = kwargs
