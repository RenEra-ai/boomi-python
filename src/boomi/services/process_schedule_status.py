
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..models import (
    ProcessScheduleStatus,
    ProcessScheduleStatusBulkRequest,
    ProcessScheduleStatusBulkResponse,
    ProcessScheduleStatusQueryConfig,
    ProcessScheduleStatusQueryResponse,
)


class ProcessScheduleStatusService(BaseService):

    @cast_models
    def get_process_schedule_status(
        self, id_: str
    ) -> Union[ProcessScheduleStatus, str, dict]:
        """Retrieves the Process Schedule Status object with a specified conceptual ID.

         The ordinary GET operation retrieves the Process Schedules object with a specific conceptual ID. The bulk GET operation retrieves the Process Schedules objects with specific conceptual IDs to a maximum of 100. In addition, you can obtain conceptual IDs from the QUERY operation.

        :param id_: The object’s conceptual ID, which is synthesized from the process and Runtime IDs.
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[ProcessScheduleStatus, str, dict]
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/ProcessScheduleStatus/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        return self._deserialize_or_raw(ProcessScheduleStatus, response, status, content)

    @cast_models
    def update_process_schedule_status(
        self, id_: str, request_body: ProcessScheduleStatus = None
    ) -> Union[ProcessScheduleStatus, str, dict]:
        """Stops or resumes process run schedules for a deployed process.

         The body of the request must specify not only the conceptual Process Schedule Status object ID but also the Runtime and process IDs. You can obtain the object ID from a QUERY operation.

         You must have the Runtime Management privilege and the Scheduling privilege to perform the UPDATE operation. If you have the Runtime Management Read Accessprivilege, you cannot update the status of process run schedules.

        :param request_body: The request body., defaults to None
        :type request_body: ProcessScheduleStatus, optional
        :param id_: id_
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[ProcessScheduleStatus, str, dict]
        """

        Validator(ProcessScheduleStatus).is_optional().validate(request_body)
        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/ProcessScheduleStatus/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        return self._deserialize_or_raw(ProcessScheduleStatus, response, status, content)

    @cast_models
    def bulk_process_schedule_status(
        self, request_body: ProcessScheduleStatusBulkRequest = None
    ) -> Union[ProcessScheduleStatusBulkResponse, str, dict]:
        """To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

        :param request_body: The request body., defaults to None
        :type request_body: ProcessScheduleStatusBulkRequest, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[ProcessScheduleStatusBulkResponse, str, dict]
        """

        Validator(ProcessScheduleStatusBulkRequest).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/ProcessScheduleStatus/bulk",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        return self._deserialize_or_raw(ProcessScheduleStatusBulkResponse, response, status, content)

    @cast_models
    def query_process_schedule_status(
        self, request_body: ProcessScheduleStatusQueryConfig = None
    ) -> Union[ProcessScheduleStatusQueryResponse, str, dict]:
        """For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body., defaults to None
        :type request_body: ProcessScheduleStatusQueryConfig, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[ProcessScheduleStatusQueryResponse, str, dict]
        """

        Validator(ProcessScheduleStatusQueryConfig).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/ProcessScheduleStatus/query",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        return self._deserialize_or_raw(ProcessScheduleStatusQueryResponse, response, status, content)

    @cast_models
    def query_more_process_schedule_status(
        self, request_body: str
    ) -> Union[ProcessScheduleStatusQueryResponse, str, dict]:
        """To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body.
        :type request_body: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[ProcessScheduleStatusQueryResponse, str, dict]
        """

        Validator(str).validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/ProcessScheduleStatus/queryMore",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body, "text/plain")
        )

        response, status, content = self.send_request(serialized_request)
        return self._deserialize_or_raw(ProcessScheduleStatusQueryResponse, response, status, content)
