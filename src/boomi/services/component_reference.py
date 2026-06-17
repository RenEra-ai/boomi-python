
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..models import (
    ComponentReference,
    ComponentReferenceBulkRequest,
    ComponentReferenceBulkResponse,
    ComponentReferenceQueryConfig,
    ComponentReferenceQueryResponse,
)


class ComponentReferenceService(BaseService):

    @cast_models
    def get_component_reference(
        self, component_id: str
    ) -> Union[ComponentReference, str, dict]:
        """Retrieves the component reference for a component ID.

         Send an HTTP GET to `https://api.boomi.com/api/rest/v1/{accountId}/ComponentReference/{componentId}`

        where `{accountId}` is the ID of the authenticating account for the request and `{componentId}` is the ID of the secondary component whose references you are attempting to GET.

        If you want to specify a branch, send an HTTP GET to `https://api.boomi.com/api/rest/v1/{accountId}/ComponentReference/{componentId}~{branchId}`

        where `{accountId}` is the ID of the authenticating account for the request and `{componentId}` is the ID of the secondary component whose references you are attempting to GET, and `{branchId}` is the branch on which you want to GET component references.

        :param component_id: The ID of the secondary component. The component ID is available in the **Revision History** dialog, which you can access from the **Build** page in the service.
        :type component_id: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[ComponentReference, str, dict]
        """

        Validator(str).validate(component_id)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/ComponentReference/{{componentId}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("componentId", component_id)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        return self._deserialize_or_raw(ComponentReference, response, status, content)

    @cast_models
    def bulk_component_reference(
        self, request_body: ComponentReferenceBulkRequest = None
    ) -> Union[ComponentReferenceBulkResponse, str, dict]:
        """To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

        :param request_body: The request body., defaults to None
        :type request_body: ComponentReferenceBulkRequest, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[ComponentReferenceBulkResponse, str, dict]
        """

        Validator(ComponentReferenceBulkRequest).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/ComponentReference/bulk",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        return self._deserialize_or_raw(ComponentReferenceBulkResponse, response, status, content)

    @cast_models
    def query_component_reference(
        self, request_body: ComponentReferenceQueryConfig = None
    ) -> Union[ComponentReferenceQueryResponse, str, dict]:
        """For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

        - You can use the QUERY operation to return the latest version(s) of a primary component(s) that references a given secondary component ID, or all the secondary components that the given primary component ID references.

        >**Note:** When querying either primary or secondary component references, the API object returns the immediate reference (one level). It does not recursively trace through nested references like the **Show Where Used** feature does in the user interface.

         For example, take a process that references a Map component where it references two Profile components. If you query by `parentComponentId=<process>`, the API returns a result for the Map component but not the profiles. To get the profiles, you need to perform a second call to query references for the Map component.

        - You can filter the query operation in one of two ways:

          - To find all the secondary components referenced by a given primary component, you must provide both the parentComponentId and the parentVersion values. You can optionally use the type filter in your query.

          - To find all the primary components that reference a given secondary component, you must provide the componentId value. You can optionally include the type filter in your query.

        - To see more information about a component ID returned in the response, like the component's type or name, you can query that same ID using the [Component Metadata object](/api/platformapi#tag/ComponentMetadata).

         #### Understanding references to deleted components

         Filtering or querying by `componentId` only returns the component's current version. If you delete the current component revision, it does not return results.

        When filtering by `parentComponentId` or `parentVersion`, it saves references to other components for a given version of the primary component. If you delete the given primary component version, it does not return results. Note that it is possible to return a reference to a deleted secondary component if you do not remove the reference in the user interface (appears in red).

        :param request_body: The request body., defaults to None
        :type request_body: ComponentReferenceQueryConfig, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[ComponentReferenceQueryResponse, str, dict]
        """

        Validator(ComponentReferenceQueryConfig).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/ComponentReference/query",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        return self._deserialize_or_raw(ComponentReferenceQueryResponse, response, status, content)

    @cast_models
    def query_more_component_reference(
        self, request_body: str
    ) -> Union[ComponentReferenceQueryResponse, str, dict]:
        """To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body.
        :type request_body: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[ComponentReferenceQueryResponse, str, dict]
        """

        Validator(str).validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/ComponentReference/queryMore",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body, "text/plain")
        )

        response, status, content = self.send_request(serialized_request)
        return self._deserialize_or_raw(ComponentReferenceQueryResponse, response, status, content)
