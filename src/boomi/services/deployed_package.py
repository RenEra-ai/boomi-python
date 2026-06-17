
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..models import (
    DeployedPackage,
    DeployedPackageBulkRequest,
    DeployedPackageBulkResponse,
    DeployedPackageQueryConfig,
    DeployedPackageQueryResponse,
)


class DeployedPackageService(BaseService):

    @cast_models
    def create_deployed_package(
        self, request_body: DeployedPackage = None
    ) -> Union[DeployedPackage, str, dict]:
        """You can use the CREATE operation in two ways:
         - With `environmentId` and `packageId`, CREATE deploys the specified packaged component to the identified environment.
         - With `environmentId` and `componentId`, CREATE packages with the specified component and deploys the package to the specified environment.
         >**Note:** By default, deployment of listener processes are in a running state. To deploy a packaged listener process in a paused state, include the `listenerStatus` field with a value of `PAUSED`.

        :param request_body: The request body., defaults to None
        :type request_body: DeployedPackage, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[DeployedPackage, str, dict]
        """

        Validator(DeployedPackage).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/DeployedPackage",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        return self._deserialize_or_raw(DeployedPackage, response, status, content)

    @cast_models
    def get_deployed_package(self, id_: str) -> Union[DeployedPackage, str, dict]:
        """Returns a single Deployed Package object based on the deployment ID.

        :param id_: The Deployed Package object you are attempting to DELETE.
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[DeployedPackage, str, dict]
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/DeployedPackage/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        return self._deserialize_or_raw(DeployedPackage, response, status, content)

    @cast_models
    def delete_deployed_package(self, id_: str) -> None:
        """Removes the packaged component from the environment each with a specific IDs.

        :param id_: id_
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/DeployedPackage/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("DELETE")
        )

        response, status, _ = self.send_request(serialized_request)

    @cast_models
    def bulk_deployed_package(
        self, request_body: DeployedPackageBulkRequest = None
    ) -> Union[DeployedPackageBulkResponse, str, dict]:
        """To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

        :param request_body: The request body., defaults to None
        :type request_body: DeployedPackageBulkRequest, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[DeployedPackageBulkResponse, str, dict]
        """

        Validator(DeployedPackageBulkRequest).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/DeployedPackage/bulk",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        return self._deserialize_or_raw(DeployedPackageBulkResponse, response, status, content)

    @cast_models
    def query_deployed_package(
        self, request_body: DeployedPackageQueryConfig = None
    ) -> Union[DeployedPackageQueryResponse, str, dict]:
        """For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body., defaults to None
        :type request_body: DeployedPackageQueryConfig, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[DeployedPackageQueryResponse, str, dict]
        """

        Validator(DeployedPackageQueryConfig).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/DeployedPackage/query",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        return self._deserialize_or_raw(DeployedPackageQueryResponse, response, status, content)

    @cast_models
    def query_more_deployed_package(
        self, request_body: str
    ) -> Union[DeployedPackageQueryResponse, str, dict]:
        """To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body.
        :type request_body: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[DeployedPackageQueryResponse, str, dict]
        """

        Validator(str).validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/DeployedPackage/queryMore",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body, "text/plain")
        )

        response, status, content = self.send_request(serialized_request)
        return self._deserialize_or_raw(DeployedPackageQueryResponse, response, status, content)
