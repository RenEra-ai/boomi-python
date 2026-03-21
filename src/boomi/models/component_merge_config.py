
from __future__ import annotations
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap({"component_id": "componentId", "priority_branch": "priorityBranch"})
class ComponentMergeConfig(BaseModel):
    """ComponentMergeConfig

    :param component_id: The ID of the component to merge.
    :type component_id: str
    :param priority_branch: The priority branch for the merge., defaults to None
    :type priority_branch: str, optional
    """

    def __init__(
        self,
        component_id: str,
        priority_branch: str = SENTINEL,
        **kwargs,
    ):
        """ComponentMergeConfig

        :param component_id: The ID of the component to merge.
        :type component_id: str
        :param priority_branch: The priority branch for the merge., defaults to None
        :type priority_branch: str, optional
        """
        self.component_id = component_id
        if priority_branch is not SENTINEL:
            self.priority_branch = priority_branch
        self._kwargs = kwargs
