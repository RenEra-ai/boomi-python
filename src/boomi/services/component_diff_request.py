
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..models import (
    ComponentDiffRequest,
    ComponentDiffRequestBulkRequest,
    ComponentDiffRequestBulkResponse,
    ComponentDiffResponseCreate,
)


class ComponentDiffRequestService(BaseService):

    @cast_models
    def create_component_diff_request(
        self, request_body: ComponentDiffRequest = None
    ) -> Union[ComponentDiffResponseCreate, str, dict]:
        """Contains a diff visualization option to help understand the differences between component versions. For more information, refer to the Postman article [Visualize request responses using Postman Visualizer](https://learning.postman.com/docs/sending-requests/response-data/visualizer/).

        :param request_body: The request body., defaults to None
        :type request_body: ComponentDiffRequest, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[ComponentDiffResponseCreate, str, dict]
        """

        Validator(ComponentDiffRequest).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/ComponentDiffRequest",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        return self._deserialize_or_raw(ComponentDiffResponseCreate, response, status, content)

    @cast_models
    def get_component_diff_request(
        self, component_id: str
    ) -> Union[ComponentDiffResponseCreate, str, dict]:
        """If you use Postman to make API calls, the GET response contains a diff visualization option to help understand the differences between component versions. For more information, refer to the Postman article [Visualize request responses using Postman Visualizer](https://learning.postman.com/docs/sending-requests/response-data/visualizer/). The Postman visualization feature currently supports only JSON responses.

        :param component_id: The ID of the component for which you want to compare versions.
        :type component_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[ComponentDiffResponseCreate, str, dict]
        """

        Validator(str).validate(component_id)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/ComponentDiffRequest/{{componentId}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("componentId", component_id)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        return self._deserialize_or_raw(ComponentDiffResponseCreate, response, status, content)

    @cast_models
    def bulk_component_diff_request(
        self, request_body: ComponentDiffRequestBulkRequest = None
    ) -> Union[ComponentDiffRequestBulkResponse, str, dict]:
        """To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

        :param request_body: The request body., defaults to None
        :type request_body: ComponentDiffRequestBulkRequest, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[ComponentDiffRequestBulkResponse, str, dict]
        """

        Validator(ComponentDiffRequestBulkRequest).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/ComponentDiffRequest/bulk",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        return self._deserialize_or_raw(ComponentDiffRequestBulkResponse, response, status, content)
