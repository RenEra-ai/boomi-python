
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .property import Property


@JsonMap({})
class CustomRuntimeProperties(BaseModel):
    """CustomRuntimeProperties

    :param property: property
    :type property: List[Property]
    """

    def __init__(self, property: List[Property], **kwargs):
        """CustomRuntimeProperties

        :param property: property
        :type property: List[Property]
        """
        self.property = self._define_list(property, Property)
        self._kwargs = kwargs
