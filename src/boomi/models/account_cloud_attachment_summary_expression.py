
from __future__ import annotations
from typing import Union
from .utils.one_of_base_model import OneOfBaseModel
from .account_cloud_attachment_summary_simple_expression import AccountCloudAttachmentSummarySimpleExpression
from .account_cloud_attachment_summary_grouping_expression import AccountCloudAttachmentSummaryGroupingExpression


class AccountCloudAttachmentSummaryExpressionGuard(OneOfBaseModel):
    class_list = {
        "AccountCloudAttachmentSummarySimpleExpression": AccountCloudAttachmentSummarySimpleExpression,
        "AccountCloudAttachmentSummaryGroupingExpression": AccountCloudAttachmentSummaryGroupingExpression,
    }


AccountCloudAttachmentSummaryExpression = Union[AccountCloudAttachmentSummarySimpleExpression, AccountCloudAttachmentSummaryGroupingExpression]
