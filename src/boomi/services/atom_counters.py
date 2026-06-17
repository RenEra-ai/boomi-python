
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..models import AtomCounters


class AtomCountersService(BaseService):

    @cast_models
    def update_atom_counters(
        self, id_: str, request_body: AtomCounters = None
    ) -> Union[AtomCounters, str, dict]:
        """The UPDATE operation updates Runtime Counter values for a specific Runtime. Using the UPDATE operation overrides all settings set on the current counter. However, calling the UPDATE operation does not delete any existing counters that are not included in the `AtomCounters` object.

        :param request_body: The request body., defaults to None
        :type request_body: AtomCounters, optional
        :param id_: A unique ID assigned by the system to the Runtime.
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[AtomCounters, str, dict]
        """

        Validator(AtomCounters).is_optional().validate(request_body)
        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/AtomCounters/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        return self._deserialize_or_raw(AtomCounters, response, status, content)
