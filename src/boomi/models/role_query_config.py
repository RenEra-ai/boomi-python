
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .role_expression import RoleExpression, RoleExpressionGuard
from .role_simple_expression import RoleSimpleExpression
from .role_grouping_expression import RoleGroupingExpression


@JsonMap({})
class RoleQueryConfigQueryFilter(BaseModel):
    """RoleQueryConfigQueryFilter

    :param expression: expression, defaults to None
    :type expression: RoleExpression, optional
    """

    def __init__(self, expression: RoleExpression = SENTINEL, **kwargs):
        """RoleQueryConfigQueryFilter

        :param expression: expression, defaults to None
        :type expression: RoleExpression, optional
        """
        if expression is not SENTINEL and expression is not None:
            self.expression = RoleExpressionGuard.return_one_of(expression)
        self._kwargs = kwargs


@JsonMap({"query_filter": "QueryFilter"})
class RoleQueryConfig(BaseModel):
    """RoleQueryConfig

    :param query_filter: query_filter, defaults to None
    :type query_filter: RoleQueryConfigQueryFilter, optional
    """

    def __init__(self, query_filter: RoleQueryConfigQueryFilter = SENTINEL, **kwargs):
        """RoleQueryConfig

        Boomi accepts an empty ``{"QueryFilter": {}}`` body for "list all roles"
        style queries. When no filter (or an empty one) is supplied, store a
        plain empty dict so ``_map()`` serializes ``QueryFilter`` as ``{}``.

        :param query_filter: query_filter, defaults to None
        :type query_filter: RoleQueryConfigQueryFilter, optional
        """
        # cast_models constructs RoleQueryConfig(**data) for dict input, so a
        # caller-supplied OpenAPI-keyed filter ({"QueryFilter": {...}}) arrives
        # in kwargs rather than query_filter. Pull it back so a real filter is
        # never silently dropped and turned into an unfiltered list-all query.
        if query_filter is SENTINEL and "QueryFilter" in kwargs:
            query_filter = kwargs.pop("QueryFilter")
        # Also handle a whole OpenAPI body passed directly as the filter, e.g.
        # RoleQueryConfig({"QueryFilter": {...}}); unwrap it so the inner filter
        # is not mistaken for an empty filter and silently dropped.
        if isinstance(query_filter, dict) and "QueryFilter" in query_filter:
            query_filter = query_filter["QueryFilter"]
        if query_filter is SENTINEL or query_filter is None or query_filter == {}:
            self.query_filter = {}
        else:
            obj = self._define_object(query_filter, RoleQueryConfigQueryFilter)
            # An expression-less filter (RoleQueryConfigQueryFilter() or
            # expression=None) is the documented "list all roles" empty filter;
            # serialize it as {} so the wire body is {"QueryFilter": {}} rather
            # than {"QueryFilter": {"@type": "RoleQueryConfigQueryFilter"}}.
            self.query_filter = obj if (obj is not None and hasattr(obj, "expression")) else {}
        self._kwargs = kwargs
