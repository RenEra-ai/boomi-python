
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..models import (
    Connector,
    ConnectorBulkRequest,
    ConnectorBulkResponse,
    ConnectorQueryConfig,
    ConnectorQueryResponse,
)


class ConnectorService(BaseService):

    @cast_models
    def get_connector(self, connector_type: str) -> Union[Connector, str, dict]:
        """You can only perform the GET operation by `type` and not by `name`.

         Send an HTTP GET where `accountId` is the ID of the authenticating account for the request and `connectorType` is the name of the connector subtype you are attempting to GET.

        For example, sending an HTTP GET to `https://api.boomi.com/api/rest/v1/accountId/Connector/database` returns `Database` type connectors available on the account.

        :param connector_type: The internal and unique identifier for connector type, such as `http`, `ftp`, `greatplains`. The [Component Metadata object](/api/platformapi#tag/ComponentMetadata) refers to this field as *subType*.
        :type connector_type: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[Connector, str, dict]
        """

        Validator(str).validate(connector_type)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/Connector/{{connectorType}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("connectorType", connector_type)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        return self._deserialize_or_raw(Connector, response, status, content)

    @cast_models
    def bulk_connector(
        self, request_body: ConnectorBulkRequest = None
    ) -> Union[ConnectorBulkResponse, str, dict]:
        """To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

        :param request_body: The request body., defaults to None
        :type request_body: ConnectorBulkRequest, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[ConnectorBulkResponse, str, dict]
        """

        Validator(ConnectorBulkRequest).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/Connector/bulk",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        return self._deserialize_or_raw(ConnectorBulkResponse, response, status, content)

    @cast_models
    def query_connector(
        self, request_body: ConnectorQueryConfig = None
    ) -> Union[ConnectorQueryResponse, str, dict]:
        """For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body., defaults to None
        :type request_body: ConnectorQueryConfig, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[ConnectorQueryResponse, str, dict]
        """

        Validator(ConnectorQueryConfig).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/Connector/query",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        return self._deserialize_or_raw(ConnectorQueryResponse, response, status, content)

    @cast_models
    def query_more_connector(
        self, request_body: str
    ) -> Union[ConnectorQueryResponse, str, dict]:
        """To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body.
        :type request_body: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[ConnectorQueryResponse, str, dict]
        """

        Validator(str).validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/Connector/queryMore",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body, "text/plain")
        )

        response, status, content = self.send_request(serialized_request)
        return self._deserialize_or_raw(ConnectorQueryResponse, response, status, content)
