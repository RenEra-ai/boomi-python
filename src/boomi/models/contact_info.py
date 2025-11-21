
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({"contact_name": "contactName"})
class ContactInfo(BaseModel):
    """ContactInfo

    :param address1: address1, defaults to None
    :type address1: str, optional
    :param address2: address2, defaults to None
    :type address2: str, optional
    :param city: city, defaults to None
    :type city: str, optional
    :param contact_name: contact_name, defaults to None
    :type contact_name: str, optional
    :param country: country, defaults to None
    :type country: str, optional
    :param email: email, defaults to None
    :type email: str, optional
    :param fax: fax, defaults to None
    :type fax: str, optional
    :param phone: phone, defaults to None
    :type phone: str, optional
    :param postalcode: postalcode, defaults to None
    :type postalcode: str, optional
    :param state: state, defaults to None
    :type state: str, optional
    """

    def __init__(
        self,
        address1: str = SENTINEL,
        address2: str = SENTINEL,
        city: str = SENTINEL,
        contact_name: str = SENTINEL,
        country: str = SENTINEL,
        email: str = SENTINEL,
        fax: str = SENTINEL,
        phone: str = SENTINEL,
        postalcode: str = SENTINEL,
        state: str = SENTINEL,
        **kwargs
    ):
        """ContactInfo

        :param address1: address1, defaults to None
        :type address1: str, optional
        :param address2: address2, defaults to None
        :type address2: str, optional
        :param city: city, defaults to None
        :type city: str, optional
        :param contact_name: contact_name, defaults to None
        :type contact_name: str, optional
        :param country: country, defaults to None
        :type country: str, optional
        :param email: email, defaults to None
        :type email: str, optional
        :param fax: fax, defaults to None
        :type fax: str, optional
        :param phone: phone, defaults to None
        :type phone: str, optional
        :param postalcode: postalcode, defaults to None
        :type postalcode: str, optional
        :param state: state, defaults to None
        :type state: str, optional
        """
        if address1 is not SENTINEL:
            self.address1 = address1
        if address2 is not SENTINEL:
            self.address2 = address2
        if city is not SENTINEL:
            self.city = city
        if contact_name is not SENTINEL:
            self.contact_name = contact_name
        if country is not SENTINEL:
            self.country = country
        if email is not SENTINEL:
            self.email = email
        if fax is not SENTINEL:
            self.fax = fax
        if phone is not SENTINEL:
            self.phone = phone
        if postalcode is not SENTINEL:
            self.postalcode = postalcode
        if state is not SENTINEL:
            self.state = state
        self._kwargs = kwargs
