
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .runtime_cloud_expression import RuntimeCloudExpression, RuntimeCloudExpressionGuard
from .runtime_cloud_simple_expression import RuntimeCloudSimpleExpression
from .runtime_cloud_grouping_expression import RuntimeCloudGroupingExpression


@JsonMap({})
class RuntimeCloudQueryConfigQueryFilter(BaseModel):
    """RuntimeCloudQueryConfigQueryFilter

    :param expression: expression
    :type expression: RuntimeCloudExpression
    """

    def __init__(self, expression: RuntimeCloudExpression, **kwargs):
        """RuntimeCloudQueryConfigQueryFilter

        :param expression: expression
        :type expression: RuntimeCloudExpression
        """
        self.expression = RuntimeCloudExpressionGuard.return_one_of(expression)
        self._kwargs = kwargs


@JsonMap({"query_filter": "QueryFilter"})
class RuntimeCloudQueryConfig(BaseModel):
    """RuntimeCloudQueryConfig

    :param query_filter: query_filter
    :type query_filter: RuntimeCloudQueryConfigQueryFilter
    """

    def __init__(self, query_filter: RuntimeCloudQueryConfigQueryFilter, **kwargs):
        """RuntimeCloudQueryConfig

        :param query_filter: query_filter
        :type query_filter: RuntimeCloudQueryConfigQueryFilter
        """
        self.query_filter = self._define_object(
            query_filter, RuntimeCloudQueryConfigQueryFilter
        )
        self._kwargs = kwargs
