
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap(
    {
        "address1": "address1",
        "address2": "address2",
        "city": "city",
        "contact_name": "contactName",
        "contact_url": "contactUrl",
        "country": "country",
        "email": "email",
        "fax": "fax",
        "phone": "phone",
        "postalcode": "postalcode",
        "state": "state",
    }
)
class OrganizationContactInfo(BaseModel):
    """OrganizationContactInfo

    :param address1: First line of the street address of the organization., defaults to None
    :type address1: str, optional
    :param address2: Second line of the street address of the organization., defaults to None
    :type address2: str, optional
    :param city: Location of the city for the organization., defaults to None
    :type city: str, optional
    :param contact_name: Name of the contact for the organization., defaults to None
    :type contact_name: str, optional
    :param contact_url: Contact URL for the organization., defaults to None
    :type contact_url: str, optional
    :param country: Location of the country for the organization., defaults to None
    :type country: str, optional
    :param email: Email address of the organization., defaults to None
    :type email: str, optional
    :param fax: Fax number for the organization., defaults to None
    :type fax: str, optional
    :param phone: Phone number for the organization., defaults to None
    :type phone: str, optional
    :param postalcode: Postal code, such as a Zip Code., defaults to None
    :type postalcode: str, optional
    :param state: Location of the state or province for the organization., defaults to None
    :type state: str, optional
    """

    def __init__(
        self,
        address1: str = SENTINEL,
        address2: str = SENTINEL,
        city: str = SENTINEL,
        contact_name: str = SENTINEL,
        contact_url: str = SENTINEL,
        country: str = SENTINEL,
        email: str = SENTINEL,
        fax: str = SENTINEL,
        phone: str = SENTINEL,
        postalcode: str = SENTINEL,
        state: str = SENTINEL,
        **kwargs
    ):
        """OrganizationContactInfo

        :param address1: First line of the street address of the organization., defaults to None
        :type address1: str, optional
        :param address2: Second line of the street address of the organization., defaults to None
        :type address2: str, optional
        :param city: Location of the city for the organization., defaults to None
        :type city: str, optional
        :param contact_name: Name of the contact for the organization., defaults to None
        :type contact_name: str, optional
        :param contact_url: Contact URL for the organization., defaults to None
        :type contact_url: str, optional
        :param country: Location of the country for the organization., defaults to None
        :type country: str, optional
        :param email: Email address of the organization., defaults to None
        :type email: str, optional
        :param fax: Fax number for the organization., defaults to None
        :type fax: str, optional
        :param phone: Phone number for the organization., defaults to None
        :type phone: str, optional
        :param postalcode: Postal code, such as a Zip Code., defaults to None
        :type postalcode: str, optional
        :param state: Location of the state or province for the organization., defaults to None
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
        if contact_url is not SENTINEL:
            self.contact_url = contact_url
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
