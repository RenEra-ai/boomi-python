
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap(
    {
        "archive_processed_documents": "archiveProcessedDocuments",
        "container_name": "containerName",
        "container_purge_days": "containerPurgeDays",
        "container_purge_immediately": "containerPurgeImmediately",
        "default_time_zone_for_account_schedules": "defaultTimeZoneForAccountSchedules",
        "low_latency_warning_threshold": "lowLatencyWarningThreshold",
        "partial_update": "partialUpdate",
        "purge_schedule_for_components": "purgeScheduleForComponents",
        "purge_schedule_for_logs": "purgeScheduleForLogs",
        "purge_schedule_for_processed_documents": "purgeScheduleForProcessedDocuments",
        "purge_schedule_for_temporary_data": "purgeScheduleForTemporaryData",
        "runtime_id": "runtimeId",
    }
)
class CloudAttachmentProperties(BaseModel):
    """CloudAttachmentProperties

    :param archive_processed_documents: archive_processed_documents, defaults to None
    :type archive_processed_documents: bool, optional
    :param container_name: container_name, defaults to None
    :type container_name: str, optional
    :param container_purge_days: container_purge_days, defaults to None
    :type container_purge_days: int, optional
    :param container_purge_immediately: container_purge_immediately, defaults to None
    :type container_purge_immediately: bool, optional
    :param default_time_zone_for_account_schedules: default_time_zone_for_account_schedules, defaults to None
    :type default_time_zone_for_account_schedules: str, optional
    :param low_latency_warning_threshold: low_latency_warning_threshold, defaults to None
    :type low_latency_warning_threshold: int, optional
    :param partial_update: partial_update, defaults to None
    :type partial_update: bool, optional
    :param purge_schedule_for_components: purge_schedule_for_components, defaults to None
    :type purge_schedule_for_components: int, optional
    :param purge_schedule_for_logs: purge_schedule_for_logs, defaults to None
    :type purge_schedule_for_logs: int, optional
    :param purge_schedule_for_processed_documents: purge_schedule_for_processed_documents, defaults to None
    :type purge_schedule_for_processed_documents: int, optional
    :param purge_schedule_for_temporary_data: purge_schedule_for_temporary_data, defaults to None
    :type purge_schedule_for_temporary_data: int, optional
    :param runtime_id: runtime_id, defaults to None
    :type runtime_id: str, optional
    """

    def __init__(
        self,
        archive_processed_documents: bool = SENTINEL,
        container_name: str = SENTINEL,
        container_purge_days: int = SENTINEL,
        container_purge_immediately: bool = SENTINEL,
        default_time_zone_for_account_schedules: str = SENTINEL,
        low_latency_warning_threshold: int = SENTINEL,
        partial_update: bool = SENTINEL,
        purge_schedule_for_components: int = SENTINEL,
        purge_schedule_for_logs: int = SENTINEL,
        purge_schedule_for_processed_documents: int = SENTINEL,
        purge_schedule_for_temporary_data: int = SENTINEL,
        runtime_id: str = SENTINEL,
        **kwargs,
    ):
        """CloudAttachmentProperties

        :param archive_processed_documents: archive_processed_documents, defaults to None
        :type archive_processed_documents: bool, optional
        :param container_name: container_name, defaults to None
        :type container_name: str, optional
        :param container_purge_days: container_purge_days, defaults to None
        :type container_purge_days: int, optional
        :param container_purge_immediately: container_purge_immediately, defaults to None
        :type container_purge_immediately: bool, optional
        :param default_time_zone_for_account_schedules: default_time_zone_for_account_schedules, defaults to None
        :type default_time_zone_for_account_schedules: str, optional
        :param low_latency_warning_threshold: low_latency_warning_threshold, defaults to None
        :type low_latency_warning_threshold: int, optional
        :param partial_update: partial_update, defaults to None
        :type partial_update: bool, optional
        :param purge_schedule_for_components: purge_schedule_for_components, defaults to None
        :type purge_schedule_for_components: int, optional
        :param purge_schedule_for_logs: purge_schedule_for_logs, defaults to None
        :type purge_schedule_for_logs: int, optional
        :param purge_schedule_for_processed_documents: purge_schedule_for_processed_documents, defaults to None
        :type purge_schedule_for_processed_documents: int, optional
        :param purge_schedule_for_temporary_data: purge_schedule_for_temporary_data, defaults to None
        :type purge_schedule_for_temporary_data: int, optional
        :param runtime_id: runtime_id, defaults to None
        :type runtime_id: str, optional
        """
        if archive_processed_documents is not SENTINEL:
            self.archive_processed_documents = archive_processed_documents
        if container_name is not SENTINEL:
            self.container_name = container_name
        if container_purge_days is not SENTINEL:
            self.container_purge_days = container_purge_days
        if container_purge_immediately is not SENTINEL:
            self.container_purge_immediately = container_purge_immediately
        if default_time_zone_for_account_schedules is not SENTINEL:
            self.default_time_zone_for_account_schedules = (
                default_time_zone_for_account_schedules
            )
        if low_latency_warning_threshold is not SENTINEL:
            self.low_latency_warning_threshold = low_latency_warning_threshold
        if partial_update is not SENTINEL:
            self.partial_update = partial_update
        if purge_schedule_for_components is not SENTINEL:
            self.purge_schedule_for_components = purge_schedule_for_components
        if purge_schedule_for_logs is not SENTINEL:
            self.purge_schedule_for_logs = purge_schedule_for_logs
        if purge_schedule_for_processed_documents is not SENTINEL:
            self.purge_schedule_for_processed_documents = (
                purge_schedule_for_processed_documents
            )
        if purge_schedule_for_temporary_data is not SENTINEL:
            self.purge_schedule_for_temporary_data = purge_schedule_for_temporary_data
        if runtime_id is not SENTINEL:
            self.runtime_id = runtime_id
        self._kwargs = kwargs
