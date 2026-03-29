"""Cross-model regression matrix.

Tests model archetypes to ensure the SENTINEL constructor invariant holds:
- Normal single-object models accept empty _unmap({})
- Bulk response wrappers accept error-only items (no result)
- Async response models accept sparse payloads (status-code only)
- Wrapper models with single list field accept list auto-wrap

This is NOT a per-bug test — it's a structural invariant test that should
catch regressions from future schema updates or batch script runs.
"""

import pytest
from boomi.models.persisted_process_properties import PersistedProcessProperties
from boomi.models.persisted_process_properties_async_response import (
    PersistedProcessPropertiesAsyncResponse,
)
from boomi.models.environment_map_extension_bulk_response import (
    EnvironmentMapExtensionBulkResponseResponse,
)
from boomi.models.environment_map_extension_user_defined_function import (
    EnvironmentMapExtensionUserDefinedFunction,
)
from boomi.models.map_extensions_inputs import MapExtensionsInputs
from boomi.models.atom import Atom
from boomi.models.atom_counters_async_response import AtomCountersAsyncResponse
from boomi.models.component import Component
from boomi.models.component_bulk_response import ComponentBulkResponseResponse
from boomi.models.account_bulk_response import AccountBulkResponseResponse
from boomi.models.deployed_package import DeployedPackage
from boomi.models.atom_disk_space_async_response import AtomDiskSpaceAsyncResponse


class TestNormalModelSparsePayload:
    """Normal models must accept _unmap({}) without crashing."""

    @pytest.mark.parametrize("model_class", [
        PersistedProcessProperties,
        Atom,
        Component,
        DeployedPackage,
    ])
    def test_empty_unmap(self, model_class):
        obj = model_class._unmap({})
        assert obj is not None

    @pytest.mark.parametrize("model_class", [
        PersistedProcessProperties,
        Atom,
        Component,
        DeployedPackage,
    ])
    def test_partial_unmap(self, model_class):
        """Models should handle a payload with only one arbitrary field."""
        obj = model_class._unmap({"nonexistentField": "value"})
        assert obj is not None


class TestAsyncResponseSparsePayload:
    """Async response models must accept status-code-only payloads."""

    @pytest.mark.parametrize("model_class", [
        PersistedProcessPropertiesAsyncResponse,
        AtomCountersAsyncResponse,
        AtomDiskSpaceAsyncResponse,
    ])
    def test_status_code_only(self, model_class):
        obj = model_class._unmap({"responseStatusCode": 202})
        assert obj.response_status_code == 202
        assert not hasattr(obj, "result")

    @pytest.mark.parametrize("model_class", [
        PersistedProcessPropertiesAsyncResponse,
        AtomCountersAsyncResponse,
        AtomDiskSpaceAsyncResponse,
    ])
    def test_string_status_code_coerced_to_int(self, model_class):
        """XML path returns strings — response_status_code must be coerced to int."""
        obj = model_class._unmap({"responseStatusCode": "202"})
        assert isinstance(obj.response_status_code, int)
        assert obj.response_status_code == 202

    @pytest.mark.parametrize("model_class", [
        PersistedProcessPropertiesAsyncResponse,
        AtomCountersAsyncResponse,
        AtomDiskSpaceAsyncResponse,
    ])
    def test_empty_unmap(self, model_class):
        obj = model_class._unmap({})
        assert obj is not None


class TestBulkResponseErrorItem:
    """Bulk response inner models must accept error-only items (no result)."""

    @pytest.mark.parametrize("model_class", [
        EnvironmentMapExtensionBulkResponseResponse,
        ComponentBulkResponseResponse,
        AccountBulkResponseResponse,
    ])
    def test_error_only_construction(self, model_class):
        obj = model_class(status_code=400, error_message="Not found")
        assert obj.status_code == 400
        assert not hasattr(obj, "result")

    @pytest.mark.parametrize("model_class", [
        EnvironmentMapExtensionBulkResponseResponse,
        ComponentBulkResponseResponse,
        AccountBulkResponseResponse,
    ])
    def test_error_only_unmap(self, model_class):
        obj = model_class._unmap({
            "statusCode": 400,
            "errorMessage": "Not found",
            "index": 0,
        })
        assert obj.status_code == 400
        assert not hasattr(obj, "result")


class TestWrapperModelAutoWrap:
    """Single-field wrapper models must accept plain list input."""

    def test_map_extensions_inputs_from_list(self):
        obj = EnvironmentMapExtensionUserDefinedFunction(
            inputs=[{"name": "in1", "key": 1}],
        )
        assert isinstance(obj.inputs, MapExtensionsInputs)

    def test_udf_partial_payload(self):
        obj = EnvironmentMapExtensionUserDefinedFunction._unmap({"name": "test"})
        assert obj.name == "test"
        assert not hasattr(obj, "inputs")
