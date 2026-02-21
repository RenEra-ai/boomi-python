
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel


@JsonMap({})
class CustomSystemProperties(BaseModel):
    """CustomSystemProperties

    :param property: property
    :type property: List[str]
    """

    def __init__(self, property: List[str], **kwargs):
        """CustomSystemProperties

        :param property: property
        :type property: List[str]
        """
        self.property = property
        self._kwargs = kwargs
