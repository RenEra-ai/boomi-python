
from __future__ import annotations
from typing import List
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL
from .runtime_observability_settings import RuntimeObservabilitySettings


@JsonMap(
    {
        "number_of_results": "numberOfResults",
        "response_status_code": "responseStatusCode",
    }
)
class RuntimeObservabilitySettingsAsyncResponse(BaseModel):
    """RuntimeObservabilitySettingsAsyncResponse

    :param response_status_code: response_status_code
    :type response_status_code: int
    :param number_of_results: number_of_results, defaults to None
    :type number_of_results: int, optional
    :param result: result, defaults to None
    :type result: List[RuntimeObservabilitySettings], optional
    """

    def __init__(
        self,
        response_status_code: int,
        number_of_results: int = SENTINEL,
        result: List[RuntimeObservabilitySettings] = SENTINEL,
        **kwargs,
    ):
        """RuntimeObservabilitySettingsAsyncResponse

        :param response_status_code: response_status_code
        :type response_status_code: int
        :param number_of_results: number_of_results, defaults to None
        :type number_of_results: int, optional
        :param result: result, defaults to None
        :type result: List[RuntimeObservabilitySettings], optional
        """
        if number_of_results is not SENTINEL:
            self.number_of_results = number_of_results
        self.response_status_code = response_status_code
        if result is not SENTINEL:
            self.result = self._define_list(
                result, RuntimeObservabilitySettings
            )
        self._kwargs = kwargs
