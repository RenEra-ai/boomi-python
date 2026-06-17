
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..models import (
    IntegrationPack,
    IntegrationPackBulkRequest,
    IntegrationPackBulkResponse,
    IntegrationPackQueryConfig,
    IntegrationPackQueryResponse,
)


class IntegrationPackService(BaseService):

    @cast_models
    def get_integration_pack(self, id_: str) -> Union[IntegrationPack, str, dict]:
        """Retrieves the properties of the integration pack with a specified ID. The ordinary GET operation retrieves the properties of the integration pack with a specified ID. The bulk GET operation retrieves the properties of the integration packs having the specified IDs, to a maximum of 100.

        :param id_: A unique ID assigned by the system to the integration pack.
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[IntegrationPack, str, dict]
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/IntegrationPack/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        return self._deserialize_or_raw(IntegrationPack, response, status, content)

    @cast_models
    def bulk_integration_pack(
        self, request_body: IntegrationPackBulkRequest = None
    ) -> Union[IntegrationPackBulkResponse, str, dict]:
        """To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

        :param request_body: The request body., defaults to None
        :type request_body: IntegrationPackBulkRequest, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[IntegrationPackBulkResponse, str, dict]
        """

        Validator(IntegrationPackBulkRequest).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/IntegrationPack/bulk",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        return self._deserialize_or_raw(
            IntegrationPackBulkResponse, response, status, content
        )

    @cast_models
    def query_integration_pack(
        self, request_body: IntegrationPackQueryConfig = None
    ) -> Union[IntegrationPackQueryResponse, str, dict]:
        """For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body., defaults to None
        :type request_body: IntegrationPackQueryConfig, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[IntegrationPackQueryResponse, str, dict]
        """

        Validator(IntegrationPackQueryConfig).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/IntegrationPack/query",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        return self._deserialize_or_raw(
            IntegrationPackQueryResponse, response, status, content
        )

    @cast_models
    def query_more_integration_pack(
        self, request_body: str
    ) -> Union[IntegrationPackQueryResponse, str, dict]:
        """To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body.
        :type request_body: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[IntegrationPackQueryResponse, str, dict]
        """

        Validator(str).validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/IntegrationPack/queryMore",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body, "text/plain")
        )

        response, status, content = self.send_request(serialized_request)
        return self._deserialize_or_raw(
            IntegrationPackQueryResponse, response, status, content
        )
