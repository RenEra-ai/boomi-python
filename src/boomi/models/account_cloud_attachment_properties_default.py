
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


class As2WorkloadDefault(Enum):
    """An enumeration representing different categories.

    :cvar GENERAL: "GENERAL"
    :vartype GENERAL: str
    :cvar LOWLATENCYDEBUG: "LOW_LATENCY_DEBUG"
    :vartype LOWLATENCYDEBUG: str
    """

    GENERAL = "GENERAL"
    LOWLATENCYDEBUG = "LOW_LATENCY_DEBUG"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, As2WorkloadDefault._member_map_.values()))


class FlowControlParallelProcessTypeOverrideDefault(Enum):
    """An enumeration representing different categories.

    :cvar NONE: "NONE"
    :vartype NONE: str
    :cvar THREADS: "THREADS"
    :vartype THREADS: str
    :cvar PROCESSES: "PROCESSES"
    :vartype PROCESSES: str
    """

    NONE = "NONE"
    THREADS = "THREADS"
    PROCESSES = "PROCESSES"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(
                lambda x: x.value,
                FlowControlParallelProcessTypeOverrideDefault._member_map_.values(),
            )
        )


class HttpWorkloadDefault(Enum):
    """An enumeration representing different categories.

    :cvar GENERAL: "GENERAL"
    :vartype GENERAL: str
    :cvar LOWLATENCYDEBUG: "LOW_LATENCY_DEBUG"
    :vartype LOWLATENCYDEBUG: str
    :cvar LOWLATENCY: "LOW_LATENCY"
    :vartype LOWLATENCY: str
    """

    GENERAL = "GENERAL"
    LOWLATENCYDEBUG = "LOW_LATENCY_DEBUG"
    LOWLATENCY = "LOW_LATENCY"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(map(lambda x: x.value, HttpWorkloadDefault._member_map_.values()))


@JsonMap(
    {
        "account_disk_usage": "accountDiskUsage",
        "as2_workload": "as2Workload",
        "atom_input_size": "atomInputSize",
        "atom_output_overflow_size": "atomOutputOverflowSize",
        "atom_working_overflow_size": "atomWorkingOverflowSize",
        "cloud_account_execution_limit": "cloudAccountExecutionLimit",
        "cloud_account_execution_warning_offset": "cloudAccountExecutionWarningOffset",
        "container_id": "containerId",
        "download_runnerlogs": "downloadRunnerlogs",
        "enable_account_data_archiving": "enableAccountDataArchiving",
        "enable_atom_worker_warmup": "enableAtomWorkerWarmup",
        "flow_control_parallel_process_type_override": "flowControlParallelProcessTypeOverride",
        "http_request_rate": "httpRequestRate",
        "http_workload": "httpWorkload",
        "listener_max_concurrent_executions": "listenerMaxConcurrentExecutions",
        "max_connector_track_docs": "maxConnectorTrackDocs",
        "min_numberof_atom_workers": "minNumberofAtomWorkers",
        "numberof_atom_workers": "numberofAtomWorkers",
        "queue_commit_batch_limit": "queueCommitBatchLimit",
        "queue_incoming_message_rate_limit": "queueIncomingMessageRateLimit",
        "queue_max_batch_size": "queueMaxBatchSize",
        "queue_max_doc_size": "queueMaxDocSize",
        "queue_msg_throttle_rate": "queueMsgThrottleRate",
        "queue_use_file_persistence": "queueUseFilePersistence",
        "test_mode_max_doc_bytes": "testModeMaxDocBytes",
        "test_mode_max_docs": "testModeMaxDocs",
        "worker_elastic_scaling_threshold": "workerElasticScalingThreshold",
        "worker_max_execution_time": "workerMaxExecutionTime",
        "worker_max_general_execution_time": "workerMaxGeneralExecutionTime",
        "worker_max_queued_executions": "workerMaxQueuedExecutions",
        "worker_max_running_executions": "workerMaxRunningExecutions",
        "worker_queued_execution_timeout": "workerQueuedExecutionTimeout",
    }
)
class AccountCloudAttachmentPropertiesDefault(BaseModel):
    """AccountCloudAttachmentPropertiesDefault

    :param account_disk_usage: account_disk_usage, defaults to None
    :type account_disk_usage: int, optional
    :param as2_workload: as2_workload, defaults to None
    :type as2_workload: As2WorkloadDefault, optional
    :param atom_input_size: atom_input_size, defaults to None
    :type atom_input_size: int, optional
    :param atom_output_overflow_size: atom_output_overflow_size, defaults to None
    :type atom_output_overflow_size: int, optional
    :param atom_working_overflow_size: atom_working_overflow_size, defaults to None
    :type atom_working_overflow_size: int, optional
    :param cloud_account_execution_limit: cloud_account_execution_limit, defaults to None
    :type cloud_account_execution_limit: int, optional
    :param cloud_account_execution_warning_offset: cloud_account_execution_warning_offset, defaults to None
    :type cloud_account_execution_warning_offset: int, optional
    :param container_id: container_id, defaults to None
    :type container_id: str, optional
    :param download_runnerlogs: download_runnerlogs, defaults to None
    :type download_runnerlogs: bool, optional
    :param enable_account_data_archiving: enable_account_data_archiving, defaults to None
    :type enable_account_data_archiving: bool, optional
    :param enable_atom_worker_warmup: enable_atom_worker_warmup, defaults to None
    :type enable_atom_worker_warmup: bool, optional
    :param flow_control_parallel_process_type_override: flow_control_parallel_process_type_override, defaults to None
    :type flow_control_parallel_process_type_override: FlowControlParallelProcessTypeOverrideDefault, optional
    :param http_request_rate: http_request_rate, defaults to None
    :type http_request_rate: int, optional
    :param http_workload: http_workload, defaults to None
    :type http_workload: HttpWorkloadDefault, optional
    :param listener_max_concurrent_executions: listener_max_concurrent_executions, defaults to None
    :type listener_max_concurrent_executions: int, optional
    :param max_connector_track_docs: max_connector_track_docs, defaults to None
    :type max_connector_track_docs: int, optional
    :param min_numberof_atom_workers: min_numberof_atom_workers, defaults to None
    :type min_numberof_atom_workers: int, optional
    :param numberof_atom_workers: numberof_atom_workers, defaults to None
    :type numberof_atom_workers: int, optional
    :param queue_commit_batch_limit: queue_commit_batch_limit, defaults to None
    :type queue_commit_batch_limit: int, optional
    :param queue_incoming_message_rate_limit: queue_incoming_message_rate_limit, defaults to None
    :type queue_incoming_message_rate_limit: int, optional
    :param queue_max_batch_size: queue_max_batch_size, defaults to None
    :type queue_max_batch_size: int, optional
    :param queue_max_doc_size: queue_max_doc_size, defaults to None
    :type queue_max_doc_size: int, optional
    :param queue_msg_throttle_rate: queue_msg_throttle_rate, defaults to None
    :type queue_msg_throttle_rate: int, optional
    :param queue_use_file_persistence: queue_use_file_persistence, defaults to None
    :type queue_use_file_persistence: bool, optional
    :param test_mode_max_doc_bytes: test_mode_max_doc_bytes, defaults to None
    :type test_mode_max_doc_bytes: int, optional
    :param test_mode_max_docs: test_mode_max_docs, defaults to None
    :type test_mode_max_docs: int, optional
    :param worker_elastic_scaling_threshold: worker_elastic_scaling_threshold, defaults to None
    :type worker_elastic_scaling_threshold: int, optional
    :param worker_max_execution_time: worker_max_execution_time, defaults to None
    :type worker_max_execution_time: int, optional
    :param worker_max_general_execution_time: worker_max_general_execution_time, defaults to None
    :type worker_max_general_execution_time: int, optional
    :param worker_max_queued_executions: worker_max_queued_executions, defaults to None
    :type worker_max_queued_executions: int, optional
    :param worker_max_running_executions: worker_max_running_executions, defaults to None
    :type worker_max_running_executions: int, optional
    :param worker_queued_execution_timeout: worker_queued_execution_timeout, defaults to None
    :type worker_queued_execution_timeout: int, optional
    """

    def __init__(
        self,
        account_disk_usage: int = SENTINEL,
        as2_workload: As2WorkloadDefault = SENTINEL,
        atom_input_size: int = SENTINEL,
        atom_output_overflow_size: int = SENTINEL,
        atom_working_overflow_size: int = SENTINEL,
        cloud_account_execution_limit: int = SENTINEL,
        cloud_account_execution_warning_offset: int = SENTINEL,
        container_id: str = SENTINEL,
        download_runnerlogs: bool = SENTINEL,
        enable_account_data_archiving: bool = SENTINEL,
        enable_atom_worker_warmup: bool = SENTINEL,
        flow_control_parallel_process_type_override: FlowControlParallelProcessTypeOverrideDefault = SENTINEL,
        http_request_rate: int = SENTINEL,
        http_workload: HttpWorkloadDefault = SENTINEL,
        listener_max_concurrent_executions: int = SENTINEL,
        max_connector_track_docs: int = SENTINEL,
        min_numberof_atom_workers: int = SENTINEL,
        numberof_atom_workers: int = SENTINEL,
        queue_commit_batch_limit: int = SENTINEL,
        queue_incoming_message_rate_limit: int = SENTINEL,
        queue_max_batch_size: int = SENTINEL,
        queue_max_doc_size: int = SENTINEL,
        queue_msg_throttle_rate: int = SENTINEL,
        queue_use_file_persistence: bool = SENTINEL,
        test_mode_max_doc_bytes: int = SENTINEL,
        test_mode_max_docs: int = SENTINEL,
        worker_elastic_scaling_threshold: int = SENTINEL,
        worker_max_execution_time: int = SENTINEL,
        worker_max_general_execution_time: int = SENTINEL,
        worker_max_queued_executions: int = SENTINEL,
        worker_max_running_executions: int = SENTINEL,
        worker_queued_execution_timeout: int = SENTINEL,
        **kwargs
    ):
        """AccountCloudAttachmentPropertiesDefault

        :param account_disk_usage: account_disk_usage, defaults to None
        :type account_disk_usage: int, optional
        :param as2_workload: as2_workload, defaults to None
        :type as2_workload: As2WorkloadDefault, optional
        :param atom_input_size: atom_input_size, defaults to None
        :type atom_input_size: int, optional
        :param atom_output_overflow_size: atom_output_overflow_size, defaults to None
        :type atom_output_overflow_size: int, optional
        :param atom_working_overflow_size: atom_working_overflow_size, defaults to None
        :type atom_working_overflow_size: int, optional
        :param cloud_account_execution_limit: cloud_account_execution_limit, defaults to None
        :type cloud_account_execution_limit: int, optional
        :param cloud_account_execution_warning_offset: cloud_account_execution_warning_offset, defaults to None
        :type cloud_account_execution_warning_offset: int, optional
        :param container_id: container_id, defaults to None
        :type container_id: str, optional
        :param download_runnerlogs: download_runnerlogs, defaults to None
        :type download_runnerlogs: bool, optional
        :param enable_account_data_archiving: enable_account_data_archiving, defaults to None
        :type enable_account_data_archiving: bool, optional
        :param enable_atom_worker_warmup: enable_atom_worker_warmup, defaults to None
        :type enable_atom_worker_warmup: bool, optional
        :param flow_control_parallel_process_type_override: flow_control_parallel_process_type_override, defaults to None
        :type flow_control_parallel_process_type_override: FlowControlParallelProcessTypeOverrideDefault, optional
        :param http_request_rate: http_request_rate, defaults to None
        :type http_request_rate: int, optional
        :param http_workload: http_workload, defaults to None
        :type http_workload: HttpWorkloadDefault, optional
        :param listener_max_concurrent_executions: listener_max_concurrent_executions, defaults to None
        :type listener_max_concurrent_executions: int, optional
        :param max_connector_track_docs: max_connector_track_docs, defaults to None
        :type max_connector_track_docs: int, optional
        :param min_numberof_atom_workers: min_numberof_atom_workers, defaults to None
        :type min_numberof_atom_workers: int, optional
        :param numberof_atom_workers: numberof_atom_workers, defaults to None
        :type numberof_atom_workers: int, optional
        :param queue_commit_batch_limit: queue_commit_batch_limit, defaults to None
        :type queue_commit_batch_limit: int, optional
        :param queue_incoming_message_rate_limit: queue_incoming_message_rate_limit, defaults to None
        :type queue_incoming_message_rate_limit: int, optional
        :param queue_max_batch_size: queue_max_batch_size, defaults to None
        :type queue_max_batch_size: int, optional
        :param queue_max_doc_size: queue_max_doc_size, defaults to None
        :type queue_max_doc_size: int, optional
        :param queue_msg_throttle_rate: queue_msg_throttle_rate, defaults to None
        :type queue_msg_throttle_rate: int, optional
        :param queue_use_file_persistence: queue_use_file_persistence, defaults to None
        :type queue_use_file_persistence: bool, optional
        :param test_mode_max_doc_bytes: test_mode_max_doc_bytes, defaults to None
        :type test_mode_max_doc_bytes: int, optional
        :param test_mode_max_docs: test_mode_max_docs, defaults to None
        :type test_mode_max_docs: int, optional
        :param worker_elastic_scaling_threshold: worker_elastic_scaling_threshold, defaults to None
        :type worker_elastic_scaling_threshold: int, optional
        :param worker_max_execution_time: worker_max_execution_time, defaults to None
        :type worker_max_execution_time: int, optional
        :param worker_max_general_execution_time: worker_max_general_execution_time, defaults to None
        :type worker_max_general_execution_time: int, optional
        :param worker_max_queued_executions: worker_max_queued_executions, defaults to None
        :type worker_max_queued_executions: int, optional
        :param worker_max_running_executions: worker_max_running_executions, defaults to None
        :type worker_max_running_executions: int, optional
        :param worker_queued_execution_timeout: worker_queued_execution_timeout, defaults to None
        :type worker_queued_execution_timeout: int, optional
        """
        if account_disk_usage is not SENTINEL:
            self.account_disk_usage = account_disk_usage
        if as2_workload is not SENTINEL:
            self.as2_workload = self._enum_matching(
                as2_workload, As2WorkloadDefault.list(), "as2_workload"
            )
        if atom_input_size is not SENTINEL:
            self.atom_input_size = atom_input_size
        if atom_output_overflow_size is not SENTINEL:
            self.atom_output_overflow_size = atom_output_overflow_size
        if atom_working_overflow_size is not SENTINEL:
            self.atom_working_overflow_size = atom_working_overflow_size
        if cloud_account_execution_limit is not SENTINEL:
            self.cloud_account_execution_limit = cloud_account_execution_limit
        if cloud_account_execution_warning_offset is not SENTINEL:
            self.cloud_account_execution_warning_offset = (
                cloud_account_execution_warning_offset
            )
        if container_id is not SENTINEL:
            self.container_id = container_id
        if download_runnerlogs is not SENTINEL:
            self.download_runnerlogs = download_runnerlogs
        if enable_account_data_archiving is not SENTINEL:
            self.enable_account_data_archiving = enable_account_data_archiving
        if enable_atom_worker_warmup is not SENTINEL:
            self.enable_atom_worker_warmup = enable_atom_worker_warmup
        if flow_control_parallel_process_type_override is not SENTINEL:
            self.flow_control_parallel_process_type_override = self._enum_matching(
                flow_control_parallel_process_type_override,
                FlowControlParallelProcessTypeOverrideDefault.list(),
                "flow_control_parallel_process_type_override",
            )
        if http_request_rate is not SENTINEL:
            self.http_request_rate = http_request_rate
        if http_workload is not SENTINEL:
            self.http_workload = self._enum_matching(
                http_workload, HttpWorkloadDefault.list(), "http_workload"
            )
        if listener_max_concurrent_executions is not SENTINEL:
            self.listener_max_concurrent_executions = listener_max_concurrent_executions
        if max_connector_track_docs is not SENTINEL:
            self.max_connector_track_docs = max_connector_track_docs
        if min_numberof_atom_workers is not SENTINEL:
            self.min_numberof_atom_workers = min_numberof_atom_workers
        if numberof_atom_workers is not SENTINEL:
            self.numberof_atom_workers = numberof_atom_workers
        if queue_commit_batch_limit is not SENTINEL:
            self.queue_commit_batch_limit = queue_commit_batch_limit
        if queue_incoming_message_rate_limit is not SENTINEL:
            self.queue_incoming_message_rate_limit = queue_incoming_message_rate_limit
        if queue_max_batch_size is not SENTINEL:
            self.queue_max_batch_size = queue_max_batch_size
        if queue_max_doc_size is not SENTINEL:
            self.queue_max_doc_size = queue_max_doc_size
        if queue_msg_throttle_rate is not SENTINEL:
            self.queue_msg_throttle_rate = queue_msg_throttle_rate
        if queue_use_file_persistence is not SENTINEL:
            self.queue_use_file_persistence = queue_use_file_persistence
        if test_mode_max_doc_bytes is not SENTINEL:
            self.test_mode_max_doc_bytes = test_mode_max_doc_bytes
        if test_mode_max_docs is not SENTINEL:
            self.test_mode_max_docs = test_mode_max_docs
        if worker_elastic_scaling_threshold is not SENTINEL:
            self.worker_elastic_scaling_threshold = worker_elastic_scaling_threshold
        if worker_max_execution_time is not SENTINEL:
            self.worker_max_execution_time = worker_max_execution_time
        if worker_max_general_execution_time is not SENTINEL:
            self.worker_max_general_execution_time = worker_max_general_execution_time
        if worker_max_queued_executions is not SENTINEL:
            self.worker_max_queued_executions = worker_max_queued_executions
        if worker_max_running_executions is not SENTINEL:
            self.worker_max_running_executions = worker_max_running_executions
        if worker_queued_execution_timeout is not SENTINEL:
            self.worker_queued_execution_timeout = worker_queued_execution_timeout
        self._kwargs = kwargs
