
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..models import (
    GenericConnectorRecord,
    GenericConnectorRecordBulkRequest,
    GenericConnectorRecordBulkResponse,
    GenericConnectorRecordQueryConfig,
    GenericConnectorRecordQueryResponse,
)


class GenericConnectorRecordService(BaseService):

    @cast_models
    def get_generic_connector_record(
        self, id_: str
    ) -> Union[GenericConnectorRecord, str, dict]:
        """Allows you to view document metadata for exactly one document based on the provided id.

        :param id_: The ID of the GenericConnectorRecord. You obtain this ID from querying the GenericConnectorRecord object.
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[GenericConnectorRecord, str, dict]
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/GenericConnectorRecord/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        return self._deserialize_or_raw(GenericConnectorRecord, response, status, content)

    @cast_models
    def bulk_generic_connector_record(
        self, request_body: GenericConnectorRecordBulkRequest = None
    ) -> Union[GenericConnectorRecordBulkResponse, str, dict]:
        """To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

        :param request_body: The request body., defaults to None
        :type request_body: GenericConnectorRecordBulkRequest, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[GenericConnectorRecordBulkResponse, str, dict]
        """

        Validator(GenericConnectorRecordBulkRequest).is_optional().validate(
            request_body
        )

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/GenericConnectorRecord/bulk",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        return self._deserialize_or_raw(GenericConnectorRecordBulkResponse, response, status, content)

    @cast_models
    def query_generic_connector_record(
        self, request_body: GenericConnectorRecordQueryConfig = None
    ) -> Union[GenericConnectorRecordQueryResponse, str, dict]:
        """- The QUERY operation allows you to view document metadata for all documents in the run. You must query by exactly one `executionId`.
         - You cannot query `connectorFields`.

         For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body., defaults to None
        :type request_body: GenericConnectorRecordQueryConfig, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[GenericConnectorRecordQueryResponse, str, dict]
        """

        Validator(GenericConnectorRecordQueryConfig).is_optional().validate(
            request_body
        )

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/GenericConnectorRecord/query",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        return self._deserialize_or_raw(GenericConnectorRecordQueryResponse, response, status, content)

    @cast_models
    def query_more_generic_connector_record(
        self, request_body: str
    ) -> Union[GenericConnectorRecordQueryResponse, str, dict]:
        """To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body.
        :type request_body: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[GenericConnectorRecordQueryResponse, str, dict]
        """

        Validator(str).validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/GenericConnectorRecord/queryMore",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body, "text/plain")
        )

        response, status, content = self.send_request(serialized_request)
        return self._deserialize_or_raw(GenericConnectorRecordQueryResponse, response, status, content)
