
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.api_error import ApiError
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..net.transport.utils import parse_xml_to_dict
from ..models import ExecutionArtifacts, LogDownload


class ExecutionArtifactsService(BaseService):

    @cast_models
    def create_execution_artifacts(
        self, request_body: ExecutionArtifacts = None
    ) -> Union[LogDownload, str]:
        """Allows you to retrieve a link for downloading detailed information about a given process run.
         - You must have the Runtime Management privilege to perform the CREATE operation. If you have the Runtime Management Read Access privilege, you cannot download execution artifacts.
         - Additionally, as the Cloud owner, you must select the **Enable Download of Execution Artifacts and Worker Logs** property for your account. This property permits you to download process execution data, and you can access it from the Cloud Attachment Quota tab of Manage > Cloud Management.
         - After providing the endpoint and a request body containing the execution ID, the CREATE response returns a download URL that you can open (or copy and paste) in your web browser, which initiates the file download to your local drive.
         To retrieve the download link for file containing a process execution artifacts,
         1. First create a CREATE (or POST) request to `https://api.boomi.com/api/rest/v1/<accountId>/ExecutionArtifacts` where `accountId` is the ID of the account authenticating the request.
         2. Populate the request body with the `executionId`, which is the identifier of the given run process.
         3. Send the request and either open or copy and paste the URL from the response into your web browser.

        :param request_body: The request body., defaults to None
        :type request_body: ExecutionArtifacts, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[LogDownload, str]
        """

        Validator(ExecutionArtifacts).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/ExecutionArtifacts",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        if content == "application/json":
            return LogDownload._unmap(response)
        if content == "application/xml":
            return LogDownload._unmap(parse_xml_to_dict(response))
        raise ApiError("Error on deserializing the response.", status, response)

    def download_execution_artifacts(
        self,
        request_body: ExecutionArtifacts = None,
        max_retries: int = 10,
        initial_delay: float = 2.0,
    ) -> bytes:
        """Request and download execution artifacts.

        Combines the two-phase download process: submits the download request via
        create_execution_artifacts(), then polls the returned URL until the content is ready.

        :param request_body: The request body., defaults to None
        :type request_body: ExecutionArtifacts, optional
        :param max_retries: Maximum number of polling attempts., defaults to 10
        :type max_retries: int
        :param initial_delay: Initial delay in seconds between retries., defaults to 2.0
        :type initial_delay: float
        :return: The raw artifact content as bytes (typically a ZIP file).
        :rtype: bytes
        """
        result = self.create_execution_artifacts(request_body=request_body)
        if hasattr(result, "status_code") and str(result.status_code) == "504":
            raise ApiError("Runtime unavailable for artifact download", 504, result)
        if not hasattr(result, "url") or not result.url:
            raise ApiError("No download URL in response", 0, result)
        return self._poll_download_url(
            result.url, max_retries=max_retries, initial_delay=initial_delay
        )
