
from __future__ import annotations
from enum import Enum
from typing import List, TYPE_CHECKING
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL

if TYPE_CHECKING:
    from .publisher_integration_pack_expression import (
        PublisherIntegrationPackExpression,
        PublisherIntegrationPackExpressionGuard,
    )
from .publisher_integration_pack_simple_expression import (
    PublisherIntegrationPackSimpleExpression,
)


class PublisherIntegrationPackGroupingExpressionOperator(Enum):
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
                lambda x: x.value,
                PublisherIntegrationPackGroupingExpressionOperator._member_map_.values(),
            )
        )


@JsonMap({"nested_expression": "nestedExpression"})
class PublisherIntegrationPackGroupingExpression(BaseModel):
    """PublisherIntegrationPackGroupingExpression

    :param nested_expression: nested_expression, defaults to None
    :type nested_expression: List[PublisherIntegrationPackExpression], optional
    :param operator: operator
    :type operator: PublisherIntegrationPackGroupingExpressionOperator
    """

    def __init__(
        self,
        operator: PublisherIntegrationPackGroupingExpressionOperator,
        nested_expression: List[PublisherIntegrationPackExpression] = SENTINEL,
        **kwargs,
    ):
        """PublisherIntegrationPackGroupingExpression

        :param nested_expression: nested_expression, defaults to None
        :type nested_expression: List[PublisherIntegrationPackExpression], optional
        :param operator: operator
        :type operator: PublisherIntegrationPackGroupingExpressionOperator
        """
        if nested_expression is not SENTINEL:

            from .publisher_integration_pack_expression import (
                PublisherIntegrationPackExpression,
            )

            self.nested_expression = self._define_list(
                nested_expression, PublisherIntegrationPackExpression
            )
        self.operator = self._enum_matching(
            operator,
            PublisherIntegrationPackGroupingExpressionOperator.list(),
            "operator",
        )
        self._kwargs = kwargs
