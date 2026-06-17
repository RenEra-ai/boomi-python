
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..models import (
    AccountSsoConfig,
    AccountSsoConfigBulkRequest,
    AccountSsoConfigBulkResponse,
)


class AccountSsoConfigService(BaseService):

    @cast_models
    def get_account_sso_config(self, id_: str) -> Union[AccountSsoConfig, str, dict]:
        """Returns the Account Single Sign-on Configuration for the supplied account ID.

        :param id_: id_
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[AccountSsoConfig, str, dict]
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/AccountSSOConfig/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        return self._deserialize_or_raw(AccountSsoConfig, response, status, content)

    @cast_models
    def update_account_sso_config(
        self, id_: str, request_body: AccountSsoConfig = None
    ) -> Union[AccountSsoConfig, str, dict]:
        """Updates the Account Single Sign-on Configuration for the supplied account ID.

        :param request_body: The request body., defaults to None
        :type request_body: AccountSsoConfig, optional
        :param id_: id_
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[AccountSsoConfig, str, dict]
        """

        Validator(AccountSsoConfig).is_optional().validate(request_body)
        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/AccountSSOConfig/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        return self._deserialize_or_raw(AccountSsoConfig, response, status, content)

    @cast_models
    def delete_account_sso_config(self, id_: str) -> None:
        """Deletes the Account Single Sign-on Configuration for the supplied account ID.

        :param id_: id_
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/AccountSSOConfig/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("DELETE")
        )

        response, status, _ = self.send_request(serialized_request)

    @cast_models
    def bulk_account_sso_config(
        self, request_body: AccountSsoConfigBulkRequest = None
    ) -> Union[AccountSsoConfigBulkResponse, str, dict]:
        """To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

        :param request_body: The request body., defaults to None
        :type request_body: AccountSsoConfigBulkRequest, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[AccountSsoConfigBulkResponse, str, dict]
        """

        Validator(AccountSsoConfigBulkRequest).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/AccountSSOConfig/bulk",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        return self._deserialize_or_raw(AccountSsoConfigBulkResponse, response, status, content)
