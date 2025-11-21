
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .hd_type import HdType
from .processing_type import ProcessingType


@JsonMap(
    {
        "application": "Application",
        "facility": "Facility",
        "network_address": "NetworkAddress",
        "processing_id": "ProcessingId",
    }
)
class MshControlInfo(BaseModel):
    """MshControlInfo

    :param application: application, defaults to None
    :type application: HdType, optional
    :param facility: facility, defaults to None
    :type facility: HdType, optional
    :param network_address: network_address, defaults to None
    :type network_address: HdType, optional
    :param processing_id: processing_id, defaults to None
    :type processing_id: ProcessingType, optional
    """

    def __init__(
        self,
        application: HdType = SENTINEL,
        facility: HdType = SENTINEL,
        network_address: HdType = SENTINEL,
        processing_id: ProcessingType = SENTINEL,
        **kwargs,
    ):
        """MshControlInfo

        :param application: application, defaults to None
        :type application: HdType, optional
        :param facility: facility, defaults to None
        :type facility: HdType, optional
        :param network_address: network_address, defaults to None
        :type network_address: HdType, optional
        :param processing_id: processing_id, defaults to None
        :type processing_id: ProcessingType, optional
        """
        if application is not SENTINEL:
            self.application = self._define_object(application, HdType)
        if facility is not SENTINEL:
            self.facility = self._define_object(facility, HdType)
        if network_address is not SENTINEL:
            self.network_address = self._define_object(network_address, HdType)
        if processing_id is not SENTINEL:
            self.processing_id = self._define_object(processing_id, ProcessingType)
        self._kwargs = kwargs
