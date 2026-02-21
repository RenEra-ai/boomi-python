
from __future__ import annotations
from enum import Enum
from typing import List, TYPE_CHECKING
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL

if TYPE_CHECKING:
    from .account_cloud_attachment_summary_expression import AccountCloudAttachmentSummaryExpression, AccountCloudAttachmentSummaryExpressionGuard
from .account_cloud_attachment_summary_simple_expression import AccountCloudAttachmentSummarySimpleExpression

class AccountCloudAttachmentSummaryGroupingExpressionOperator(Enum):
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
                lambda x: x.value, AccountCloudAttachmentSummaryGroupingExpressionOperator._member_map_.values()
            )
        )

@JsonMap({"nested_expression": "nestedExpression"})
class AccountCloudAttachmentSummaryGroupingExpression(BaseModel):
    """AccountCloudAttachmentSummaryGroupingExpression

    :param nested_expression: nested_expression, defaults to None
    :type nested_expression: List["AccountCloudAttachmentSummaryExpression"], optional
    :param operator: operator
    :type operator: AccountCloudAttachmentSummaryGroupingExpressionOperator
    """

    def __init__(
        self,
        operator: AccountCloudAttachmentSummaryGroupingExpressionOperator,
        nested_expression: List["AccountCloudAttachmentSummaryExpression"] = SENTINEL,
        **kwargs,
    ):
        """AccountCloudAttachmentSummaryGroupingExpression

        :param nested_expression: nested_expression, defaults to None
        :type nested_expression: List["AccountCloudAttachmentSummaryExpression"], optional
        :param operator: operator
        :type operator: AccountCloudAttachmentSummaryGroupingExpressionOperator
        """
        if nested_expression is not SENTINEL:

            from .account_cloud_attachment_summary_expression import AccountCloudAttachmentSummaryExpression

            self.nested_expression = self._define_list(
                nested_expression, AccountCloudAttachmentSummaryExpression
            )
        self.operator = self._enum_matching(
            operator, AccountCloudAttachmentSummaryGroupingExpressionOperator.list(), "operator"
        )
        self._kwargs = kwargs
