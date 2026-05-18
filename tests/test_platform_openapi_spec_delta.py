"""Regression tests for the platformOpenAPISpec.json delta sync.

Covers:
- AccountSsoConfig.caseInsensitiveFederationId mapping (new field).
- GetAssignableRoles endpoint path casing fix (/getAssignableRoles).
- Environment.GB enum value (new GB/EU base URL).
- EnvironmentMapExtensionUserDefinedFunctionSummarySimpleExpressionProperty
  retains all four SDK-supported values for backward compatibility.
"""

from __future__ import annotations

import inspect

from boomi.models.account_sso_config import AccountSsoConfig
from boomi.models.environment_map_extension_user_defined_function_summary_simple_expression import (
    EnvironmentMapExtensionUserDefinedFunctionSummarySimpleExpressionProperty,
)
from boomi.net.environment.environment import Environment
from boomi.services.get_assignable_roles import GetAssignableRolesService


def test_account_sso_config_maps_case_insensitive_federation_id():
    config = AccountSsoConfig(case_insensitive_federation_id=True)
    mapped = config._map()
    assert mapped.get("caseInsensitiveFederationId") is True


def test_account_sso_config_unmaps_case_insensitive_federation_id():
    config = AccountSsoConfig._unmap({"caseInsensitiveFederationId": True})
    assert config.case_insensitive_federation_id is True


def test_account_sso_config_omits_field_when_not_set():
    config = AccountSsoConfig(account_id="acct-1")
    mapped = config._map()
    assert "caseInsensitiveFederationId" not in mapped
    assert mapped.get("accountId") == "acct-1"


def test_get_assignable_roles_uses_lowercase_endpoint_path():
    source = inspect.getsource(GetAssignableRolesService)
    assert "/getAssignableRoles" in source
    assert "/GetAssignableRoles" not in source


def test_environment_gb_url_is_available():
    assert (
        Environment.GB.url
        == "https://api.platform.gb.boomi.com/api/rest/v1/{accountId}"
    )
    assert (
        Environment.DEFAULT.url == "https://api.boomi.com/api/rest/v1/{accountId}"
    )


def test_udf_summary_property_enum_keeps_backward_compatible_values():
    values = {
        member.value
        for member in EnvironmentMapExtensionUserDefinedFunctionSummarySimpleExpressionProperty
    }
    assert {
        "environmentId",
        "extensionGroupId",
        "environmentMapExtensionId",
        "componentId",
    }.issubset(values)
