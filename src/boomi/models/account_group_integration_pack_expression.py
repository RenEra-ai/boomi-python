
from __future__ import annotations
from typing import Union
from .utils.one_of_base_model import OneOfBaseModel
from .account_group_integration_pack_simple_expression import (
    AccountGroupIntegrationPackSimpleExpression,
)
from .account_group_integration_pack_grouping_expression import (
    AccountGroupIntegrationPackGroupingExpression,
)


class AccountGroupIntegrationPackExpressionGuard(OneOfBaseModel):
    class_list = {
        "AccountGroupIntegrationPackSimpleExpression": AccountGroupIntegrationPackSimpleExpression,
        "AccountGroupIntegrationPackGroupingExpression": AccountGroupIntegrationPackGroupingExpression,
    }


AccountGroupIntegrationPackExpression = Union[
    AccountGroupIntegrationPackSimpleExpression,
    AccountGroupIntegrationPackGroupingExpression,
]
