
from __future__ import annotations
from enum import Enum
from typing import List, TYPE_CHECKING
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL

if TYPE_CHECKING:
    from .runtime_cloud_expression import RuntimeCloudExpression, RuntimeCloudExpressionGuard
from .runtime_cloud_simple_expression import RuntimeCloudSimpleExpression

class RuntimeCloudGroupingExpressionOperator(Enum):
    """An enumeration representing different categories.

    :cvar AND: "and"
    :vartype AND: str
    :cvar OR: "or"
    :vartype OR: str
    """

    AND = "and"
    OR = "or"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(
                lambda x: x.value, RuntimeCloudGroupingExpressionOperator._member_map_.values()
            )
        )

@JsonMap({"nested_expression": "nestedExpression"})
class RuntimeCloudGroupingExpression(BaseModel):
    """RuntimeCloudGroupingExpression

    :param nested_expression: nested_expression, defaults to None
    :type nested_expression: List["RuntimeCloudExpression"], optional
    :param operator: operator
    :type operator: RuntimeCloudGroupingExpressionOperator
    """

    def __init__(
        self,
        operator: RuntimeCloudGroupingExpressionOperator,
        nested_expression: List["RuntimeCloudExpression"] = SENTINEL,
        **kwargs,
    ):
        """RuntimeCloudGroupingExpression

        :param nested_expression: nested_expression, defaults to None
        :type nested_expression: List["RuntimeCloudExpression"], optional
        :param operator: operator
        :type operator: RuntimeCloudGroupingExpressionOperator
        """
        if nested_expression is not SENTINEL:

            from .runtime_cloud_expression import RuntimeCloudExpression

            self.nested_expression = self._define_list(
                nested_expression, RuntimeCloudExpression
            )
        self.operator = self._enum_matching(
            operator, RuntimeCloudGroupingExpressionOperator.list(), "operator"
        )
        self._kwargs = kwargs
