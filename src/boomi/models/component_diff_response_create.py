
from typing import List, Union
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({})
class ChangeValue(BaseModel):
    """ChangeValue - Typed representation of newValue/oldValue in diff changes.

    Live API responses return these as objects with xpath and value fields
    rather than plain strings.

    :param xpath: XPath expression identifying the changed element, defaults to None
    :type xpath: str, optional
    :param value: The actual value content, defaults to None
    :type value: str, optional
    """

    def __init__(self, xpath: str = SENTINEL, value: str = SENTINEL, **kwargs):
        if xpath is not SENTINEL:
            self.xpath = xpath
        if value is not SENTINEL:
            self.value = value
        self._kwargs = kwargs


@JsonMap({})
class KeyPart(BaseModel):
    """KeyPart

    :param attribute: Attribute name, defaults to None
    :type attribute: str, optional
    :param value: Attribute value, defaults to None
    :type value: str, optional
    """

    def __init__(self, attribute: str = SENTINEL, value: str = SENTINEL, **kwargs):
        """KeyPart

        :param attribute: Attribute name, defaults to None
        :type attribute: str, optional
        :param value: Attribute value, defaults to None
        :type value: str, optional
        """
        if attribute is not SENTINEL:
            self.attribute = attribute
        if value is not SENTINEL:
            self.value = value
        self._kwargs = kwargs


@JsonMap({"element_name": "elementName", "key_part": "key-part"})
class ChangeElementKey1(BaseModel):
    """ChangeElementKey1

    :param element_name: Name of the element, defaults to None
    :type element_name: str, optional
    :param key_part: key_part, defaults to None
    :type key_part: KeyPart, optional
    """

    def __init__(
        self, element_name: str = SENTINEL, key_part: KeyPart = SENTINEL, **kwargs
    ):
        """ChangeElementKey1

        :param element_name: Name of the element, defaults to None
        :type element_name: str, optional
        :param key_part: key_part (may be object, list, or empty list in live responses), defaults to None
        :type key_part: KeyPart, optional
        """
        if element_name is not SENTINEL:
            self.element_name = element_name
        if key_part is not SENTINEL:
            # Normalize key-part: live API returns object, one-item list, or empty list
            if isinstance(key_part, list):
                self._key_parts = self._define_list(key_part, KeyPart) or []
                self.key_part = self._key_parts[0] if self._key_parts else None
            else:
                self.key_part = self._define_object(key_part, KeyPart)
                self._key_parts = [self.key_part] if self.key_part else []
        self._kwargs = kwargs

    @property
    def key_parts(self):
        """All key-part entries as a list."""
        return getattr(self, '_key_parts', [])


@JsonMap(
    {
        "type_": "type",
        "changed_particle_name": "changedParticleName",
        "element_key": "elementKey",
        "new_value": "newValue",
    }
)
class AdditionChange(BaseModel):
    """AdditionChange

    :param type_: Type of change (e.g., element), defaults to None
    :type type_: str, optional
    :param changed_particle_name: Name of the particle that changed, defaults to None
    :type changed_particle_name: str, optional
    :param element_key: element_key, defaults to None
    :type element_key: ChangeElementKey1, optional
    :param new_value: New value of the element in the diff, defaults to None
    :type new_value: Union[str, ChangeValue], optional
    """

    def __init__(
        self,
        type_: str = SENTINEL,
        changed_particle_name: str = SENTINEL,
        element_key: ChangeElementKey1 = SENTINEL,
        new_value: str = SENTINEL,
        **kwargs
    ):
        if type_ is not SENTINEL:
            self.type_ = type_
        if changed_particle_name is not SENTINEL:
            self.changed_particle_name = changed_particle_name
        if element_key is not SENTINEL:
            self.element_key = self._define_object(element_key, ChangeElementKey1)
        if new_value is not SENTINEL:
            if isinstance(new_value, dict):
                self.new_value = self._define_object(new_value, ChangeValue)
            else:
                self.new_value = new_value
        self._kwargs = kwargs


@JsonMap({})
class Addition(BaseModel):
    """Addition

    :param total: Total number of additions, defaults to None
    :type total: int, optional
    :param change: change, defaults to None
    :type change: List[AdditionChange], optional
    """

    def __init__(
        self, total: int = SENTINEL, change: List[AdditionChange] = SENTINEL, **kwargs
    ):
        if total is not SENTINEL:
            self.total = total
        if change is not SENTINEL:
            # Normalize singleton dict to list
            if isinstance(change, dict):
                change = [change]
            self.change = self._define_list(change, AdditionChange)
        self._kwargs = kwargs


@JsonMap({"element_name": "elementName"})
class ChangeElementKey2(BaseModel):
    """ChangeElementKey2

    :param element_name: Name of the element, defaults to None
    :type element_name: str, optional
    """

    def __init__(self, element_name: str = SENTINEL, **kwargs):
        if element_name is not SENTINEL:
            self.element_name = element_name
        self._kwargs = kwargs


@JsonMap(
    {
        "type_": "type",
        "changed_particle_name": "changedParticleName",
        "element_key": "elementKey",
        "new_value": "newValue",
        "old_value": "oldValue",
    }
)
class ModificationChange(BaseModel):
    """ModificationChange

    :param type_: Type of modification (e.g., attribute), defaults to None
    :type type_: str, optional
    :param changed_particle_name: Name of the particle that was modified, defaults to None
    :type changed_particle_name: str, optional
    :param element_key: element_key, defaults to None
    :type element_key: ChangeElementKey2, optional
    :param new_value: New value of the attribute, defaults to None
    :type new_value: Union[str, ChangeValue], optional
    :param old_value: Old value of the attribute, defaults to None
    :type old_value: Union[str, ChangeValue], optional
    """

    def __init__(
        self,
        type_: str = SENTINEL,
        changed_particle_name: str = SENTINEL,
        element_key: ChangeElementKey2 = SENTINEL,
        new_value: str = SENTINEL,
        old_value: str = SENTINEL,
        **kwargs
    ):
        if type_ is not SENTINEL:
            self.type_ = type_
        if changed_particle_name is not SENTINEL:
            self.changed_particle_name = changed_particle_name
        if element_key is not SENTINEL:
            self.element_key = self._define_object(element_key, ChangeElementKey2)
        if new_value is not SENTINEL:
            if isinstance(new_value, dict):
                self.new_value = self._define_object(new_value, ChangeValue)
            else:
                self.new_value = new_value
        if old_value is not SENTINEL:
            if isinstance(old_value, dict):
                self.old_value = self._define_object(old_value, ChangeValue)
            else:
                self.old_value = old_value
        self._kwargs = kwargs


@JsonMap({})
class Modification(BaseModel):
    """Modification

    :param total: Total number of modifications, defaults to None
    :type total: int, optional
    :param change: change, defaults to None
    :type change: List[ModificationChange], optional
    """

    def __init__(
        self, total: int = SENTINEL, change: List[ModificationChange] = SENTINEL, **kwargs
    ):
        if total is not SENTINEL:
            self.total = total
        if change is not SENTINEL:
            # Normalize singleton dict to list
            if isinstance(change, dict):
                change = [change]
            self.change = self._define_list(change, ModificationChange)
        self._kwargs = kwargs


@JsonMap(
    {
        "type_": "type",
        "changed_particle_name": "changedParticleName",
        "element_key": "elementKey",
        "old_value": "oldValue",
    }
)
class DeletionChange(BaseModel):
    """DeletionChange

    :param type_: Type of change (e.g., element), defaults to None
    :type type_: str, optional
    :param changed_particle_name: Name of the particle that changed, defaults to None
    :type changed_particle_name: str, optional
    :param element_key: element_key, defaults to None
    :type element_key: ChangeElementKey1, optional
    :param old_value: Old value of the element in the diff, defaults to None
    :type old_value: Union[str, ChangeValue], optional
    """

    def __init__(
        self,
        type_: str = SENTINEL,
        changed_particle_name: str = SENTINEL,
        element_key: ChangeElementKey1 = SENTINEL,
        old_value: str = SENTINEL,
        **kwargs
    ):
        if type_ is not SENTINEL:
            self.type_ = type_
        if changed_particle_name is not SENTINEL:
            self.changed_particle_name = changed_particle_name
        if element_key is not SENTINEL:
            self.element_key = self._define_object(element_key, ChangeElementKey1)
        if old_value is not SENTINEL:
            if isinstance(old_value, dict):
                self.old_value = self._define_object(old_value, ChangeValue)
            else:
                self.old_value = old_value
        self._kwargs = kwargs


@JsonMap({})
class Deletion(BaseModel):
    """Deletion

    :param total: Total number of deletions, defaults to None
    :type total: int, optional
    :param change: change, defaults to None
    :type change: List[DeletionChange], optional
    """

    def __init__(
        self, total: int = SENTINEL, change: List[DeletionChange] = SENTINEL, **kwargs
    ):
        if total is not SENTINEL:
            self.total = total
        if change is not SENTINEL:
            # Normalize singleton dict to list
            if isinstance(change, dict):
                change = [change]
            self.change = self._define_list(change, DeletionChange)
        self._kwargs = kwargs


@JsonMap({})
class GenericDiff(BaseModel):
    """GenericDiff

    :param addition: addition, defaults to None
    :type addition: Addition, optional
    :param deletion: deletion, defaults to None
    :type deletion: Deletion, optional
    :param modification: modification, defaults to None
    :type modification: Modification, optional
    """

    def __init__(
        self,
        addition: Addition = SENTINEL,
        deletion: Deletion = SENTINEL,
        modification: Modification = SENTINEL,
        **kwargs
    ):
        if addition is not SENTINEL:
            self.addition = self._define_object(addition, Addition)
        if deletion is not SENTINEL:
            self.deletion = self._define_object(deletion, Deletion)
        if modification is not SENTINEL:
            self.modification = self._define_object(modification, Modification)
        self._kwargs = kwargs


@JsonMap({"generic_diff": "GenericDiff"})
class ComponentDiffResponse(BaseModel):
    """ComponentDiffResponse

    :param message: Message providing details about the diffed components, defaults to None
    :type message: str, optional
    :param generic_diff: generic_diff, defaults to None
    :type generic_diff: GenericDiff, optional
    """

    def __init__(
        self, message: str = SENTINEL, generic_diff: GenericDiff = SENTINEL, **kwargs
    ):
        if message is not SENTINEL:
            self.message = message
        if generic_diff is not SENTINEL:
            self.generic_diff = self._define_object(generic_diff, GenericDiff)
        self._kwargs = kwargs


@JsonMap({"component_diff_response": "ComponentDiffResponse"})
class ComponentDiffResponseCreate(BaseModel):
    """ComponentDiffResponseCreate

    Wrapper for component diff responses. Handles both wrapped payloads
    (with a top-level ComponentDiffResponse key) and unwrapped payloads
    (where message/GenericDiff appear at the top level).

    :param component_diff_response: component_diff_response, defaults to None
    :type component_diff_response: ComponentDiffResponse, optional
    """

    def __init__(
        self, component_diff_response: ComponentDiffResponse = SENTINEL, **kwargs
    ):
        if component_diff_response is not SENTINEL:
            self.component_diff_response = self._define_object(
                component_diff_response, ComponentDiffResponse
            )
        elif kwargs.get('@type') == 'ComponentDiffResponse' or 'GenericDiff' in kwargs or 'message' in kwargs:
            # Unwrapped response: API returned diff data at top level without
            # the ComponentDiffResponse wrapper key. Build the inner response
            # from kwargs so public fields are populated.
            diff_data = {k: v for k, v in kwargs.items() if k != '@type'}
            self.component_diff_response = ComponentDiffResponse._unmap(diff_data)
            kwargs = {k: v for k, v in kwargs.items() if k not in ('message', 'GenericDiff', '@type')}
        self._kwargs = kwargs

    @property
    def message(self):
        """Proxy to component_diff_response.message for convenience."""
        cdr = getattr(self, 'component_diff_response', None)
        return getattr(cdr, 'message', None) if cdr else None

    @property
    def generic_diff(self):
        """Proxy to component_diff_response.generic_diff for convenience."""
        cdr = getattr(self, 'component_diff_response', None)
        return getattr(cdr, 'generic_diff', None) if cdr else None
