"""Tests for _define_object() list auto-wrap guard in base_model.py.

Ensures auto-wrap ONLY fires for genuine wrapper models (single list field),
not for arbitrary single-field models.
"""

import pytest
from boomi.models.utils.base_model import BaseModel
from boomi.models.utils.json_map import JsonMap
from boomi.models.utils.sentinel import SENTINEL


# --- Test wrapper model (should auto-wrap) ---
@JsonMap({"items": "Item"})
class FakeWrapperModel(BaseModel):
    def __init__(self, items=SENTINEL, **kwargs):
        if items is not SENTINEL:
            self.items = items


# --- Test non-wrapper model with TWO fields (should NOT auto-wrap) ---
@JsonMap({"type_": "type", "name": "name"})
class FakeMultiFieldModel(BaseModel):
    def __init__(self, type_=SENTINEL, name=SENTINEL, **kwargs):
        if type_ is not SENTINEL:
            self.type_ = type_
        if name is not SENTINEL:
            self.name = name


class Host(BaseModel):
    """Host model to test _define_object calls."""

    def try_define_object(self, data, cls):
        return self._define_object(data, cls)


class TestDefineObjectAutoWrap:

    def test_list_autowraps_for_wrapper_model(self):
        host = Host()
        result = host.try_define_object([{"name": "a"}], FakeWrapperModel)
        assert isinstance(result, FakeWrapperModel)
        assert result.items == [{"name": "a"}]

    def test_list_raises_for_multi_field_model(self):
        host = Host()
        with pytest.raises(TypeError, match="got list"):
            host.try_define_object(["a", "b"], FakeMultiFieldModel)

    def test_dict_passes_through(self):
        host = Host()
        result = host.try_define_object({"Item": [{"name": "a"}]}, FakeWrapperModel)
        assert isinstance(result, FakeWrapperModel)

    def test_none_returns_none(self):
        host = Host()
        assert host.try_define_object(None, FakeWrapperModel) is None

    def test_sentinel_returns_none(self):
        host = Host()
        assert host.try_define_object(SENTINEL, FakeWrapperModel) is None

    def test_already_correct_type_passes_through(self):
        host = Host()
        obj = FakeWrapperModel(items=["x"])
        assert host.try_define_object(obj, FakeWrapperModel) is obj
