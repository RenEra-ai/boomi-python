import copy
from typing import Union

from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.api_error import ApiError
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..net.transport.utils import parse_xml_to_dict
from ..models import (
    AccountCloudAttachmentProperties,
    AccountCloudAttachmentPropertiesAsyncResponse,
    AsyncOperationTokenResult,
)


class AccountCloudAttachmentPropertiesService(BaseService):

    def __init__(self, base_url: str = None):
        super().__init__(base_url)
        self._token_to_container = {}

    @cast_models
    def update_account_cloud_attachment_properties(
        self,
        id_: str,
        request_body: AccountCloudAttachmentProperties,
    ) -> Union[AccountCloudAttachmentProperties, str]:
        """Modifies one or more Account Cloud attachment properties.

         - To update property values, include all property names that you want to modify including their new values in the request body you do not need to provide the full list of properties in the request. This action is equivalent to editing property values on the [Attachment quotas tab](https://help.boomi.com/docs/Atomsphere/Integration/Integration%20management/r-atm-Attachment_Quotas_tab_4fbc3fff-7aaf-4bbd-a2dc-25d0edb5189c) (Manage > Cloud Management) in the user interface.

         - To ensure a successful request, you must provide valid property names and their accepted values in the request body. Otherwise, it returns an error.

         - The response returns a status code of 200 indicating a successful request. To verify updates made to a property, you can make a new GET request or view the Cloud attachment quotas tab (Manage > Cloud Management) in the user interface.

         - To modify properties, you must be the owner of the private Runtime cloud, and both the Runtime cloud and its attachments must be online.

        :param request_body: The request body. Must include container_id.
        :type request_body: AccountCloudAttachmentProperties
        :param id_: id_
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[AccountCloudAttachmentProperties, str]
        """

        Validator(AccountCloudAttachmentProperties).validate(request_body)
        Validator(str).validate(id_)

        body = request_body
        if not getattr(request_body, "container_id", None):
            body = copy.copy(request_body)
            body.container_id = id_

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/AccountCloudAttachmentProperties/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("POST")
            .set_body(body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return AccountCloudAttachmentProperties._unmap(response)
        if content == "application/xml":
            return AccountCloudAttachmentProperties._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    @cast_models
    def async_get_account_cloud_attachment_properties(
        self, id_: str
    ) -> Union[AsyncOperationTokenResult, str]:
        """Use the GET operation to return and view a full list of Account Cloud attachment properties and their current values. This action is equivalent to viewing the [Attachment quotas](https://help.boomi.com/docs/Atomsphere/Integration/Integration%20management/r-atm-Attachment_Quotas_tab_4fbc3fff-7aaf-4bbd-a2dc-25d0edb5189c) tab (Manage > Cloud Management) in the user interface.
         >**Note:** The Cloud and attachments to which you are calling must be online. Cloud owners and users that own the Cloud attachments can use this operation.

        :param id_: id_
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[AsyncOperationTokenResult, str]
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/async/AccountCloudAttachmentProperties/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            result = AsyncOperationTokenResult._unmap(response)
        elif content == "application/xml":
            result = AsyncOperationTokenResult._unmap(parse_xml_to_dict(response))
        else:
            raise ApiError("Error on deserializing the response.", status, response)

        if hasattr(result, "async_token") and hasattr(result.async_token, "token"):
            self._token_to_container[result.async_token.token] = id_
        return result

    @cast_models
    def async_token_account_cloud_attachment_properties(
        self, token: str
    ) -> Union[AccountCloudAttachmentPropertiesAsyncResponse, str]:
        """Send a second GET request with the token returned in the first GET request. The object returns a list of existing property names and values for the given account and Cloud.
         >**Note:** The Cloud and attachments to which you are calling must be online. Cloud owners and users that own the Cloud attachments can use this operation.

        :param token: Takes in the token from a previous call to return a result.
        :type token: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[AccountCloudAttachmentPropertiesAsyncResponse, str]
        """

        Validator(str).validate(token)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/async/AccountCloudAttachmentProperties/response/{{token}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("token", token)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            result = AccountCloudAttachmentPropertiesAsyncResponse._unmap(response)
        elif content == "application/xml":
            result = AccountCloudAttachmentPropertiesAsyncResponse._unmap(parse_xml_to_dict(response))
        else:
            raise ApiError("Error on deserializing the response.", status, response)

        container_id = self._token_to_container.get(token)
        response_status_code = getattr(result, "response_status_code", None)
        if container_id and hasattr(result, "result") and result.result:
            for item in result.result:
                if not getattr(item, "container_id", None):
                    item.container_id = container_id
        if container_id and response_status_code != 202:
            # Keep the mapping for intermediate 202 responses because some
            # endpoints return partial result objects before the completed 200.
            self._token_to_container.pop(token, None)
        return result
