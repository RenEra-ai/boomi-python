
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .account_cloud_attachment_summary_expression import AccountCloudAttachmentSummaryExpression, AccountCloudAttachmentSummaryExpressionGuard
from .account_cloud_attachment_summary_simple_expression import AccountCloudAttachmentSummarySimpleExpression
from .account_cloud_attachment_summary_grouping_expression import AccountCloudAttachmentSummaryGroupingExpression


@JsonMap({})
class AccountCloudAttachmentSummaryQueryConfigQueryFilter(BaseModel):
    """AccountCloudAttachmentSummaryQueryConfigQueryFilter

    :param expression: expression
    :type expression: AccountCloudAttachmentSummaryExpression
    """

    def __init__(self, expression: AccountCloudAttachmentSummaryExpression, **kwargs):
        """AccountCloudAttachmentSummaryQueryConfigQueryFilter

        :param expression: expression
        :type expression: AccountCloudAttachmentSummaryExpression
        """
        self.expression = AccountCloudAttachmentSummaryExpressionGuard.return_one_of(expression)
        self._kwargs = kwargs


@JsonMap({"query_filter": "QueryFilter"})
class AccountCloudAttachmentSummaryQueryConfig(BaseModel):
    """AccountCloudAttachmentSummaryQueryConfig

    :param query_filter: query_filter
    :type query_filter: AccountCloudAttachmentSummaryQueryConfigQueryFilter
    """

    def __init__(self, query_filter: AccountCloudAttachmentSummaryQueryConfigQueryFilter, **kwargs):
        """AccountCloudAttachmentSummaryQueryConfig

        :param query_filter: query_filter
        :type query_filter: AccountCloudAttachmentSummaryQueryConfigQueryFilter
        """
        self.query_filter = self._define_object(
            query_filter, AccountCloudAttachmentSummaryQueryConfigQueryFilter
        )
        self._kwargs = kwargs
