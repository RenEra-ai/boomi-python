
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..models import (
    AtomStartupProperties,
    AtomStartupPropertiesBulkRequest,
    AtomStartupPropertiesBulkResponse,
)


class AtomStartupPropertiesService(BaseService):

    @cast_models
    def get_atom_startup_properties(
        self, id_: str
    ) -> Union[AtomStartupProperties, str, dict]:
        """Retrieves the startup properties for the Runtime, Runtime cluster, or Runtime cloud with the specified ID.

        :param id_: A unique ID for the Runtime, Runtime cluster, or Runtime cloud. (This API is not applicable for runtimes attached to clouds)
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[AtomStartupProperties, str, dict]
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/AtomStartupProperties/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        return self._deserialize_or_raw(AtomStartupProperties, response, status, content)

    @cast_models
    def bulk_atom_startup_properties(
        self, request_body: AtomStartupPropertiesBulkRequest = None
    ) -> Union[AtomStartupPropertiesBulkResponse, str, dict]:
        """To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

        :param request_body: The request body., defaults to None
        :type request_body: AtomStartupPropertiesBulkRequest, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[AtomStartupPropertiesBulkResponse, str, dict]
        """

        Validator(AtomStartupPropertiesBulkRequest).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/AtomStartupProperties/bulk",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        return self._deserialize_or_raw(AtomStartupPropertiesBulkResponse, response, status, content)
