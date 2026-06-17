
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..models import RuntimeRestartRequest


class RuntimeRestartRequestService(BaseService):

    @cast_models
    def create_runtime_restart_request(
        self, request_body: RuntimeRestartRequest = None
    ) -> Union[RuntimeRestartRequest, str, dict]:
        """Restarts the runtime.

         - The client sends a runtime restart request to the platform API that specifies the runtimeId that you want to restart.
         - The platform returns the status code and message while the request is in progress. A successful response implies the restart request was submitted, not when the runtime restart is completed.

        :param request_body: The request body., defaults to None
        :type request_body: RuntimeRestartRequest, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[RuntimeRestartRequest, str, dict]
        """

        Validator(RuntimeRestartRequest).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/RuntimeRestartRequest",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        # Restart confirmations can come back as plain text; return those verbatim.
        if isinstance(response, str):
            return response
        return self._deserialize_or_raw(
            RuntimeRestartRequest, response, status, content
        )
