
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..models import (
    AccountCloudAttachmentSummary,
    AccountCloudAttachmentSummaryBulkRequest,
    AccountCloudAttachmentSummaryBulkResponse,
    AccountCloudAttachmentSummaryQueryConfig,
    AccountCloudAttachmentSummaryQueryResponse,
)


class AccountCloudAttachmentSummaryService(BaseService):
    """Service for AccountCloudAttachmentSummary endpoints.

    .. note::
        The Cloud Management feature must be enabled for your Boomi account.
        Without it, all AccountCloudAttachmentSummary endpoints return HTTP 400
        with the message "The Cloud Management feature is not enabled for your
        account."  This response does not indicate a malformed SDK request.
    """

    @cast_models
    def get_account_cloud_attachment_summary(
        self, id_: str
    ) -> Union[AccountCloudAttachmentSummary, str, dict]:
        """Retrieves the properties of the AccountCloudAttachmentSummary having the specified ID.

        :param id_: A unique ID assigned by the system.
        :type id_: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[AccountCloudAttachmentSummary, str, dict]
        """

        Validator(str).validate(id_)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/AccountCloudAttachmentSummary/{{id}}",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_path("id", id_)
            .serialize()
            .set_method("GET")
        )

        response, status, content = self.send_request(serialized_request)
        return self._deserialize_or_raw(AccountCloudAttachmentSummary, response, status, content)

    @cast_models
    def bulk_account_cloud_attachment_summary(
        self, request_body: AccountCloudAttachmentSummaryBulkRequest = None
    ) -> Union[AccountCloudAttachmentSummaryBulkResponse, str, dict]:
        """To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

        :param request_body: The request body., defaults to None
        :type request_body: AccountCloudAttachmentSummaryBulkRequest, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[AccountCloudAttachmentSummaryBulkResponse, str, dict]
        """

        Validator(AccountCloudAttachmentSummaryBulkRequest).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/AccountCloudAttachmentSummary/bulk",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        return self._deserialize_or_raw(AccountCloudAttachmentSummaryBulkResponse, response, status, content)

    @cast_models
    def query_account_cloud_attachment_summary(
        self, request_body: AccountCloudAttachmentSummaryQueryConfig = None
    ) -> Union[AccountCloudAttachmentSummaryQueryResponse, str, dict]:
        """For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body., defaults to None
        :type request_body: AccountCloudAttachmentSummaryQueryConfig, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[AccountCloudAttachmentSummaryQueryResponse, str, dict]
        """

        Validator(AccountCloudAttachmentSummaryQueryConfig).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/AccountCloudAttachmentSummary/query",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        return self._deserialize_or_raw(AccountCloudAttachmentSummaryQueryResponse, response, status, content)

    @cast_models
    def query_more_account_cloud_attachment_summary(
        self, request_body: str
    ) -> Union[AccountCloudAttachmentSummaryQueryResponse, str, dict]:
        """To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body.
        :type request_body: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[AccountCloudAttachmentSummaryQueryResponse, str, dict]
        """

        Validator(str).validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/AccountCloudAttachmentSummary/queryMore",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body, "text/plain")
        )

        response, status, content = self.send_request(serialized_request)
        return self._deserialize_or_raw(AccountCloudAttachmentSummaryQueryResponse, response, status, content)
