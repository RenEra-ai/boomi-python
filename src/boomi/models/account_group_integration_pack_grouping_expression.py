
from __future__ import annotations
from enum import Enum
from typing import List, TYPE_CHECKING
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL

if TYPE_CHECKING:
    from .account_group_integration_pack_expression import (
        AccountGroupIntegrationPackExpression,
        AccountGroupIntegrationPackExpressionGuard,
    )
from .account_group_integration_pack_simple_expression import (
    AccountGroupIntegrationPackSimpleExpression,
)


class AccountGroupIntegrationPackGroupingExpressionOperator(Enum):
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
                AccountGroupIntegrationPackGroupingExpressionOperator._member_map_.values(),
            )
        )


@JsonMap({"nested_expression": "nestedExpression"})
class AccountGroupIntegrationPackGroupingExpression(BaseModel):
    """AccountGroupIntegrationPackGroupingExpression

    :param nested_expression: nested_expression, defaults to None
    :type nested_expression: List[AccountGroupIntegrationPackExpression], optional
    :param operator: operator
    :type operator: AccountGroupIntegrationPackGroupingExpressionOperator
    """

    def __init__(
        self,
        operator: AccountGroupIntegrationPackGroupingExpressionOperator,
        nested_expression: List[AccountGroupIntegrationPackExpression] = SENTINEL,
        **kwargs,
    ):
        """AccountGroupIntegrationPackGroupingExpression

        :param nested_expression: nested_expression, defaults to None
        :type nested_expression: List[AccountGroupIntegrationPackExpression], optional
        :param operator: operator
        :type operator: AccountGroupIntegrationPackGroupingExpressionOperator
        """
        if nested_expression is not SENTINEL:

            from .account_group_integration_pack_expression import (
                AccountGroupIntegrationPackExpression,
            )

            self.nested_expression = self._define_list(
                nested_expression, AccountGroupIntegrationPackExpression
            )
        self.operator = self._enum_matching(
            operator,
            AccountGroupIntegrationPackGroupingExpressionOperator.list(),
            "operator",
        )
        self._kwargs = kwargs
