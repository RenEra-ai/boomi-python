
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..models import (
    EnvironmentExtensions,
    EnvironmentExtensionsBulkRequest,
    EnvironmentExtensionsBulkResponse,
    EnvironmentExtensionsQueryConfig,
    EnvironmentExtensionsQueryResponse,
)


class EnvironmentExtensionsService(BaseService):

    @cast_models
    def get_environment_extensions(self, id_: str) -> Union[EnvironmentExtensions, str, dict]:
        """Retrieves the extension values for the environment having the specified ID (except for encrypted values).

        :param id_: The ID of the object. This can be either of the following:
         1. The value of `environmentId`.
         2. A conceptual ID synthesized from the environment ID (`environmentId`) and the ID of the multi-install integration pack to which the extension values apply (`extensionGroupId`).
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[EnvironmentExtensions, str, dict]
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/EnvironmentExtensions/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        return self._deserialize_or_raw(EnvironmentExtensions, response, status, content)

    @cast_models
    def update_environment_extensions(
        self, id_: str, request_body: EnvironmentExtensions = None
    ) -> Union[EnvironmentExtensions, str, dict]:
        """Updates the extension values for the environment having the specified ID. When updating extension values, you must perform either a partial update to update only those extension values requiring modification in the request, or a full update to update the full set of environment extensions in a single request. A partial update is typically recommended because it results in smaller payloads and more targeted updates.

         >**Warning:** The UPDATE operation does not support running muliple map extensions requests concurrently. Some map extensions might not get updated properly.

         #### Performing a partial update

        To perform a **partial update**, set `partial` to true and then provide only the extension fields and values that you wish to update in the request.

        >**Note:** For cross reference tables, you can update a single cross reference table. However, you must provide all values for the entire table. You cannot update individual rows within a table.
        >
        > - For process property components, you can update a single process property component but you must provide the values for all properties in the component.

         #### Performing a full update

        To perform a **full update**, set `partial` to false and then provide all the environment extension fields and values in the request, regardless if you wish to change only some values but not all.

        >**Caution:** Values not included in the request are reset to use their default values. If you omit the partial attribute, the behavior defaults to a full update.

        :param request_body: The request body., defaults to None
        :type request_body: EnvironmentExtensions, optional
        :param id_: The ID of the object. This can be either of the following:
         1. The value of environmentId.
         2. A conceptual ID synthesized from the environment ID (environmentId) and the ID of the multi-install integration pack to which the extension values apply (extensionGroupId).
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[EnvironmentExtensions, str, dict]
        """

        Validator(EnvironmentExtensions).is_optional().validate(request_body)
        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/EnvironmentExtensions/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        return self._deserialize_or_raw(EnvironmentExtensions, response, status, content)

    @cast_models
    def bulk_environment_extensions(
        self, request_body: EnvironmentExtensionsBulkRequest = None
    ) -> Union[EnvironmentExtensionsBulkResponse, str, dict]:
        """To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

        :param request_body: The request body., defaults to None
        :type request_body: EnvironmentExtensionsBulkRequest, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[EnvironmentExtensionsBulkResponse, str, dict]
        """

        Validator(EnvironmentExtensionsBulkRequest).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/EnvironmentExtensions/bulk",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        return self._deserialize_or_raw(EnvironmentExtensionsBulkResponse, response, status, content)

    @cast_models
    def query_environment_extensions(
        self, request_body: EnvironmentExtensionsQueryConfig = None
    ) -> Union[EnvironmentExtensionsQueryResponse, str, dict]:
        """For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body., defaults to None
        :type request_body: EnvironmentExtensionsQueryConfig, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[EnvironmentExtensionsQueryResponse, str, dict]
        """

        Validator(EnvironmentExtensionsQueryConfig).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/EnvironmentExtensions/query",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        return self._deserialize_or_raw(EnvironmentExtensionsQueryResponse, response, status, content)

    @cast_models
    def query_more_environment_extensions(
        self, request_body: str
    ) -> Union[EnvironmentExtensionsQueryResponse, str, dict]:
        """To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body.
        :type request_body: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[EnvironmentExtensionsQueryResponse, str, dict]
        """

        Validator(str).validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/EnvironmentExtensions/queryMore",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body, "text/plain")
        )

        response, status, content = self.send_request(serialized_request)
        return self._deserialize_or_raw(EnvironmentExtensionsQueryResponse, response, status, content)
