"""Tests for BUG-11: EnvironmentMapExtensionUserDefinedFunction construction fixes.

Covers:
- List auto-wrap in _define_object for single-field wrapper models
- Optional positional args (inputs, mappings, outputs, steps)
- _unmap() type validation
- Round-trip serialization
"""

import pytest
from boomi.models.environment_map_extension_user_defined_function import (
    EnvironmentMapExtensionUserDefinedFunction,
)
from boomi.models.map_extensions_inputs import MapExtensionsInputs
from boomi.models.map_extensions_function_mappings import MapExtensionsFunctionMappings
from boomi.models.map_extensions_outputs import MapExtensionsOutputs
from boomi.models.map_extensions_function_steps import MapExtensionsFunctionSteps
from boomi.models.simple_lookup_table import SimpleLookupTable
from boomi.models.simple_lookup_table_rows import SimpleLookupTableRows


class TestUdfUnmapApiFormat:
    """_unmap() with proper API-format dicts should still work."""

    def test_full_api_format(self):
        data = {
            "Inputs": {"Input": [{"name": "in1", "key": 1}]},
            "Outputs": {"Output": [{"name": "out1", "key": 1}]},
            "Mappings": {"Mapping": []},
            "Steps": {"Step": []},
            "name": "_TEST",
        }
        obj = EnvironmentMapExtensionUserDefinedFunction._unmap(data)
        assert obj.name == "_TEST"
        assert isinstance(obj.inputs, MapExtensionsInputs)
        assert isinstance(obj.mappings, MapExtensionsFunctionMappings)
        assert isinstance(obj.outputs, MapExtensionsOutputs)
        assert isinstance(obj.steps, MapExtensionsFunctionSteps)

    def test_api_format_with_metadata(self):
        data = {
            "Inputs": {"Input": []},
            "Outputs": {"Output": []},
            "Mappings": {"Mapping": []},
            "Steps": {"Step": []},
            "name": "_TEST",
            "environmentMapExtensionId": "eme-123",
            "id": "udf-456",
        }
        obj = EnvironmentMapExtensionUserDefinedFunction._unmap(data)
        assert obj.environment_map_extension_id == "eme-123"
        assert obj.id_ == "udf-456"


class TestUdfListAutoWrap:
    """Plain lists should be auto-wrapped into single-field wrapper models."""

    def test_inputs_as_plain_list(self):
        obj = EnvironmentMapExtensionUserDefinedFunction(
            inputs=[{"name": "in1", "key": 1}],
        )
        assert isinstance(obj.inputs, MapExtensionsInputs)
        assert len(obj.inputs.input) == 1
        assert obj.inputs.input[0].name == "in1"

    def test_outputs_as_plain_list(self):
        obj = EnvironmentMapExtensionUserDefinedFunction(
            outputs=[{"name": "out1", "key": 1}],
        )
        assert isinstance(obj.outputs, MapExtensionsOutputs)
        assert len(obj.outputs.output) == 1

    def test_mappings_as_plain_list(self):
        obj = EnvironmentMapExtensionUserDefinedFunction(mappings=[])
        assert isinstance(obj.mappings, MapExtensionsFunctionMappings)

    def test_steps_as_plain_list(self):
        obj = EnvironmentMapExtensionUserDefinedFunction(steps=[])
        assert isinstance(obj.steps, MapExtensionsFunctionSteps)

    def test_unmap_with_plain_lists(self):
        """The exact BUG-11 crash path: _unmap with user-provided flat data."""
        data = {
            "name": "_TEST",
            "inputs": [{"name": "in1", "key": 1}],
            "outputs": [{"name": "out1", "key": 1}],
            "mappings": [],
            "steps": [],
        }
        obj = EnvironmentMapExtensionUserDefinedFunction._unmap(data)
        assert obj.name == "_TEST"
        assert isinstance(obj.inputs, MapExtensionsInputs)


class TestUdfMissingFields:
    """Construction with missing fields should not crash."""

    def test_name_only(self):
        obj = EnvironmentMapExtensionUserDefinedFunction(name="_TEST")
        assert obj.name == "_TEST"
        assert not hasattr(obj, "inputs")
        assert not hasattr(obj, "mappings")

    def test_empty_unmap(self):
        obj = EnvironmentMapExtensionUserDefinedFunction._unmap({})
        assert not hasattr(obj, "name")
        assert not hasattr(obj, "inputs")

    def test_partial_fields(self):
        obj = EnvironmentMapExtensionUserDefinedFunction._unmap({
            "name": "partial",
            "Inputs": {"Input": [{"name": "in1", "key": 1}]},
        })
        assert obj.name == "partial"
        assert isinstance(obj.inputs, MapExtensionsInputs)
        assert not hasattr(obj, "steps")


class TestUnmapTypeValidation:
    """_unmap() should raise TypeError for non-dict input."""

    def test_list_raises_type_error(self):
        with pytest.raises(TypeError, match="expects a dict, got list"):
            EnvironmentMapExtensionUserDefinedFunction._unmap([1, 2, 3])

    def test_string_raises_type_error(self):
        with pytest.raises(TypeError, match="expects a dict, got str"):
            EnvironmentMapExtensionUserDefinedFunction._unmap("bad input")


class TestSimpleLookupTableAutoWrap:
    """SimpleLookupTable.rows has the same single-field wrapper pattern."""

    def test_rows_as_plain_list(self):
        obj = SimpleLookupTable(rows=[{"ref1": "a", "ref2": "b"}])
        assert isinstance(obj.rows, SimpleLookupTableRows)

    def test_rows_as_wrapper_dict(self):
        obj = SimpleLookupTable(rows={"Row": [{"ref1": "a", "ref2": "b"}]})
        assert isinstance(obj.rows, SimpleLookupTableRows)


class TestRoundTrip:
    """Construct → _map() should produce valid serialized output."""

    def test_round_trip_serialization(self):
        obj = EnvironmentMapExtensionUserDefinedFunction._unmap({
            "Inputs": {"Input": [{"name": "in1", "key": 1}]},
            "Outputs": {"Output": [{"name": "out1", "key": 1}]},
            "Mappings": {"Mapping": []},
            "Steps": {"Step": []},
            "name": "_RT_TEST",
            "environmentMapExtensionId": "eme-abc",
        })
        mapped = obj._map()
        assert mapped["name"] == "_RT_TEST"
        assert mapped["environmentMapExtensionId"] == "eme-abc"
        assert "Inputs" in mapped
        assert "Input" in mapped["Inputs"]
        assert mapped["Inputs"]["Input"][0]["name"] == "in1"
