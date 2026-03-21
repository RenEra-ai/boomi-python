
from enum import Enum
from .sentinel import was_value_set

# Mapping SDK class names to Boomi API @type names
# Needed for polymorphic types where SDK uses different casing than API
TYPE_NAME_MAPPING = {
    # MLLP Protocol
    'MllpCommunicationOptions': 'MLLPCommunicationOptions',
    'MllpSendSettings': 'MLLPSendSettings',
    'MllpsslOptions': 'MLLPSSLOptions',
    # HL7 Standard
    'Hl7PartnerInfo': 'HL7PartnerInfo',
    'Hl7Options': 'HL7Options',
    # FTP/SFTP Protocol
    'FtpCommunicationOptions': 'FTPCommunicationOptions',
    'FtpSendSettings': 'FTPSendSettings',
    'FtpsslOptions': 'FTPSSLOptions',
    'SftpCommunicationOptions': 'SFTPCommunicationOptions',
    'SftpSendSettings': 'SFTPSendSettings',
    'SftpsshOptions': 'SFTPSSHOptions',
    'SftpProxySettings': 'SFTPProxySettings',
    # HTTP Protocol
    'HttpCommunicationOptions': 'HTTPCommunicationOptions',
    'HttpSendSettings': 'HTTPSendSettings',
    'HttpsslOptions': 'HTTPSSLOptions',
    'HttpoAuthSettings': 'HTTPOAuthSettings',
    'HttpoAuth2Settings': 'HTTPOAuth2Settings',
    # AS2 Protocol
    'As2CommunicationOptions': 'AS2CommunicationOptions',
    'As2SendSettings': 'AS2SendSettings',
    'As2SendOptions': 'AS2SendOptions',
    'As2SslOptions': 'AS2SSLOptions',
    'As2PartnerInfo': 'AS2PartnerInfo',
    'As2MdnOptions': 'AS2MDNOptions',
    'As2MessageOptions': 'AS2MessageOptions',
    # OFTP Protocol
    'OftpCommunicationOptions': 'OFTPCommunicationOptions',
    'OftpSendSettings': 'OFTPSendSettings',
    'OftpPartnerInfo': 'OFTPPartnerInfo',
    # X12 Standard
    'X12PartnerInfo': 'X12PartnerInfo',
    'X12Options': 'X12Options',
    # EDIFACT Standard
    'EdifactPartnerInfo': 'EDIFACTPartnerInfo',
    'EdifactOptions': 'EDIFACTOptions',
}


class JsonMap:
    """
    A class decorator used to map adjusted attribute names to original JSON attribute names before a request,
    and vice versa after the request.

    Example:
    @JsonMapping({
        'adjusted_name': 'original_name',
        'adjusted_list': 'original_list'
    })
    class SomeClass(BaseModel):
        adjusted_name: str
        adjusted_list: List[OtherClass]

    :param mapping: A dictionary specifying the mapping between adjusted attribute names and original JSON attribute names.
    :type mapping: dict
    """

    def __init__(self, mapping):
        self.mapping = mapping

    def __call__(self, cls):
        """
        Transform the decorated class with attribute mapping capabilities.

        :param cls: The class to be decorated.
        :type cls: type
        :return: The decorated class.
        :rtype: type
        """
        cls.__json_mapping = self.mapping

        def _map(self):
            """
            Convert the object's attributes to a dictionary with mapped attribute names.

            :return: A dictionary with mapped attribute names and values.
            :rtype: dict
            """
            map = self.__json_mapping
            attribute_dict = vars(self)
            result_dict = {}

            # Add @type field for Boomi API polymorphic type support
            # This is required for nested objects in TradingPartnerComponent
            # Use mapping to convert SDK class names to API type names
            class_name = self.__class__.__name__
            result_dict['@type'] = TYPE_NAME_MAPPING.get(class_name, class_name)

            for key, value in attribute_dict.items():
                if key.startswith("_") or not was_value_set(value):
                    continue

                # Skip None values - Boomi API doesn't accept nulls
                if value is None:
                    continue

                if isinstance(value, list):
                    value = [v._map() if hasattr(v, "_map") else v for v in value]
                elif isinstance(value, Enum):
                    value = value.value
                elif hasattr(value, "_map"):
                    value = value._map()
                elif isinstance(value, bool):
                    # Keep as native bool (JSON serializer handles it)
                    pass
                elif isinstance(value, str) and value.lower() in ('true', 'false'):
                    # Convert string booleans to native bool
                    value = value.lower() == 'true'

                mapped_key = map.get(key, key)
                result_dict[mapped_key] = value

            return result_dict

        @classmethod
        def _unmap(cls, mapped_data):
            """
            Create an object instance from a dictionary with mapped attribute names.

            :param mapped_data: A dictionary with mapped attribute names and values.
            :type mapped_data: dict
            :return: An instance of the class with attribute values assigned from the dictionary.
            :rtype: cls
            """
            reversed_map = {v: k for k, v in cls.__json_mapping.items()}
            mapped_attributes = {}

            for key, value in mapped_data.items():
                # Handle Boomi typed-array format: ['BigInteger', 2575] -> 2575, ['Long', 3496] -> 3496
                # Only unwrap known Java type wrappers, not arbitrary [str, value] lists
                _JAVA_TYPE_NAMES = {
                    'BigInteger', 'BigDecimal', 'Long', 'Integer', 'Short', 'Byte',
                    'Float', 'Double', 'Boolean', 'String', 'Character',
                }
                if (isinstance(value, list) and len(value) == 2
                        and isinstance(value[0], str) and value[0] in _JAVA_TYPE_NAMES):
                    value = value[1]
                mapped_key = reversed_map.get(key, key)
                mapped_attributes[mapped_key] = value

            return cls(**mapped_attributes)

        # Only set _map if the class doesn't have its own custom implementation
        # This allows classes to override with their own serialization logic
        # Use __dict__ to check if the class itself (not parent) defines _map
        if '_map' not in cls.__dict__:
            cls._map = _map
        cls._unmap = _unmap

        return cls
