
from typing import Union
from .utils.validator import Validator
from .utils.base_service import BaseService
from ..net.transport.serializer import Serializer
from ..net.transport.api_error import ApiError
from ..net.environment.environment import Environment
from ..models.utils.cast_models import cast_models
from ..models import Hl7ConnectorRecordQueryConfig, Hl7ConnectorRecordQueryResponse


class Hl7ConnectorRecordService(BaseService):

    @cast_models
    def query_hl7_connector_record(
        self, request_body: Hl7ConnectorRecordQueryConfig = None
    ) -> Union[Hl7ConnectorRecordQueryResponse, str, dict]:
        """To filter by a customField, use the format `customFields.fieldName` as the filter property where `fieldName` is the element name of the custom field in the HL7 Connector Record structure. To get a list of the available custom fields, refer to [CustomTrackedField object](#tag/CustomTrackedField).

         The STARTS_WITH operator accepts values that do not include spaces.

         For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body., defaults to None
        :type request_body: Hl7ConnectorRecordQueryConfig, optional
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[Hl7ConnectorRecordQueryResponse, str]
        """

        Validator(Hl7ConnectorRecordQueryConfig).is_optional().validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/HL7ConnectorRecord/query",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body)
        )

        response, status, content = self.send_request(serialized_request)
        return self._deserialize_or_raw(Hl7ConnectorRecordQueryResponse, response, status, content)

    @cast_models
    def query_more_hl7_connector_record(
        self, request_body: str
    ) -> Union[Hl7ConnectorRecordQueryResponse, str, dict]:
        """To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

        :param request_body: The request body.
        :type request_body: str
        ...
        :raises RequestError: Raised when a request fails, with optional HTTP status code and details.
        ...
        :return: The parsed response data.
        :rtype: Union[Hl7ConnectorRecordQueryResponse, str]
        """

        Validator(str).validate(request_body)

        serialized_request = (
            Serializer(
                f"{self.base_url or Environment.DEFAULT.url}/HL7ConnectorRecord/queryMore",
                [self.get_access_token(), self.get_basic_auth()],
            )
            .serialize()
            .set_method("POST")
            .set_body(request_body, "text/plain")
        )

        response, status, content = self.send_request(serialized_request)
        return self._deserialize_or_raw(Hl7ConnectorRecordQueryResponse, response, status, content)
