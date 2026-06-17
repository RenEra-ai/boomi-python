
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..models import (
    ThroughputAccountGroupQueryConfig,
    ThroughputAccountGroupQueryResponse,
)


class ThroughputAccountGroupService(BaseService):

    @cast_models
    def query_throughput_account_group(
        self, request_body: ThroughputAccountGroupQueryConfig = None
    ) -> Union[ThroughputAccountGroupQueryResponse, str, dict]:
        """- You can only use the EQUALS operator with the `environmentId` filter parameter.
         - The authenticating user for a QUERY operation must have the Dashboard privilege.

         For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body., defaults to None
        :type request_body: ThroughputAccountGroupQueryConfig, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[ThroughputAccountGroupQueryResponse, str, dict]
        """

        Validator(ThroughputAccountGroupQueryConfig).is_optional().validate(
            request_body
        )

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/ThroughputAccountGroup/query",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        return self._deserialize_or_raw(ThroughputAccountGroupQueryResponse, response, status, content)

    @cast_models
    def query_more_throughput_account_group(
        self, request_body: str
    ) -> Union[ThroughputAccountGroupQueryResponse, str, dict]:
        """To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body.
        :type request_body: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[ThroughputAccountGroupQueryResponse, str, dict]
        """

        Validator(str).validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/ThroughputAccountGroup/queryMore",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body, "text/plain")
        )

        response, status, content = self.send_request(serialized_request)
        return self._deserialize_or_raw(ThroughputAccountGroupQueryResponse, response, status, content)
