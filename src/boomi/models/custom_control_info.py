
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap(
    {
        "message_id": "messageId",
        "message_id_qual": "messageIdQual",
    }
)
class CustomControlInfo(BaseModel):
    """CustomControlInfo

    :param message_id: message_id, defaults to None
    :type message_id: str, optional
    :param message_id_qual: message_id_qual, defaults to None
    :type message_id_qual: str, optional
    """

    def __init__(
        self,
        message_id: str = SENTINEL,
        message_id_qual: str = SENTINEL,
        **kwargs,
    ):
        """CustomControlInfo

        :param message_id: message_id, defaults to None
        :type message_id: str, optional
        :param message_id_qual: message_id_qual, defaults to None
        :type message_id_qual: str, optional
        """
        if message_id is not SENTINEL:
            self.message_id = message_id
        if message_id_qual is not SENTINEL:
            self.message_id_qual = message_id_qual
        self._kwargs = kwargs
