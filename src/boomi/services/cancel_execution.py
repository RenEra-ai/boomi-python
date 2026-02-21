
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models


class CancelExecutionService(BaseService):

    @cast_models
    def cancel_execution(self, execution_id: str) -> None:
        """Cancels the execution having the specified execution ID.

        :param execution_id: The execution ID to cancel.
        :type execution_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(str).validate(execution_id)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/cancelExecution/{{executionId}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("executionId", execution_id)
            .serialize()
            .set_method("POST")
        )

        self.send_request(serialized_request)
