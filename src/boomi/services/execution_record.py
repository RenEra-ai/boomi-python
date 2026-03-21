
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.api_error import ApiError
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..net.transport.utils import parse_xml_to_dict
from ..models import ExecutionRecord, ExecutionRecordQueryConfig, ExecutionRecordQueryResponse


class ExecutionRecordService(BaseService):

    @cast_models
    def query_execution_record(
        self, request_body: ExecutionRecordQueryConfig = None
    ) -> Union[ExecutionRecordQueryResponse, str]:
        """For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body., defaults to None
        :type request_body: ExecutionRecordQueryConfig, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[ExecutionRecordQueryResponse, str]
        """

        Validator(ExecutionRecordQueryConfig).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/ExecutionRecord/query",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return ExecutionRecordQueryResponse._unmap(response)
        if content == "application/xml":
            return ExecutionRecordQueryResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def query_more_execution_record(
        self, request_body: str
    ) -> Union[ExecutionRecordQueryResponse, str]:
        """To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body.
        :type request_body: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[ExecutionRecordQueryResponse, str]
        """

        Validator(str).validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/ExecutionRecord/queryMore",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body, "text/plain")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return ExecutionRecordQueryResponse._unmap(response)
        if content == "application/xml":
            return ExecutionRecordQueryResponse._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def async_get_execution_record(self, id_: str) -> Union[ExecutionRecord, str]:
        """Retrieves the execution record asynchronously for the specified ID.

        Use the requestId returned by ExecutionRequest create to poll this endpoint.
        The API returns HTTP 202 while the execution is still processing, and HTTP 200
        with the ExecutionRecord payload once the result is available.

        The Boomi API wraps the response in an AsyncOperationResult envelope:
        ``{"@type": "AsyncOperationResult", "result": [...], "responseStatusCode": 200}``
        This method extracts the ExecutionRecord from that wrapper automatically.

        :param id_: The requestId from create_execution_request (format: executionrecord-<UUID>).
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed execution record, or None if still processing (HTTP 202).
        :rtype: Union[ExecutionRecord, str, None]
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/ExecutionRecord/async/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)

        data = response
        if content == "application/xml":
            data = parse_xml_to_dict(response)

        # Handle AsyncOperationResult wrapper returned by the Boomi API.
        # The async GET endpoint wraps ExecutionRecord in:
        # {"@type": "AsyncOperationResult", "result": [...], "responseStatusCode": N}
        if isinstance(data, dict):
            if data.get("@type") == "AsyncOperationResult" or "responseStatusCode" in data:
                inner_status = data.get("responseStatusCode", status)
                result_list = data.get("result")
                try:
                    numeric_status = int(inner_status)
                except (TypeError, ValueError):
                    raise ApiError(
                        f"Async operation returned unexpected status: {inner_status!r}",
                        status,
                        data,
                    )
                if numeric_status == 202:
                    return None
                if numeric_status >= 400:
                    raise ApiError(
                        f"Async operation failed with status {numeric_status}",
                        numeric_status,
                        data,
                    )
                if not result_list:
                    return None
                if isinstance(result_list, list) and len(result_list) > 0:
                    data = result_list[0]
                elif isinstance(result_list, dict):
                    data = result_list

        if data is None:
            return None

        return ExecutionRecord._unmap(data)

    def get_execution_record(self, id_: str) -> Union[ExecutionRecord, str]:
        """Retrieves the execution record for the specified ID.

        Convenience wrapper for async_get_execution_record(). Note: this calls
        the Boomi async API endpoint (GET /ExecutionRecord/async/{id}).

        :param id_: The execution record ID.
        :type id_: str
        :return: The parsed response data.
        :rtype: Union[ExecutionRecord, str]
        """
        return self.async_get_execution_record(id_)
