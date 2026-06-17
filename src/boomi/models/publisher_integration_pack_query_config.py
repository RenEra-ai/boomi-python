
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .publisher_integration_pack_expression import (
    PublisherIntegrationPackExpression,
    PublisherIntegrationPackExpressionGuard,
)
from .publisher_integration_pack_simple_expression import (
    PublisherIntegrationPackSimpleExpression,
)
from .publisher_integration_pack_grouping_expression import (
    PublisherIntegrationPackGroupingExpression,
)


@JsonMap({})
class PublisherIntegrationPackQueryConfigQueryFilter(BaseModel):
    """PublisherIntegrationPackQueryConfigQueryFilter

    :param expression: expression
    :type expression: PublisherIntegrationPackExpression
    """

    def __init__(self, expression: PublisherIntegrationPackExpression, **kwargs):
        """PublisherIntegrationPackQueryConfigQueryFilter

        :param expression: expression
        :type expression: PublisherIntegrationPackExpression
        """
        self.expression = PublisherIntegrationPackExpressionGuard.return_one_of(
            expression
        )
        self._kwargs = kwargs


@JsonMap({"query_filter": "QueryFilter"})
class PublisherIntegrationPackQueryConfig(BaseModel):
    """PublisherIntegrationPackQueryConfig

    :param query_filter: query_filter
    :type query_filter: PublisherIntegrationPackQueryConfigQueryFilter
    """

    def __init__(
        self, query_filter: PublisherIntegrationPackQueryConfigQueryFilter, **kwargs
    ):
        """PublisherIntegrationPackQueryConfig

        :param query_filter: query_filter
        :type query_filter: PublisherIntegrationPackQueryConfigQueryFilter
        """
        self.query_filter = self._define_object(
            query_filter, PublisherIntegrationPackQueryConfigQueryFilter
        )
        self._kwargs = kwargs
