
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.api_error import ApiError
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..net.transport.utils import parse_xml_to_dict
from ..models import ConnectorDocument, ConnectorDocumentDownload


class ConnectorDocumentService(BaseService):

    @cast_models
    def create_connector_document(
        self, request_body: ConnectorDocument = None
    ) -> Union[ConnectorDocumentDownload, str]:
        """The Connector Document operation allows you to download the raw, document data for a specific Generic Connector Record. This action submits the download request and the call returns a URL used to download the actual document data.

        :param request_body: The request body., defaults to None
        :type request_body: ConnectorDocument, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[ConnectorDocumentDownload, str]
        """

        Validator(ConnectorDocument).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/ConnectorDocument",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .add_header("Accept", "application/json")
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return ConnectorDocumentDownload._unmap(response)
        if content == "application/xml":
            return ConnectorDocumentDownload._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    def download_connector_document(
        self,
        request_body: ConnectorDocument = None,
        max_retries: int = 10,
        initial_delay: float = 2.0,
    ) -> bytes:
        """Request and download raw document data for a specific Generic Connector Record.

        Combines the two-phase download process: submits the download request via
        create_connector_document(), then polls the returned URL until the content is ready.

        :param request_body: The request body., defaults to None
        :type request_body: ConnectorDocument, optional
        :param max_retries: Maximum number of polling attempts., defaults to 10
        :type max_retries: int
        :param initial_delay: Initial delay in seconds between retries., defaults to 2.0
        :type initial_delay: float
        :return: The raw document content as bytes.
        :rtype: bytes
        """
        result = self.create_connector_document(request_body=request_body)
        if not hasattr(result, "url") or not result.url:
            raise ApiError("No download URL in response", 0, result)
        return self._poll_download_url(
            result.url, max_retries=max_retries, initial_delay=initial_delay
        )
