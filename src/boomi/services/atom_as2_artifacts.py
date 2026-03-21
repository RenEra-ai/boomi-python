
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.api_error import ApiError
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..net.transport.utils import parse_xml_to_dict
from ..models import AtomAs2Artifacts, LogDownload


class AtomAs2ArtifactsService(BaseService):

    @cast_models
    def create_atom_as2_artifacts(
        self, request_body: AtomAs2Artifacts = None
    ) -> Union[LogDownload, str]:
        """You can use the Download AS2 Artifacts Log operation to request and download AS2 artifacts logs.

        :param request_body: The request body., defaults to None
        :type request_body: AtomAs2Artifacts, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[LogDownload, str]
        """

        Validator(AtomAs2Artifacts).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/AtomAS2Artifacts",
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

    def download_atom_as2_artifacts(
        self,
        request_body: AtomAs2Artifacts = None,
        max_retries: int = 10,
        initial_delay: float = 2.0,
    ) -> bytes:
        """Request and download AS2 artifacts logs.

        Combines the two-phase download process: submits the download request via
        create_atom_as2_artifacts(), then polls the returned URL until the content is ready.

        :param request_body: The request body., defaults to None
        :type request_body: AtomAs2Artifacts, optional
        :param max_retries: Maximum number of polling attempts., defaults to 10
        :type max_retries: int
        :param initial_delay: Initial delay in seconds between retries., defaults to 2.0
        :type initial_delay: float
        :return: The raw artifact content as bytes.
        :rtype: bytes
        """
        result = self.create_atom_as2_artifacts(request_body=request_body)
        if hasattr(result, "status_code") and str(result.status_code) == "504":
            raise ApiError("Runtime unavailable for artifact download", 504, result)
        if not hasattr(result, "url") or not result.url:
            raise ApiError("No download URL in response", 0, result)
        return self._poll_download_url(
            result.url, max_retries=max_retries, initial_delay=initial_delay
        )
