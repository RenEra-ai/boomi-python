
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .custom_fields import CustomFields


@JsonMap(
    {
        "account": "account",
        "action_type": "actionType",
        "atom_id": "atomId",
        "connector_name": "connectorName",
        "connector_type": "connectorType",
        "custom_fields": "customFields",
        "date_processed": "dateProcessed",
        "document_index": "documentIndex",
        "error_message": "errorMessage",
        "execution_id": "executionId",
        "from_trading_partner": "fromTradingPartner",
        "id_": "id",
        "operation_name": "operationName",
        "size": "size",
        "successful": "successful",
        "to_trading_partner": "toTradingPartner",
        "custom_standard_id": "customStandardID",
        "custom_standard_name": "customStandardName",
        "message_date": "messageDate",
        "message_id": "messageID",
        "message_time": "messageTime",
        "message_type": "messageType",
        "receiver_id": "receiverID",
        "receiver_id_qualifier": "receiverIDQualifier",
        "sender_id": "senderID",
        "sender_id_qualifier": "senderIDQualifier",
        "standard_id": "standardID",
    }
)
class EdiCustomConnectorRecord(BaseModel):
    """EdiCustomConnectorRecord

    :param account: The ID of the account that ran this record.
    :type account: str
    :param action_type: The type of action with which this record corresponds — *Send* for an outbound interchange, *Get* for an inbound interchange using the Disk, FTP, or SFTP communication method, or *Listen* for an inbound interchange using the AS2 or HTTP communication method.
    :type action_type: str
    :param atom_id: The ID of the Runtime that processed this record.
    :type atom_id: str
    :param connector_name: The value is *Trading Partner* for a Custom trading partner Send operation, or *Start* for a Custom trading partner Listen operation.
    :type connector_name: str
    :param connector_type: *edicustom* is the connector type for any record.
    :type connector_type: str
    :param custom_fields: custom_fields
    :type custom_fields: CustomFields
    :param date_processed: The processing date and time of this record. Format is yyyy-MM-dd'T'HH:mm:ss'Z' \(for example, 2019-09-14T15:32:00Z\).
    :type date_processed: str
    :param document_index: The numerical index of this record in the execution., defaults to None
    :type document_index: int, optional
    :param error_message: Any error message associated with this record. This field is omitted for a successful interchange.
    :type error_message: str
    :param execution_id: The ID of the run.
    :type execution_id: str
    :param from_trading_partner: The name of the sending trading partner component., defaults to None
    :type from_trading_partner: str, optional
    :param id_: The ID of this record.
    :type id_: str
    :param operation_name: The name of the operation component that processed the record.
    :type operation_name: str
    :param size: The size, in bytes, of the document that corresponds to this record., defaults to None
    :type size: int, optional
    :param successful: Whether the record is a success or error., defaults to None
    :type successful: bool, optional
    :param to_trading_partner: The name of the receiving trading partner component., defaults to None
    :type to_trading_partner: str, optional
    :param custom_standard_id: custom_standard_id, defaults to None
    :type custom_standard_id: str, optional
    :param custom_standard_name: custom_standard_name, defaults to None
    :type custom_standard_name: str, optional
    :param message_date: message_date, defaults to None
    :type message_date: str, optional
    :param message_id: message_id, defaults to None
    :type message_id: str, optional
    :param message_time: message_time, defaults to None
    :type message_time: str, optional
    :param message_type: message_type, defaults to None
    :type message_type: str, optional
    :param receiver_id: receiver_id, defaults to None
    :type receiver_id: str, optional
    :param receiver_id_qualifier: receiver_id_qualifier, defaults to None
    :type receiver_id_qualifier: str, optional
    :param sender_id: sender_id, defaults to None
    :type sender_id: str, optional
    :param sender_id_qualifier: sender_id_qualifier, defaults to None
    :type sender_id_qualifier: str, optional
    :param standard_id: standard_id, defaults to None
    :type standard_id: str, optional
    :param version: version, defaults to None
    :type version: str, optional
    """

    def __init__(
        self,
        account: str,
        action_type: str,
        atom_id: str,
        connector_name: str,
        connector_type: str,
        custom_fields: CustomFields,
        date_processed: str,
        error_message: str,
        execution_id: str,
        id_: str,
        operation_name: str,
        document_index: int = SENTINEL,
        from_trading_partner: str = SENTINEL,
        size: int = SENTINEL,
        successful: bool = SENTINEL,
        to_trading_partner: str = SENTINEL,
        custom_standard_id: str = SENTINEL,
        custom_standard_name: str = SENTINEL,
        message_date: str = SENTINEL,
        message_id: str = SENTINEL,
        message_time: str = SENTINEL,
        message_type: str = SENTINEL,
        receiver_id: str = SENTINEL,
        receiver_id_qualifier: str = SENTINEL,
        sender_id: str = SENTINEL,
        sender_id_qualifier: str = SENTINEL,
        standard_id: str = SENTINEL,
        version: str = SENTINEL,
        **kwargs,
    ):
        """EdiCustomConnectorRecord

        :param account: The ID of the account that ran this record.
        :type account: str
        :param action_type: The type of action with which this record corresponds — *Send* for an outbound interchange, *Get* for an inbound interchange using the Disk, FTP, or SFTP communication method, or *Listen* for an inbound interchange using the AS2 or HTTP communication method.
        :type action_type: str
        :param atom_id: The ID of the Runtime that processed this record.
        :type atom_id: str
        :param connector_name: The value is *Trading Partner* for a Custom trading partner Send operation, or *Start* for a Custom trading partner Listen operation.
        :type connector_name: str
        :param connector_type: *edicustom* is the connector type for any record.
        :type connector_type: str
        :param custom_fields: custom_fields
        :type custom_fields: CustomFields
        :param date_processed: The processing date and time of this record. Format is yyyy-MM-dd'T'HH:mm:ss'Z' \(for example, 2019-09-14T15:32:00Z\).
        :type date_processed: str
        :param document_index: The numerical index of this record in the execution., defaults to None
        :type document_index: int, optional
        :param error_message: Any error message associated with this record. This field is omitted for a successful interchange.
        :type error_message: str
        :param execution_id: The ID of the run.
        :type execution_id: str
        :param from_trading_partner: The name of the sending trading partner component., defaults to None
        :type from_trading_partner: str, optional
        :param id_: The ID of this record.
        :type id_: str
        :param operation_name: The name of the operation component that processed the record.
        :type operation_name: str
        :param size: The size, in bytes, of the document that corresponds to this record., defaults to None
        :type size: int, optional
        :param successful: Whether the record is a success or error., defaults to None
        :type successful: bool, optional
        :param to_trading_partner: The name of the receiving trading partner component., defaults to None
        :type to_trading_partner: str, optional
        :param custom_standard_id: custom_standard_id, defaults to None
        :type custom_standard_id: str, optional
        :param custom_standard_name: custom_standard_name, defaults to None
        :type custom_standard_name: str, optional
        :param message_date: message_date, defaults to None
        :type message_date: str, optional
        :param message_id: message_id, defaults to None
        :type message_id: str, optional
        :param message_time: message_time, defaults to None
        :type message_time: str, optional
        :param message_type: message_type, defaults to None
        :type message_type: str, optional
        :param receiver_id: receiver_id, defaults to None
        :type receiver_id: str, optional
        :param receiver_id_qualifier: receiver_id_qualifier, defaults to None
        :type receiver_id_qualifier: str, optional
        :param sender_id: sender_id, defaults to None
        :type sender_id: str, optional
        :param sender_id_qualifier: sender_id_qualifier, defaults to None
        :type sender_id_qualifier: str, optional
        :param standard_id: standard_id, defaults to None
        :type standard_id: str, optional
        :param version: version, defaults to None
        :type version: str, optional
        """
        self.account = account
        self.action_type = action_type
        self.atom_id = atom_id
        self.connector_name = connector_name
        self.connector_type = connector_type
        self.custom_fields = self._define_object(custom_fields, CustomFields)
        self.date_processed = date_processed
        if document_index is not SENTINEL:
            self.document_index = document_index
        self.error_message = error_message
        self.execution_id = execution_id
        if from_trading_partner is not SENTINEL:
            self.from_trading_partner = from_trading_partner
        self.id_ = id_
        self.operation_name = operation_name
        if size is not SENTINEL:
            self.size = size
        if successful is not SENTINEL:
            self.successful = successful
        if to_trading_partner is not SENTINEL:
            self.to_trading_partner = to_trading_partner
        if custom_standard_id is not SENTINEL:
            self.custom_standard_id = custom_standard_id
        if custom_standard_name is not SENTINEL:
            self.custom_standard_name = custom_standard_name
        if message_date is not SENTINEL:
            self.message_date = message_date
        if message_id is not SENTINEL:
            self.message_id = message_id
        if message_time is not SENTINEL:
            self.message_time = message_time
        if message_type is not SENTINEL:
            self.message_type = message_type
        if receiver_id is not SENTINEL:
            self.receiver_id = receiver_id
        if receiver_id_qualifier is not SENTINEL:
            self.receiver_id_qualifier = receiver_id_qualifier
        if sender_id is not SENTINEL:
            self.sender_id = sender_id
        if sender_id_qualifier is not SENTINEL:
            self.sender_id_qualifier = sender_id_qualifier
        if standard_id is not SENTINEL:
            self.standard_id = standard_id
        if version is not SENTINEL:
            self.version = version
        self._kwargs = kwargs
