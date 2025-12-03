
from __future__ import annotations
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .http_endpoint import HttpEndpoint
from .http_request_parameters import HttpRequestParameters
from .httpo_auth_credentials import HttpoAuthCredentials


class GrantType(Enum):
    """An enumeration representing different categories.

    :cvar CODE: "code"
    :vartype CODE: str
    :cvar CLIENTCREDENTIALS: "client_credentials"
    :vartype CLIENTCREDENTIALS: str
    :cvar PASSWORD: "password"
    :vartype PASSWORD: str
    """

    CODE = "code"
    CLIENTCREDENTIALS = "client_credentials"
    PASSWORD = "password"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, GrantType._member_map_.values()))


@JsonMap(
    {
        "access_token_endpoint": "accessTokenEndpoint",
        "access_token_parameters": "accessTokenParameters",
        "authorization_parameters": "authorizationParameters",
        "authorization_token_endpoint": "authorizationTokenEndpoint",
        "grant_type": "grantType",
    }
)
class HttpoAuth2Settings(BaseModel):
    """HttpoAuth2Settings

    :param access_token_endpoint: access_token_endpoint, defaults to None
    :type access_token_endpoint: HttpEndpoint, optional
    :param access_token_parameters: access_token_parameters, defaults to None
    :type access_token_parameters: HttpRequestParameters, optional
    :param authorization_parameters: authorization_parameters, defaults to None
    :type authorization_parameters: HttpRequestParameters, optional
    :param authorization_token_endpoint: authorization_token_endpoint, defaults to None
    :type authorization_token_endpoint: HttpEndpoint, optional
    :param credentials: credentials, defaults to None
    :type credentials: HttpoAuthCredentials, optional
    :param grant_type: grant_type, defaults to None
    :type grant_type: GrantType, optional
    :param scope: scope, defaults to None
    :type scope: str, optional
    """

    def __init__(
        self,
        access_token_endpoint: HttpEndpoint = SENTINEL,
        access_token_parameters: HttpRequestParameters = SENTINEL,
        authorization_parameters: HttpRequestParameters = SENTINEL,
        authorization_token_endpoint: HttpEndpoint = SENTINEL,
        credentials: HttpoAuthCredentials = SENTINEL,
        grant_type: GrantType = SENTINEL,
        scope: str = SENTINEL,
        **kwargs,
    ):
        """HttpoAuth2Settings

        :param access_token_endpoint: access_token_endpoint, defaults to None
        :type access_token_endpoint: HttpEndpoint, optional
        :param access_token_parameters: access_token_parameters, defaults to None
        :type access_token_parameters: HttpRequestParameters, optional
        :param authorization_parameters: authorization_parameters, defaults to None
        :type authorization_parameters: HttpRequestParameters, optional
        :param authorization_token_endpoint: authorization_token_endpoint, defaults to None
        :type authorization_token_endpoint: HttpEndpoint, optional
        :param credentials: credentials, defaults to None
        :type credentials: HttpoAuthCredentials, optional
        :param grant_type: grant_type, defaults to None
        :type grant_type: GrantType, optional
        :param scope: scope, defaults to None
        :type scope: str, optional
        """
        if access_token_endpoint is not SENTINEL:
            self.access_token_endpoint = self._define_object(
                access_token_endpoint, HttpEndpoint
            )
        if access_token_parameters is not SENTINEL:
            self.access_token_parameters = self._define_object(
                access_token_parameters, HttpRequestParameters
            )
        if authorization_parameters is not SENTINEL:
            self.authorization_parameters = self._define_object(
                authorization_parameters, HttpRequestParameters
            )
        if authorization_token_endpoint is not SENTINEL:
            self.authorization_token_endpoint = self._define_object(
                authorization_token_endpoint, HttpEndpoint
            )
        if credentials is not SENTINEL:
            self.credentials = self._define_object(credentials, HttpoAuthCredentials)
        if grant_type is not SENTINEL:
            self.grant_type = self._enum_matching(
                grant_type, GrantType.list(), "grant_type"
            )
        if scope is not SENTINEL:
            self.scope = scope
        self._kwargs = kwargs
