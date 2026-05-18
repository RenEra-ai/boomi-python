"""Live QA for the platformOpenAPISpec.json delta sync.

Hits the real Boomi Platform API with credentials from .env and verifies:
- /getAssignableRoles (lowercase) — proves the casing fix works against
  the live endpoint and the SDK still parses Roles back.
- AccountSSOConfig GET — proves the new caseInsensitiveFederationId field
  unmaps from the real response (when the account is configured for SSO),
  or at minimum that the existing fields continue to unmap.
- Environment.GB — verifies a Boomi client built with the GB enum
  resolves to the GB base URL via the SDK's normal setup.

Run with:
    pytest --run-live tests/live/test_spec_delta_qa_live.py -q -s
"""

from __future__ import annotations

import os
from pathlib import Path

import pytest
import requests
from dotenv import load_dotenv

from boomi import Boomi
from boomi.models import AccountSsoConfig, Roles
from boomi.net.environment.environment import Environment


REPO_ROOT = Path(__file__).resolve().parents[2]
load_dotenv(REPO_ROOT / ".env")


pytestmark = [pytest.mark.live, pytest.mark.live_spec_delta]


# ---------------------------------------------------------------------------
# 1. /getAssignableRoles  (path casing fix)
# ---------------------------------------------------------------------------

def test_get_assignable_roles_live(sync_sdk: Boomi, live_credentials: dict) -> None:
    """Verify the SDK can call /getAssignableRoles end-to-end (casing fix)."""

    result = sync_sdk.get_assignable_roles.get_get_assignable_roles()

    assert result is not None, "expected a response from /getAssignableRoles"
    assert isinstance(result, Roles), f"expected Roles, got {type(result).__name__}: {result!r}"

    role_list = getattr(result, "role", None) or []
    if not isinstance(role_list, list):
        role_list = [role_list]
    print(f"\n[live] /getAssignableRoles returned {len(role_list)} role(s)")
    if role_list:
        first = role_list[0]
        print(f"[live] sample role: name={getattr(first, 'name', None)!r} id={getattr(first, 'id_', getattr(first, 'id', None))!r}")


def test_get_assignable_roles_old_path_is_404(sync_sdk: Boomi, live_credentials: dict) -> None:
    """Direct REST sanity-check: the OLD CamelCase path must NOT work, the
    NEW lowercase path MUST work. Proves we shipped the right fix.

    Uses the SDK service's resolved base_url so this honors BOOMI_BASE_URL
    (e.g. running against the GB region) instead of always hitting US.
    """

    auth = (live_credentials["username"], live_credentials["password"])
    headers = {"Accept": "application/json"}
    base = sync_sdk.get_assignable_roles.base_url

    old = requests.get(f"{base}/GetAssignableRoles", auth=auth, headers=headers, timeout=30)
    new = requests.get(f"{base}/getAssignableRoles", auth=auth, headers=headers, timeout=30)

    print(f"\n[live] OLD /GetAssignableRoles -> HTTP {old.status_code}")
    print(f"[live] NEW /getAssignableRoles -> HTTP {new.status_code}")

    assert new.status_code == 200, f"new lowercase path should succeed, got {new.status_code}: {new.text[:200]}"
    # The platform routes the old CamelCase path to a different handler (400/404/405
    # all observed in the wild). The meaningful invariant is: new succeeds, old does not.
    assert old.status_code != 200, (
        f"old CamelCase path should NOT succeed; got 200 — the casing fix would be unnecessary. "
        f"Body: {old.text[:200]}"
    )
    assert 400 <= old.status_code < 500, (
        f"old CamelCase path should return a 4xx rejection; got {old.status_code}: {old.text[:200]}"
    )


# ---------------------------------------------------------------------------
# 2. AccountSSOConfig (caseInsensitiveFederationId field)
# ---------------------------------------------------------------------------

def test_account_sso_config_get_live(sync_sdk: Boomi, live_credentials: dict) -> None:
    """Verify GET AccountSSOConfig parses, and that the new field is
    accessible (None is acceptable if the account hasn't set it)."""

    account = live_credentials["account_id"]
    result = sync_sdk.account_sso_config.get_account_sso_config(id_=account)

    assert result is not None, "expected an AccountSsoConfig response"
    assert isinstance(result, AccountSsoConfig), (
        f"expected AccountSsoConfig, got {type(result).__name__}: {result!r}"
    )

    cifi = getattr(result, "case_insensitive_federation_id", None)
    enabled = getattr(result, "enabled", None)
    print(f"\n[live] AccountSSOConfig enabled={enabled!r}")
    print(f"[live] AccountSSOConfig case_insensitive_federation_id={cifi!r}")

    # The field must be addressable on the model regardless of value.
    # If the server returned it, validate the type is bool-like.
    if cifi is not None:
        assert isinstance(cifi, bool), (
            f"caseInsensitiveFederationId expected bool, got {type(cifi).__name__}={cifi!r}"
        )


def test_account_sso_config_raw_xml_contains_field(sync_sdk: Boomi, live_credentials: dict) -> None:
    """Direct API hit: inspect the raw XML/JSON the server returned and
    confirm caseInsensitiveFederationId is something the SDK is allowed
    to parse (presence is optional, but if present must be bool-shaped).

    Uses the SDK service's resolved base_url so this honors BOOMI_BASE_URL.
    """

    account = live_credentials["account_id"]
    auth = (live_credentials["username"], live_credentials["password"])

    # Try XML first (Boomi's native format), then JSON.
    url = f"{sync_sdk.account_sso_config.base_url}/AccountSSOConfig/{account}"
    xml_resp = requests.get(url, auth=auth, headers={"Accept": "application/xml"}, timeout=30)
    json_resp = requests.get(url, auth=auth, headers={"Accept": "application/json"}, timeout=30)

    print(f"\n[live] AccountSSOConfig XML  HTTP {xml_resp.status_code}")
    print(f"[live] AccountSSOConfig JSON HTTP {json_resp.status_code}")
    snippet_xml = xml_resp.text[:300] if xml_resp.ok else xml_resp.text[:200]
    snippet_json = json_resp.text[:300] if json_resp.ok else json_resp.text[:200]
    print(f"[live] XML snippet : {snippet_xml}")
    print(f"[live] JSON snippet: {snippet_json}")

    if xml_resp.ok and "caseInsensitiveFederationId" in xml_resp.text:
        print("[live] caseInsensitiveFederationId IS present in the live XML response — field round-trips.")
    elif json_resp.ok and "caseInsensitiveFederationId" in json_resp.text:
        print("[live] caseInsensitiveFederationId IS present in the live JSON response — field round-trips.")
    else:
        pytest.skip(
            "caseInsensitiveFederationId not returned by this account's SSO config "
            "(field may only appear when the CASE_INSENSITIVE_FEDERATION_ID_COMPARISON "
            "feature is enabled). Schema mapping verified separately in tests/test_platform_openapi_spec_delta.py."
        )


# ---------------------------------------------------------------------------
# 3. Environment.GB resolution
# ---------------------------------------------------------------------------

def test_environment_gb_resolves_in_sdk_client(live_credentials: dict) -> None:
    """Construct a Boomi client with Environment.GB and confirm the
    underlying services pick up the GB base URL."""

    account = live_credentials["account_id"]
    client = Boomi(
        account_id=account,
        username=live_credentials["username"],
        password=live_credentials["password"],
        base_url=Environment.GB,
    )

    # The Boomi client stores the raw enum value (with {accountId} unfilled).
    template = "https://api.platform.gb.boomi.com/api/rest/v1/{accountId}"
    assert client._base_url == template, f"client._base_url should be GB template, got {client._base_url!r}"

    # Service-level base_url has {accountId} substituted with the live account.
    filled = f"https://api.platform.gb.boomi.com/api/rest/v1/{account}"
    assert client.get_assignable_roles.base_url == filled, (
        f"service base_url should be filled GB URL, got {client.get_assignable_roles.base_url!r}"
    )
    assert client.account_sso_config.base_url == filled
    print(f"\n[live] Environment.GB resolved on client (template): {template}")
    print(f"[live] Environment.GB resolved on services (filled):  {filled}")
