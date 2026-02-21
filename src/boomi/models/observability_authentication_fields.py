
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap(
    {
        "id_": "id",
        "type_": "type",
        "encrypted_value_set": "encryptedValueSet",
    }
)
class ObservabilityAuthenticationFields(BaseModel):
    """ObservabilityAuthenticationFields

    :param id_: id_
    :type id_: str
    :param type_: type_
    :type type_: str
    :param value: value
    :type value: str
    :param encrypted_value_set: encrypted_value_set, defaults to None
    :type encrypted_value_set: bool, optional
    """

    def __init__(
        self,
        id_: str,
        type_: str,
        value: str,
        encrypted_value_set: bool = SENTINEL,
        **kwargs,
    ):
        """ObservabilityAuthenticationFields

        :param id_: id_
        :type id_: str
        :param type_: type_
        :type type_: str
        :param value: value
        :type value: str
        :param encrypted_value_set: encrypted_value_set, defaults to None
        :type encrypted_value_set: bool, optional
        """
        self.id_ = id_
        self.type_ = type_
        self.value = value
        if encrypted_value_set is not SENTINEL:
            self.encrypted_value_set = encrypted_value_set
        self._kwargs = kwargs
