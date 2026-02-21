
from __future__ import annotations
from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .observability_authentication_fields import ObservabilityAuthenticationFields


class AuthType(Enum):
    """An enumeration representing different categories.

    :cvar NONE: "NONE"
    :vartype NONE: str
    :cvar BASIC: "BASIC"
    :vartype BASIC: str
    :cvar BEARER_TOKEN: "BEARER_TOKEN"
    :vartype BEARER_TOKEN: str
    """

    NONE = "NONE"
    BASIC = "BASIC"
    BEARER_TOKEN = "BEARER_TOKEN"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, AuthType._member_map_.values()))


@JsonMap({"auth_type": "authType"})
class ObservabilityEndpointAuthentication(BaseModel):
    """ObservabilityEndpointAuthentication

    :param auth_type: auth_type
    :type auth_type: AuthType
    :param fields: fields, defaults to None
    :type fields: List[ObservabilityAuthenticationFields], optional
    """

    def __init__(
        self,
        auth_type: AuthType,
        fields: List[ObservabilityAuthenticationFields] = SENTINEL,
        **kwargs,
    ):
        """ObservabilityEndpointAuthentication

        :param auth_type: auth_type
        :type auth_type: AuthType
        :param fields: fields, defaults to None
        :type fields: List[ObservabilityAuthenticationFields], optional
        """
        self.auth_type = self._enum_matching(
            auth_type, AuthType.list(), "auth_type"
        )
        if fields is not SENTINEL:
            self.fields = self._define_list(
                fields, ObservabilityAuthenticationFields
            )
        self._kwargs = kwargs
