
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..models import ExecutionRequest


class ExecutionRequestService(BaseService):

    @cast_models
    def create_execution_request(
        self, request_body: ExecutionRequest = None
    ) -> Union[ExecutionRequest, str, dict]:
        """Submits the process to run and returns results immediately. The operation does not wait for the run to complete.

         - The Execution Request response returns a requestID, which you use to make a subsequent call to the [Execution Record object](/api/platformapi#tag/ExecutionRecord) to retrieve detailed information about the process run.
        - This operation returns an error when the client:
          -  Fails authentication or does not have the correct permissions
          -  Supplies an invalid Account ID
          -  Supplies an invalid Runtime ID
          -  Attempts to reach a deleted Atom
          -  Supplies an invalid Process ID
          -  Missing privileges to run processes on the given Runtime or its associated Environment.

        :param request_body: The request body., defaults to None
        :type request_body: ExecutionRequest, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[ExecutionRequest, str, dict]
        """

        Validator(ExecutionRequest).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/ExecutionRequest",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        return self._deserialize_or_raw(ExecutionRequest, response, status, content)
