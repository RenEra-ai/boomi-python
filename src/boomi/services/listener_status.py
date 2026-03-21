
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.api_error import ApiError
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..net.transport.utils import parse_xml_to_dict
from ..models import (
    AsyncOperationTokenResult,
    ListenerStatusAsyncResponse,
    ListenerStatusQueryConfig,
)


def _has_container_id_equals(expr):
    """Walk an expression tree and return True if it contains at least one
    containerId EQUALS simple expression with a non-empty argument."""
    # SimpleExpression: has .property and .operator attributes
    if hasattr(expr, 'property') and hasattr(expr, 'operator'):
        prop = getattr(expr.property, 'value', expr.property)
        op = getattr(expr.operator, 'value', expr.operator)
        if prop == "containerId" and op == "EQUALS":
            arg = getattr(expr, 'argument', None)
            if arg and isinstance(arg, list) and any(a for a in arg):
                return True
        return False
    # GroupingExpression: has .nested_expression list
    if hasattr(expr, 'nested_expression'):
        nested = getattr(expr, 'nested_expression', None)
        if nested:
            return any(_has_container_id_equals(child) for child in nested)
    return False


def _validate_listener_status_query(request_body):
    """Validate that a ListenerStatus query contains a required containerId EQUALS expression."""
    if request_body is None:
        raise ValueError("request_body is required for async_get_listener_status")
    qf = getattr(request_body, 'query_filter', None)
    if qf is None:
        raise ValueError("request_body must have a query_filter with a containerId EQUALS expression")
    expr = getattr(qf, 'expression', None)
    if expr is None:
        raise ValueError("query must contain at least one containerId EQUALS expression with a non-empty argument")
    if not _has_container_id_equals(expr):
        raise ValueError("query must contain at least one containerId EQUALS expression with a non-empty argument")


class ListenerStatusService(BaseService):

    @cast_models
    def async_get_listener_status(
        self, request_body: ListenerStatusQueryConfig
    ) -> Union[AsyncOperationTokenResult, str]:
        """Send an HTTP POST where {accountId} is the ID of the authenticating account for the request.
         >**Note:** For backward compatibility, Boomi continues to support the legacy URL: https://api.boomi.com/api/rest/v1/accountId/ListenerStatus/query/async.

         For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body. Must include a containerId EQUALS expression.
        :type request_body: ListenerStatusQueryConfig
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[AsyncOperationTokenResult, str]
        """

        if request_body is None:
            raise ValueError("request_body is required for async_get_listener_status")
        Validator(ListenerStatusQueryConfig).validate(request_body)
        _validate_listener_status_query(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/async/ListenerStatus/query",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return AsyncOperationTokenResult._unmap(response)
        if content == "application/xml":
            return AsyncOperationTokenResult._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def async_token_listener_status(
        self, token: str
    ) -> Union[ListenerStatusAsyncResponse, str]:
        """The ordinary GET operation retrieves async results from the QUERY. Send an HTTP GET where {accountId} is the account that you are authenticating with and {token} is the listener status token returned by your QUERY request.
         >**Note:** For backward compatibility, Boomi continues to support the legacy URL: https://api.boomi.com/api/rest/v1/accountId/ListenerStatus/query/async.

        :param token: Takes in the token from a previous call to return a result.
        :type token: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[ListenerStatusAsyncResponse, str]
        """

        Validator(str).validate(token)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/async/ListenerStatus/response/{{token}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("token", token)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return ListenerStatusAsyncResponse._unmap(response)
        if content == "application/xml":
            return ListenerStatusAsyncResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)
