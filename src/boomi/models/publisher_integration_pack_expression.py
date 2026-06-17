
from __future__ import annotations
from typing import Union
from .utils.one_of_base_model import OneOfBaseModel
from .publisher_integration_pack_simple_expression import (
    PublisherIntegrationPackSimpleExpression,
)
from .publisher_integration_pack_grouping_expression import (
    PublisherIntegrationPackGroupingExpression,
)


class PublisherIntegrationPackExpressionGuard(OneOfBaseModel):
    class_list = {
        "PublisherIntegrationPackSimpleExpression": PublisherIntegrationPackSimpleExpression,
        "PublisherIntegrationPackGroupingExpression": PublisherIntegrationPackGroupingExpression,
    }


PublisherIntegrationPackExpression = Union[
    PublisherIntegrationPackSimpleExpression,
    PublisherIntegrationPackGroupingExpression,
]
