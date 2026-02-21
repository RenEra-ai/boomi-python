
from enum import Enum
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


class RuntimeCloudSimpleExpressionOperator(Enum):
    """An enumeration representing different categories.

    :cvar EQUALS: "EQUALS"
    :vartype EQUALS: str
    :cvar LIKE: "LIKE"
    :vartype LIKE: str
    :cvar NOTEQUALS: "NOT_EQUALS"
    :vartype NOTEQUALS: str
    :cvar ISNULL: "IS_NULL"
    :vartype ISNULL: str
    :cvar ISNOTNULL: "IS_NOT_NULL"
    :vartype ISNOTNULL: str
    :cvar BETWEEN: "BETWEEN"
    :vartype BETWEEN: str
    :cvar GREATERTHAN: "GREATER_THAN"
    :vartype GREATERTHAN: str
    :cvar GREATERTHANOREQUAL: "GREATER_THAN_OR_EQUAL"
    :vartype GREATERTHANOREQUAL: str
    :cvar LESSTHAN: "LESS_THAN"
    :vartype LESSTHAN: str
    :cvar LESSTHANOREQUAL: "LESS_THAN_OR_EQUAL"
    :vartype LESSTHANOREQUAL: str
    :cvar CONTAINS: "CONTAINS"
    :vartype CONTAINS: str
    :cvar NOTCONTAINS: "NOT_CONTAINS"
    :vartype NOTCONTAINS: str
    """

    EQUALS = "EQUALS"
    LIKE = "LIKE"
    NOTEQUALS = "NOT_EQUALS"
    ISNULL = "IS_NULL"
    ISNOTNULL = "IS_NOT_NULL"
    BETWEEN = "BETWEEN"
    GREATERTHAN = "GREATER_THAN"
    GREATERTHANOREQUAL = "GREATER_THAN_OR_EQUAL"
    LESSTHAN = "LESS_THAN"
    LESSTHANOREQUAL = "LESS_THAN_OR_EQUAL"
    CONTAINS = "CONTAINS"
    NOTCONTAINS = "NOT_CONTAINS"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, RuntimeCloudSimpleExpressionOperator._member_map_.values())
        )


class RuntimeCloudSimpleExpressionProperty(Enum):
    """An enumeration representing different categories.

    :cvar NAME: "name"
    :vartype NAME: str
    :cvar ID: "id"
    :vartype ID: str
    :cvar CLASSIFICATION: "classification"
    :vartype CLASSIFICATION: str
    :cvar ALLOWDEPLOYMENTS: "allowDeployments"
    :vartype ALLOWDEPLOYMENTS: str
    :cvar ALLOWBROWSING: "allowBrowsing"
    :vartype ALLOWBROWSING: str
    :cvar ALLOWTESTEXECUTIONS: "allowTestExecutions"
    :vartype ALLOWTESTEXECUTIONS: str
    :cvar MAXATTACHMENTSPERACCOUNT: "maxAttachmentsPerAccount"
    :vartype MAXATTACHMENTSPERACCOUNT: str
    :cvar CREATEDDATE: "createdDate"
    :vartype CREATEDDATE: str
    :cvar MODIFIEDDATE: "modifiedDate"
    :vartype MODIFIEDDATE: str
    :cvar CREATEDBY: "createdBy"
    :vartype CREATEDBY: str
    :cvar MODIFIEDBY: "modifiedBy"
    :vartype MODIFIEDBY: str
    """

    NAME = "name"
    ID = "id"
    CLASSIFICATION = "classification"
    ALLOWDEPLOYMENTS = "allowDeployments"
    ALLOWBROWSING = "allowBrowsing"
    ALLOWTESTEXECUTIONS = "allowTestExecutions"
    MAXATTACHMENTSPERACCOUNT = "maxAttachmentsPerAccount"
    CREATEDDATE = "createdDate"
    MODIFIEDDATE = "modifiedDate"
    CREATEDBY = "createdBy"
    MODIFIEDBY = "modifiedBy"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, RuntimeCloudSimpleExpressionProperty._member_map_.values())
        )


@JsonMap({})
class RuntimeCloudSimpleExpression(BaseModel):
    """RuntimeCloudSimpleExpression

    :param argument: argument, defaults to None
    :type argument: List[str], optional
    :param operator: operator
    :type operator: RuntimeCloudSimpleExpressionOperator
    :param property: property
    :type property: RuntimeCloudSimpleExpressionProperty
    """

    def __init__(
        self,
        operator: RuntimeCloudSimpleExpressionOperator,
        property: RuntimeCloudSimpleExpressionProperty,
        argument: List[str] = SENTINEL,
        **kwargs
    ):
        """RuntimeCloudSimpleExpression

        :param argument: argument, defaults to None
        :type argument: List[str], optional
        :param operator: operator
        :type operator: RuntimeCloudSimpleExpressionOperator
        :param property: property
        :type property: RuntimeCloudSimpleExpressionProperty
        """
        if argument is not SENTINEL:
            self.argument = argument
        self.operator = self._enum_matching(
            operator, RuntimeCloudSimpleExpressionOperator.list(), "operator"
        )
        self.property = self._enum_matching(
            property, RuntimeCloudSimpleExpressionProperty.list(), "property"
        )
        self._kwargs = kwargs
