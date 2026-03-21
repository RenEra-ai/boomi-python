
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .component_merge_config import ComponentMergeConfig


@JsonMap({"component_merge_config": "ComponentMergeConfig"})
class ComponentMergeConfigs(BaseModel):
    """ComponentMergeConfigs

    :param component_merge_config: A list of ComponentMergeConfig entries., defaults to None
    :type component_merge_config: List[ComponentMergeConfig], optional
    """

    def __init__(
        self,
        component_merge_config: List[ComponentMergeConfig] = SENTINEL,
        **kwargs,
    ):
        """ComponentMergeConfigs

        :param component_merge_config: A list of ComponentMergeConfig entries., defaults to None
        :type component_merge_config: List[ComponentMergeConfig], optional
        """
        if component_merge_config is not SENTINEL:
            self.component_merge_config = self._define_list(
                component_merge_config, ComponentMergeConfig
            )
        self._kwargs = kwargs
