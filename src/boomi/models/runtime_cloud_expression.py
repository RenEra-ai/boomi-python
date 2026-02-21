
from __future__ import annotations
from typing import Union
from .utils.one_of_base_model import OneOfBaseModel
from .runtime_cloud_simple_expression import RuntimeCloudSimpleExpression
from .runtime_cloud_grouping_expression import RuntimeCloudGroupingExpression


class RuntimeCloudExpressionGuard(OneOfBaseModel):
    class_list = {
        "RuntimeCloudSimpleExpression": RuntimeCloudSimpleExpression,
        "RuntimeCloudGroupingExpression": RuntimeCloudGroupingExpression,
    }


RuntimeCloudExpression = Union[RuntimeCloudSimpleExpression, RuntimeCloudGroupingExpression]
