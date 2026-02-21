
from enum import Enum
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


class ClusterNetworkTransportType(Enum):
    """An enumeration representing different categories.

    :cvar MULTICAST: "MULTICAST"
    :vartype MULTICAST: str
    :cvar UNICAST: "UNICAST"
    :vartype UNICAST: str
    """

    MULTICAST = "MULTICAST"
    UNICAST = "UNICAST"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, ClusterNetworkTransportType._member_map_.values())
        )


class DebugLogLevelThreshold(Enum):
    """An enumeration representing different categories.

    :cvar DEBUG: "DEBUG"
    :vartype DEBUG: str
    :cvar INFO: "INFO"
    :vartype INFO: str
    :cvar OFF: "OFF"
    :vartype OFF: str
    :cvar SEVERE: "SEVERE"
    :vartype SEVERE: str
    :cvar WARNING: "WARNING"
    :vartype WARNING: str
    """

    DEBUG = "DEBUG"
    INFO = "INFO"
    OFF = "OFF"
    SEVERE = "SEVERE"
    WARNING = "WARNING"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, DebugLogLevelThreshold._member_map_.values())
        )


class ExecuteProcessesAsForkedJvms(Enum):
    """An enumeration representing different categories.

    :cvar ELASTIC: "ELASTIC"
    :vartype ELASTIC: str
    :cvar MULTI_PROCESS: "MULTI_PROCESS"
    :vartype MULTI_PROCESS: str
    :cvar MULTI_THREAD: "MULTI_THREAD"
    :vartype MULTI_THREAD: str
    """

    ELASTIC = "ELASTIC"
    MULTI_PROCESS = "MULTI_PROCESS"
    MULTI_THREAD = "MULTI_THREAD"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, ExecuteProcessesAsForkedJvms._member_map_.values())
        )


class ListenerStartupMode(Enum):
    """An enumeration representing different categories.

    :cvar ALL: "ALL"
    :vartype ALL: str
    :cvar MULTITENANT_ONLY: "MULTITENANT_ONLY"
    :vartype MULTITENANT_ONLY: str
    :cvar NONE: "NONE"
    :vartype NONE: str
    :cvar EFFECTIVE_SINGLE_TENANT_ONLY: "EFFECTIVE_SINGLE_TENANT_ONLY"
    :vartype EFFECTIVE_SINGLE_TENANT_ONLY: str
    """

    ALL = "ALL"
    MULTITENANT_ONLY = "MULTITENANT_ONLY"
    NONE = "NONE"
    EFFECTIVE_SINGLE_TENANT_ONLY = "EFFECTIVE_SINGLE_TENANT_ONLY"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, ListenerStartupMode._member_map_.values())
        )


class SecurityPolicy(Enum):
    """An enumeration representing different categories.

    :cvar HIGH: "HIGH"
    :vartype HIGH: str
    :cvar LOW: "LOW"
    :vartype LOW: str
    :cvar CUSTOM: "CUSTOM"
    :vartype CUSTOM: str
    """

    HIGH = "HIGH"
    LOW = "LOW"
    CUSTOM = "CUSTOM"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, SecurityPolicy._member_map_.values())
        )


class StandardErrorLogLevel(Enum):
    """An enumeration representing different categories.

    :cvar OFF: "OFF"
    :vartype OFF: str
    :cvar WARNING: "WARNING"
    :vartype WARNING: str
    :cvar SEVERE: "SEVERE"
    :vartype SEVERE: str
    """

    OFF = "OFF"
    WARNING = "WARNING"
    SEVERE = "SEVERE"

    def list():
        """Lists all category values.

        :return: A list of all category values.
        :rtype: list
        """
        return list(
            map(lambda x: x.value, StandardErrorLogLevel._member_map_.values())
        )


@JsonMap(
    {
        "account_working_data_directories": "accountWorkingDataDirectories",
        "allow_browsing": "allowBrowsing",
        "allow_user_logs": "allowUserLogs",
        "archive_processed_documents": "archiveProcessedDocuments",
        "async_message_poller_timeout_for_cluster_scale_down": "asyncMessagePollerTimeoutForClusterScaleDown",
        "auto_restart_on_out_of_memory": "autoRestartOnOutOfMemory",
        "auto_restart_on_too_many_files_error": "autoRestartOnTooManyFilesError",
        "aws_secrets_manager": "awsSecretsManager",
        "aws_secrets_manager_region": "awsSecretsManagerRegion",
        "azure_secrets_manager": "azureSecretsManager",
        "clean_up_custom_script_engine_data_on_completion": "cleanUpCustomScriptEngineDataOnCompletion",
        "cloud_partition_replicas": "cloudPartitionReplicas",
        "cloud_partition_size": "cloudPartitionSize",
        "cluster_bootstrap_timeout": "clusterBootstrapTimeout",
        "cluster_network_bind_address": "clusterNetworkBindAddress",
        "cluster_network_transport_type": "clusterNetworkTransportType",
        "cluster_problem_automatic_delete_delay": "clusterProblemAutomaticDeleteDelay",
        "cluster_problem_automatic_shutdown_delay": "clusterProblemAutomaticShutdownDelay",
        "cluster_rolling_restart_percentage": "clusterRollingRestartPercentage",
        "compress_history_after_x_days": "compressHistoryAfterXDays",
        "connector_browsing_idle_timeout": "connectorBrowsingIdleTimeout",
        "connector_browsing_max_thread_count": "connectorBrowsingMaxThreadCount",
        "connector_browsing_maximum_browse_time": "connectorBrowsingMaximumBrowseTime",
        "connector_browsing_time_to_live": "connectorBrowsingTimeToLive",
        "connector_server_startup_timeout": "connectorServerStartupTimeout",
        "connector_trace_logging": "connectorTraceLogging",
        "container_force_restart": "containerForceRestart",
        "container_host_name": "containerHostName",
        "container_name": "containerName",
        "container_purge_days": "containerPurgeDays",
        "container_purge_immediately": "containerPurgeImmediately",
        "control_id_cache_idle_timeout": "controlIdCacheIdleTimeout",
        "control_id_cache_time_to_live": "controlIdCacheTimeToLive",
        "counter_file_lock_retry": "counterFileLockRetry",
        "counter_lock_retry_maximum_retries": "counterLockRetryMaximumRetries",
        "counter_lock_retry_wait_time": "counterLockRetryWaitTime",
        "customized_procbrowser_script_file_name": "customizedProcbrowserScriptFileName",
        "customized_procrunner_script_file_name": "customizedProcrunnerScriptFileName",
        "customized_procworker_script_file_name": "customizedProcworkerScriptFileName",
        "customized_restart_script_file_name": "customizedRestartScriptFileName",
        "debug_log_level_threshold": "debugLogLevelThreshold",
        "debug_logging": "debugLogging",
        "decommission_time_for_post_pause_sleep": "decommissionTimeForPostPauseSleep",
        "default_time_zone_for_account_schedules": "defaultTimeZoneForAccountSchedules",
        "disk_space_monitoring": "diskSpaceMonitoring",
        "disk_space_monitoring_account_auto_suspension": "diskSpaceMonitoringAccountAutoSuspension",
        "disk_space_monitoring_frequency": "diskSpaceMonitoringFrequency",
        "disk_space_monitoring_threads": "diskSpaceMonitoringThreads",
        "disk_space_monitoring_verbose_logging": "diskSpaceMonitoringVerboseLogging",
        "disk_space_warning_limit": "diskSpaceWarningLimit",
        "dump_to_file_when_exceeding_open_file_threshold": "dumpToFileWhenExceedingOpenFileThreshold",
        "early_stale_execution_worker_ttl_percentage": "earlyStaleExecutionWorkerTtlPercentage",
        "elastic_worker_directory_level": "elasticWorkerDirectoryLevel",
        "elastic_worker_metrics_polling_period": "elasticWorkerMetricsPollingPeriod",
        "execute_processes_as_forked_jvms": "executeProcessesAsForkedJvms",
        "execution_worker_idle_timeout": "executionWorkerIdleTimeout",
        "execution_worker_local_port_range": "executionWorkerLocalPortRange",
        "execution_worker_pending_updates_queue_size": "executionWorkerPendingUpdatesQueueSize",
        "execution_worker_startup_timeout": "executionWorkerStartupTimeout",
        "execution_worker_thread_pool_idle_timeout": "executionWorkerThreadPoolIdleTimeout",
        "execution_worker_time_to_live": "executionWorkerTimeToLive",
        "execution_workers_enabled": "executionWorkersEnabled",
        "external_hostname": "externalHostname",
        "force_restart_override_for_cluster_scale_down": "forceRestartOverrideForClusterScaleDown",
        "force_start_shared_web_server": "forceStartSharedWebServer",
        "generate_heap_dump_on_low_memory": "generateHeapDumpOnLowMemory",
        "https_protocols": "httpsProtocols",
        "initial_hosts_for_unicast": "initialHostsForUnicast",
        "jgroups_debug_logging": "jgroupsDebugLogging",
        "listener_startup_mode": "listenerStartupMode",
        "logger_queue_size": "loggerQueueSize",
        "logger_timeout": "loggerTimeout",
        "low_latency_warning_threshold": "lowLatencyWarningThreshold",
        "low_memory_mode_threshold": "lowMemoryModeThreshold",
        "low_remaining_open_files_threshold": "lowRemainingOpenFilesThreshold",
        "mapping_expand_child_elements_legacy": "mappingExpandChildElementsLegacy",
        "max_cached_control_ids": "maxCachedControlIds",
        "max_cached_transaction_keys": "maxCachedTransactionKeys",
        "max_document_elements_cache_size": "maxDocumentElementsCacheSize",
        "max_execution_threads_per_connector_browser": "maxExecutionThreadsPerConnectorBrowser",
        "max_execution_threads_per_execution_worker": "maxExecutionThreadsPerExecutionWorker",
        "max_execution_threads_per_forked_execution": "maxExecutionThreadsPerForkedExecution",
        "max_flow_control_units": "maxFlowControlUnits",
        "max_forked_execution_time_in_cloud": "maxForkedExecutionTimeInCloud",
        "max_number_of_active_batches_per_listener": "maxNumberOfActiveBatchesPerListener",
        "max_queued_executions_per_node": "maxQueuedExecutionsPerNode",
        "max_queued_forked_executions_per_node": "maxQueuedForkedExecutionsPerNode",
        "max_simultaneous_executions_per_node": "maxSimultaneousExecutionsPerNode",
        "max_simultaneous_forked_executions_per_node": "maxSimultaneousForkedExecutionsPerNode",
        "max_simultaneous_forked_jvms_per_node": "maxSimultaneousForkedJvmsPerNode",
        "max_size_for_update_operation": "maxSizeForUpdateOperation",
        "milliseconds_logging": "millisecondsLogging",
        "min_number_of_hosts_for_unicast_autodetect": "minNumberOfHostsForUnicastAutodetect",
        "monitor_number_of_open_files": "monitorNumberOfOpenFiles",
        "multicast_address": "multicastAddress",
        "multicast_port": "multicastPort",
        "persisted_connector_cache": "persistedConnectorCache",
        "process_execution_directory_level": "processExecutionDirectoryLevel",
        "processed_document_archive_directory": "processedDocumentArchiveDirectory",
        "proxy_user_id": "proxyUserId",
        "purge_manager": "purgeManager",
        "purge_manager_threads": "purgeManagerThreads",
        "purge_schedule_for_components": "purgeScheduleForComponents",
        "purge_schedule_for_logs": "purgeScheduleForLogs",
        "purge_schedule_for_processed_documents": "purgeScheduleForProcessedDocuments",
        "purge_schedule_for_temporary_data": "purgeScheduleForTemporaryData",
        "rolling_restart_force_timeout": "rollingRestartForceTimeout",
        "rolling_restart_next_in_line_timeout": "rollingRestartNextInLineTimeout",
        "runtime_data_directory_level": "runtimeDataDirectoryLevel",
        "runtime_pending_shutdown_delay": "runtimePendingShutdownDelay",
        "save_swagger_template_in_work_folder": "saveSwaggerTemplateInWorkFolder",
        "security_policy": "securityPolicy",
        "sequential_processing_of_custom_script_engine_data": "sequentialProcessingOfCustomScriptEngineData",
        "show_runtime_icon_in_system_tray": "showRuntimeIconInSystemTray",
        "ssl_debug_logging": "sslDebugLogging",
        "standard_error_log_level": "standardErrorLogLevel",
        "standard_output_and_error_logging": "standardOutputAndErrorLogging",
        "tcp_port_for_unicast": "tcpPortForUnicast",
        "threads_for_account_initialization": "threadsForAccountInitialization",
        "threads_for_account_initialization_during_starting_and_stopping_plugins": "threadsForAccountInitializationDuringStartingAndStoppingPlugins",
        "threads_for_recovering_executions_during_container_startup": "threadsForRecoveringExecutionsDuringContainerStartup",
        "threads_for_runtime_scheduling": "threadsForRuntimeScheduling",
        "threads_for_runtime_to_platform_messages": "threadsForRuntimeToPlatformMessages",
        "threads_for_runtime_to_platform_polling": "threadsForRuntimeToPlatformPolling",
        "threads_for_runtime_to_runtime_messages": "threadsForRuntimeToRuntimeMessages",
        "timeout_for_escalating_cluster_issue": "timeoutForEscalatingClusterIssue",
        "timeout_for_queued_executions_per_node": "timeoutForQueuedExecutionsPerNode",
        "timeout_for_queued_forked_executions_per_node": "timeoutForQueuedForkedExecutionsPerNode",
        "trace_logging": "traceLogging",
        "use_local_storage_for_runtime_assets": "useLocalStorageForRuntimeAssets",
        "worker_heartbeat_timeout": "workerHeartbeatTimeout",
        "working_data_local_storage_directory": "workingDataLocalStorageDirectory",
        "xml_entity_processing": "xmlEntityProcessing",
        "xml_external_entity_processing": "xmlExternalEntityProcessing",
    }
)
class StandardProperties(BaseModel):
    """StandardProperties

    :param account_working_data_directories: account_working_data_directories, defaults to None
    :type account_working_data_directories: str, optional
    :param allow_browsing: allow_browsing, defaults to None
    :type allow_browsing: bool, optional
    :param allow_user_logs: allow_user_logs, defaults to None
    :type allow_user_logs: bool, optional
    :param archive_processed_documents: archive_processed_documents, defaults to None
    :type archive_processed_documents: bool, optional
    :param async_message_poller_timeout_for_cluster_scale_down: async_message_poller_timeout_for_cluster_scale_down, defaults to None
    :type async_message_poller_timeout_for_cluster_scale_down: int, optional
    :param auto_restart_on_out_of_memory: auto_restart_on_out_of_memory, defaults to None
    :type auto_restart_on_out_of_memory: bool, optional
    :param auto_restart_on_too_many_files_error: auto_restart_on_too_many_files_error, defaults to None
    :type auto_restart_on_too_many_files_error: bool, optional
    :param aws_secrets_manager: aws_secrets_manager, defaults to None
    :type aws_secrets_manager: bool, optional
    :param aws_secrets_manager_region: aws_secrets_manager_region, defaults to None
    :type aws_secrets_manager_region: str, optional
    :param azure_secrets_manager: azure_secrets_manager, defaults to None
    :type azure_secrets_manager: bool, optional
    :param clean_up_custom_script_engine_data_on_completion: clean_up_custom_script_engine_data_on_completion, defaults to None
    :type clean_up_custom_script_engine_data_on_completion: bool, optional
    :param cloud_partition_replicas: cloud_partition_replicas, defaults to None
    :type cloud_partition_replicas: int, optional
    :param cloud_partition_size: cloud_partition_size, defaults to None
    :type cloud_partition_size: int, optional
    :param cluster_bootstrap_timeout: cluster_bootstrap_timeout, defaults to None
    :type cluster_bootstrap_timeout: int, optional
    :param cluster_network_bind_address: cluster_network_bind_address, defaults to None
    :type cluster_network_bind_address: str, optional
    :param cluster_network_transport_type: cluster_network_transport_type, defaults to None
    :type cluster_network_transport_type: ClusterNetworkTransportType, optional
    :param cluster_problem_automatic_delete_delay: cluster_problem_automatic_delete_delay, defaults to None
    :type cluster_problem_automatic_delete_delay: int, optional
    :param cluster_problem_automatic_shutdown_delay: cluster_problem_automatic_shutdown_delay, defaults to None
    :type cluster_problem_automatic_shutdown_delay: int, optional
    :param cluster_rolling_restart_percentage: cluster_rolling_restart_percentage, defaults to None
    :type cluster_rolling_restart_percentage: int, optional
    :param compress_history_after_x_days: compress_history_after_x_days, defaults to None
    :type compress_history_after_x_days: int, optional
    :param connector_browsing_idle_timeout: connector_browsing_idle_timeout, defaults to None
    :type connector_browsing_idle_timeout: int, optional
    :param connector_browsing_max_thread_count: connector_browsing_max_thread_count, defaults to None
    :type connector_browsing_max_thread_count: int, optional
    :param connector_browsing_maximum_browse_time: connector_browsing_maximum_browse_time, defaults to None
    :type connector_browsing_maximum_browse_time: int, optional
    :param connector_browsing_time_to_live: connector_browsing_time_to_live, defaults to None
    :type connector_browsing_time_to_live: int, optional
    :param connector_server_startup_timeout: connector_server_startup_timeout, defaults to None
    :type connector_server_startup_timeout: int, optional
    :param connector_trace_logging: connector_trace_logging, defaults to None
    :type connector_trace_logging: bool, optional
    :param container_force_restart: container_force_restart, defaults to None
    :type container_force_restart: bool, optional
    :param container_host_name: container_host_name, defaults to None
    :type container_host_name: str, optional
    :param container_name: container_name, defaults to None
    :type container_name: str, optional
    :param container_purge_days: container_purge_days, defaults to None
    :type container_purge_days: int, optional
    :param container_purge_immediately: container_purge_immediately, defaults to None
    :type container_purge_immediately: bool, optional
    :param control_id_cache_idle_timeout: control_id_cache_idle_timeout, defaults to None
    :type control_id_cache_idle_timeout: int, optional
    :param control_id_cache_time_to_live: control_id_cache_time_to_live, defaults to None
    :type control_id_cache_time_to_live: int, optional
    :param counter_file_lock_retry: counter_file_lock_retry, defaults to None
    :type counter_file_lock_retry: bool, optional
    :param counter_lock_retry_maximum_retries: counter_lock_retry_maximum_retries, defaults to None
    :type counter_lock_retry_maximum_retries: int, optional
    :param counter_lock_retry_wait_time: counter_lock_retry_wait_time, defaults to None
    :type counter_lock_retry_wait_time: int, optional
    :param customized_procbrowser_script_file_name: customized_procbrowser_script_file_name, defaults to None
    :type customized_procbrowser_script_file_name: str, optional
    :param customized_procrunner_script_file_name: customized_procrunner_script_file_name, defaults to None
    :type customized_procrunner_script_file_name: str, optional
    :param customized_procworker_script_file_name: customized_procworker_script_file_name, defaults to None
    :type customized_procworker_script_file_name: str, optional
    :param customized_restart_script_file_name: customized_restart_script_file_name, defaults to None
    :type customized_restart_script_file_name: str, optional
    :param debug_log_level_threshold: debug_log_level_threshold, defaults to None
    :type debug_log_level_threshold: DebugLogLevelThreshold, optional
    :param debug_logging: debug_logging, defaults to None
    :type debug_logging: bool, optional
    :param decommission_time_for_post_pause_sleep: decommission_time_for_post_pause_sleep, defaults to None
    :type decommission_time_for_post_pause_sleep: int, optional
    :param default_time_zone_for_account_schedules: default_time_zone_for_account_schedules, defaults to None
    :type default_time_zone_for_account_schedules: str, optional
    :param disk_space_monitoring: disk_space_monitoring, defaults to None
    :type disk_space_monitoring: bool, optional
    :param disk_space_monitoring_account_auto_suspension: disk_space_monitoring_account_auto_suspension, defaults to None
    :type disk_space_monitoring_account_auto_suspension: bool, optional
    :param disk_space_monitoring_frequency: disk_space_monitoring_frequency, defaults to None
    :type disk_space_monitoring_frequency: int, optional
    :param disk_space_monitoring_threads: disk_space_monitoring_threads, defaults to None
    :type disk_space_monitoring_threads: int, optional
    :param disk_space_monitoring_verbose_logging: disk_space_monitoring_verbose_logging, defaults to None
    :type disk_space_monitoring_verbose_logging: bool, optional
    :param disk_space_warning_limit: disk_space_warning_limit, defaults to None
    :type disk_space_warning_limit: int, optional
    :param dump_to_file_when_exceeding_open_file_threshold: dump_to_file_when_exceeding_open_file_threshold, defaults to None
    :type dump_to_file_when_exceeding_open_file_threshold: bool, optional
    :param early_stale_execution_worker_ttl_percentage: early_stale_execution_worker_ttl_percentage, defaults to None
    :type early_stale_execution_worker_ttl_percentage: int, optional
    :param elastic_worker_directory_level: elastic_worker_directory_level, defaults to None
    :type elastic_worker_directory_level: int, optional
    :param elastic_worker_metrics_polling_period: elastic_worker_metrics_polling_period, defaults to None
    :type elastic_worker_metrics_polling_period: int, optional
    :param execute_processes_as_forked_jvms: execute_processes_as_forked_jvms, defaults to None
    :type execute_processes_as_forked_jvms: ExecuteProcessesAsForkedJvms, optional
    :param execution_worker_idle_timeout: execution_worker_idle_timeout, defaults to None
    :type execution_worker_idle_timeout: int, optional
    :param execution_worker_local_port_range: execution_worker_local_port_range, defaults to None
    :type execution_worker_local_port_range: str, optional
    :param execution_worker_pending_updates_queue_size: execution_worker_pending_updates_queue_size, defaults to None
    :type execution_worker_pending_updates_queue_size: int, optional
    :param execution_worker_startup_timeout: execution_worker_startup_timeout, defaults to None
    :type execution_worker_startup_timeout: int, optional
    :param execution_worker_thread_pool_idle_timeout: execution_worker_thread_pool_idle_timeout, defaults to None
    :type execution_worker_thread_pool_idle_timeout: int, optional
    :param execution_worker_time_to_live: execution_worker_time_to_live, defaults to None
    :type execution_worker_time_to_live: int, optional
    :param execution_workers_enabled: execution_workers_enabled, defaults to None
    :type execution_workers_enabled: bool, optional
    :param external_hostname: external_hostname, defaults to None
    :type external_hostname: str, optional
    :param force_restart_override_for_cluster_scale_down: force_restart_override_for_cluster_scale_down, defaults to None
    :type force_restart_override_for_cluster_scale_down: bool, optional
    :param force_start_shared_web_server: force_start_shared_web_server, defaults to None
    :type force_start_shared_web_server: bool, optional
    :param generate_heap_dump_on_low_memory: generate_heap_dump_on_low_memory, defaults to None
    :type generate_heap_dump_on_low_memory: bool, optional
    :param https_protocols: https_protocols, defaults to None
    :type https_protocols: str, optional
    :param initial_hosts_for_unicast: initial_hosts_for_unicast, defaults to None
    :type initial_hosts_for_unicast: str, optional
    :param jgroups_debug_logging: jgroups_debug_logging, defaults to None
    :type jgroups_debug_logging: bool, optional
    :param listener_startup_mode: listener_startup_mode, defaults to None
    :type listener_startup_mode: ListenerStartupMode, optional
    :param logger_queue_size: logger_queue_size, defaults to None
    :type logger_queue_size: int, optional
    :param logger_timeout: logger_timeout, defaults to None
    :type logger_timeout: int, optional
    :param low_latency_warning_threshold: low_latency_warning_threshold, defaults to None
    :type low_latency_warning_threshold: int, optional
    :param low_memory_mode_threshold: low_memory_mode_threshold, defaults to None
    :type low_memory_mode_threshold: str, optional
    :param low_remaining_open_files_threshold: low_remaining_open_files_threshold, defaults to None
    :type low_remaining_open_files_threshold: str, optional
    :param mapping_expand_child_elements_legacy: mapping_expand_child_elements_legacy, defaults to None
    :type mapping_expand_child_elements_legacy: bool, optional
    :param max_cached_control_ids: max_cached_control_ids, defaults to None
    :type max_cached_control_ids: int, optional
    :param max_cached_transaction_keys: max_cached_transaction_keys, defaults to None
    :type max_cached_transaction_keys: int, optional
    :param max_document_elements_cache_size: max_document_elements_cache_size, defaults to None
    :type max_document_elements_cache_size: int, optional
    :param max_execution_threads_per_connector_browser: max_execution_threads_per_connector_browser, defaults to None
    :type max_execution_threads_per_connector_browser: int, optional
    :param max_execution_threads_per_execution_worker: max_execution_threads_per_execution_worker, defaults to None
    :type max_execution_threads_per_execution_worker: int, optional
    :param max_execution_threads_per_forked_execution: max_execution_threads_per_forked_execution, defaults to None
    :type max_execution_threads_per_forked_execution: int, optional
    :param max_flow_control_units: max_flow_control_units, defaults to None
    :type max_flow_control_units: int, optional
    :param max_forked_execution_time_in_cloud: max_forked_execution_time_in_cloud, defaults to None
    :type max_forked_execution_time_in_cloud: int, optional
    :param max_number_of_active_batches_per_listener: max_number_of_active_batches_per_listener, defaults to None
    :type max_number_of_active_batches_per_listener: int, optional
    :param max_queued_executions_per_node: max_queued_executions_per_node, defaults to None
    :type max_queued_executions_per_node: int, optional
    :param max_queued_forked_executions_per_node: max_queued_forked_executions_per_node, defaults to None
    :type max_queued_forked_executions_per_node: int, optional
    :param max_simultaneous_executions_per_node: max_simultaneous_executions_per_node, defaults to None
    :type max_simultaneous_executions_per_node: int, optional
    :param max_simultaneous_forked_executions_per_node: max_simultaneous_forked_executions_per_node, defaults to None
    :type max_simultaneous_forked_executions_per_node: int, optional
    :param max_simultaneous_forked_jvms_per_node: max_simultaneous_forked_jvms_per_node, defaults to None
    :type max_simultaneous_forked_jvms_per_node: int, optional
    :param max_size_for_update_operation: max_size_for_update_operation, defaults to None
    :type max_size_for_update_operation: int, optional
    :param milliseconds_logging: milliseconds_logging, defaults to None
    :type milliseconds_logging: bool, optional
    :param min_number_of_hosts_for_unicast_autodetect: min_number_of_hosts_for_unicast_autodetect, defaults to None
    :type min_number_of_hosts_for_unicast_autodetect: int, optional
    :param monitor_number_of_open_files: monitor_number_of_open_files, defaults to None
    :type monitor_number_of_open_files: bool, optional
    :param multicast_address: multicast_address, defaults to None
    :type multicast_address: str, optional
    :param multicast_port: multicast_port, defaults to None
    :type multicast_port: int, optional
    :param persisted_connector_cache: persisted_connector_cache, defaults to None
    :type persisted_connector_cache: bool, optional
    :param process_execution_directory_level: process_execution_directory_level, defaults to None
    :type process_execution_directory_level: int, optional
    :param processed_document_archive_directory: processed_document_archive_directory, defaults to None
    :type processed_document_archive_directory: str, optional
    :param proxy_user_id: proxy_user_id, defaults to None
    :type proxy_user_id: str, optional
    :param purge_manager: purge_manager, defaults to None
    :type purge_manager: bool, optional
    :param purge_manager_threads: purge_manager_threads, defaults to None
    :type purge_manager_threads: int, optional
    :param purge_schedule_for_components: purge_schedule_for_components, defaults to None
    :type purge_schedule_for_components: str, optional
    :param purge_schedule_for_logs: purge_schedule_for_logs, defaults to None
    :type purge_schedule_for_logs: str, optional
    :param purge_schedule_for_processed_documents: purge_schedule_for_processed_documents, defaults to None
    :type purge_schedule_for_processed_documents: str, optional
    :param purge_schedule_for_temporary_data: purge_schedule_for_temporary_data, defaults to None
    :type purge_schedule_for_temporary_data: str, optional
    :param rolling_restart_force_timeout: rolling_restart_force_timeout, defaults to None
    :type rolling_restart_force_timeout: int, optional
    :param rolling_restart_next_in_line_timeout: rolling_restart_next_in_line_timeout, defaults to None
    :type rolling_restart_next_in_line_timeout: int, optional
    :param runtime_data_directory_level: runtime_data_directory_level, defaults to None
    :type runtime_data_directory_level: int, optional
    :param runtime_pending_shutdown_delay: runtime_pending_shutdown_delay, defaults to None
    :type runtime_pending_shutdown_delay: int, optional
    :param save_swagger_template_in_work_folder: save_swagger_template_in_work_folder, defaults to None
    :type save_swagger_template_in_work_folder: bool, optional
    :param security_policy: security_policy, defaults to None
    :type security_policy: SecurityPolicy, optional
    :param sequential_processing_of_custom_script_engine_data: sequential_processing_of_custom_script_engine_data, defaults to None
    :type sequential_processing_of_custom_script_engine_data: bool, optional
    :param show_runtime_icon_in_system_tray: show_runtime_icon_in_system_tray, defaults to None
    :type show_runtime_icon_in_system_tray: bool, optional
    :param ssl_debug_logging: ssl_debug_logging, defaults to None
    :type ssl_debug_logging: bool, optional
    :param standard_error_log_level: standard_error_log_level, defaults to None
    :type standard_error_log_level: StandardErrorLogLevel, optional
    :param standard_output_and_error_logging: standard_output_and_error_logging, defaults to None
    :type standard_output_and_error_logging: bool, optional
    :param tcp_port_for_unicast: tcp_port_for_unicast, defaults to None
    :type tcp_port_for_unicast: int, optional
    :param threads_for_account_initialization: threads_for_account_initialization, defaults to None
    :type threads_for_account_initialization: int, optional
    :param threads_for_account_initialization_during_starting_and_stopping_plugins: threads_for_account_initialization_during_starting_and_stopping_plugins, defaults to None
    :type threads_for_account_initialization_during_starting_and_stopping_plugins: int, optional
    :param threads_for_recovering_executions_during_container_startup: threads_for_recovering_executions_during_container_startup, defaults to None
    :type threads_for_recovering_executions_during_container_startup: int, optional
    :param threads_for_runtime_scheduling: threads_for_runtime_scheduling, defaults to None
    :type threads_for_runtime_scheduling: int, optional
    :param threads_for_runtime_to_platform_messages: threads_for_runtime_to_platform_messages, defaults to None
    :type threads_for_runtime_to_platform_messages: int, optional
    :param threads_for_runtime_to_platform_polling: threads_for_runtime_to_platform_polling, defaults to None
    :type threads_for_runtime_to_platform_polling: int, optional
    :param threads_for_runtime_to_runtime_messages: threads_for_runtime_to_runtime_messages, defaults to None
    :type threads_for_runtime_to_runtime_messages: int, optional
    :param timeout_for_escalating_cluster_issue: timeout_for_escalating_cluster_issue, defaults to None
    :type timeout_for_escalating_cluster_issue: int, optional
    :param timeout_for_queued_executions_per_node: timeout_for_queued_executions_per_node, defaults to None
    :type timeout_for_queued_executions_per_node: int, optional
    :param timeout_for_queued_forked_executions_per_node: timeout_for_queued_forked_executions_per_node, defaults to None
    :type timeout_for_queued_forked_executions_per_node: int, optional
    :param trace_logging: trace_logging, defaults to None
    :type trace_logging: bool, optional
    :param use_local_storage_for_runtime_assets: use_local_storage_for_runtime_assets, defaults to None
    :type use_local_storage_for_runtime_assets: bool, optional
    :param worker_heartbeat_timeout: worker_heartbeat_timeout, defaults to None
    :type worker_heartbeat_timeout: int, optional
    :param working_data_local_storage_directory: working_data_local_storage_directory, defaults to None
    :type working_data_local_storage_directory: str, optional
    :param xml_entity_processing: xml_entity_processing, defaults to None
    :type xml_entity_processing: bool, optional
    :param xml_external_entity_processing: xml_external_entity_processing, defaults to None
    :type xml_external_entity_processing: bool, optional
    """

    def __init__(
        self,
        account_working_data_directories: str = SENTINEL,
        allow_browsing: bool = SENTINEL,
        allow_user_logs: bool = SENTINEL,
        archive_processed_documents: bool = SENTINEL,
        async_message_poller_timeout_for_cluster_scale_down: int = SENTINEL,
        auto_restart_on_out_of_memory: bool = SENTINEL,
        auto_restart_on_too_many_files_error: bool = SENTINEL,
        aws_secrets_manager: bool = SENTINEL,
        aws_secrets_manager_region: str = SENTINEL,
        azure_secrets_manager: bool = SENTINEL,
        clean_up_custom_script_engine_data_on_completion: bool = SENTINEL,
        cloud_partition_replicas: int = SENTINEL,
        cloud_partition_size: int = SENTINEL,
        cluster_bootstrap_timeout: int = SENTINEL,
        cluster_network_bind_address: str = SENTINEL,
        cluster_network_transport_type: ClusterNetworkTransportType = SENTINEL,
        cluster_problem_automatic_delete_delay: int = SENTINEL,
        cluster_problem_automatic_shutdown_delay: int = SENTINEL,
        cluster_rolling_restart_percentage: int = SENTINEL,
        compress_history_after_x_days: int = SENTINEL,
        connector_browsing_idle_timeout: int = SENTINEL,
        connector_browsing_max_thread_count: int = SENTINEL,
        connector_browsing_maximum_browse_time: int = SENTINEL,
        connector_browsing_time_to_live: int = SENTINEL,
        connector_server_startup_timeout: int = SENTINEL,
        connector_trace_logging: bool = SENTINEL,
        container_force_restart: bool = SENTINEL,
        container_host_name: str = SENTINEL,
        container_name: str = SENTINEL,
        container_purge_days: int = SENTINEL,
        container_purge_immediately: bool = SENTINEL,
        control_id_cache_idle_timeout: int = SENTINEL,
        control_id_cache_time_to_live: int = SENTINEL,
        counter_file_lock_retry: bool = SENTINEL,
        counter_lock_retry_maximum_retries: int = SENTINEL,
        counter_lock_retry_wait_time: int = SENTINEL,
        customized_procbrowser_script_file_name: str = SENTINEL,
        customized_procrunner_script_file_name: str = SENTINEL,
        customized_procworker_script_file_name: str = SENTINEL,
        customized_restart_script_file_name: str = SENTINEL,
        debug_log_level_threshold: DebugLogLevelThreshold = SENTINEL,
        debug_logging: bool = SENTINEL,
        decommission_time_for_post_pause_sleep: int = SENTINEL,
        default_time_zone_for_account_schedules: str = SENTINEL,
        disk_space_monitoring: bool = SENTINEL,
        disk_space_monitoring_account_auto_suspension: bool = SENTINEL,
        disk_space_monitoring_frequency: int = SENTINEL,
        disk_space_monitoring_threads: int = SENTINEL,
        disk_space_monitoring_verbose_logging: bool = SENTINEL,
        disk_space_warning_limit: int = SENTINEL,
        dump_to_file_when_exceeding_open_file_threshold: bool = SENTINEL,
        early_stale_execution_worker_ttl_percentage: int = SENTINEL,
        elastic_worker_directory_level: int = SENTINEL,
        elastic_worker_metrics_polling_period: int = SENTINEL,
        execute_processes_as_forked_jvms: ExecuteProcessesAsForkedJvms = SENTINEL,
        execution_worker_idle_timeout: int = SENTINEL,
        execution_worker_local_port_range: str = SENTINEL,
        execution_worker_pending_updates_queue_size: int = SENTINEL,
        execution_worker_startup_timeout: int = SENTINEL,
        execution_worker_thread_pool_idle_timeout: int = SENTINEL,
        execution_worker_time_to_live: int = SENTINEL,
        execution_workers_enabled: bool = SENTINEL,
        external_hostname: str = SENTINEL,
        force_restart_override_for_cluster_scale_down: bool = SENTINEL,
        force_start_shared_web_server: bool = SENTINEL,
        generate_heap_dump_on_low_memory: bool = SENTINEL,
        https_protocols: str = SENTINEL,
        initial_hosts_for_unicast: str = SENTINEL,
        jgroups_debug_logging: bool = SENTINEL,
        listener_startup_mode: ListenerStartupMode = SENTINEL,
        logger_queue_size: int = SENTINEL,
        logger_timeout: int = SENTINEL,
        low_latency_warning_threshold: int = SENTINEL,
        low_memory_mode_threshold: str = SENTINEL,
        low_remaining_open_files_threshold: str = SENTINEL,
        mapping_expand_child_elements_legacy: bool = SENTINEL,
        max_cached_control_ids: int = SENTINEL,
        max_cached_transaction_keys: int = SENTINEL,
        max_document_elements_cache_size: int = SENTINEL,
        max_execution_threads_per_connector_browser: int = SENTINEL,
        max_execution_threads_per_execution_worker: int = SENTINEL,
        max_execution_threads_per_forked_execution: int = SENTINEL,
        max_flow_control_units: int = SENTINEL,
        max_forked_execution_time_in_cloud: int = SENTINEL,
        max_number_of_active_batches_per_listener: int = SENTINEL,
        max_queued_executions_per_node: int = SENTINEL,
        max_queued_forked_executions_per_node: int = SENTINEL,
        max_simultaneous_executions_per_node: int = SENTINEL,
        max_simultaneous_forked_executions_per_node: int = SENTINEL,
        max_simultaneous_forked_jvms_per_node: int = SENTINEL,
        max_size_for_update_operation: int = SENTINEL,
        milliseconds_logging: bool = SENTINEL,
        min_number_of_hosts_for_unicast_autodetect: int = SENTINEL,
        monitor_number_of_open_files: bool = SENTINEL,
        multicast_address: str = SENTINEL,
        multicast_port: int = SENTINEL,
        persisted_connector_cache: bool = SENTINEL,
        process_execution_directory_level: int = SENTINEL,
        processed_document_archive_directory: str = SENTINEL,
        proxy_user_id: str = SENTINEL,
        purge_manager: bool = SENTINEL,
        purge_manager_threads: int = SENTINEL,
        purge_schedule_for_components: str = SENTINEL,
        purge_schedule_for_logs: str = SENTINEL,
        purge_schedule_for_processed_documents: str = SENTINEL,
        purge_schedule_for_temporary_data: str = SENTINEL,
        rolling_restart_force_timeout: int = SENTINEL,
        rolling_restart_next_in_line_timeout: int = SENTINEL,
        runtime_data_directory_level: int = SENTINEL,
        runtime_pending_shutdown_delay: int = SENTINEL,
        save_swagger_template_in_work_folder: bool = SENTINEL,
        security_policy: SecurityPolicy = SENTINEL,
        sequential_processing_of_custom_script_engine_data: bool = SENTINEL,
        show_runtime_icon_in_system_tray: bool = SENTINEL,
        ssl_debug_logging: bool = SENTINEL,
        standard_error_log_level: StandardErrorLogLevel = SENTINEL,
        standard_output_and_error_logging: bool = SENTINEL,
        tcp_port_for_unicast: int = SENTINEL,
        threads_for_account_initialization: int = SENTINEL,
        threads_for_account_initialization_during_starting_and_stopping_plugins: int = SENTINEL,
        threads_for_recovering_executions_during_container_startup: int = SENTINEL,
        threads_for_runtime_scheduling: int = SENTINEL,
        threads_for_runtime_to_platform_messages: int = SENTINEL,
        threads_for_runtime_to_platform_polling: int = SENTINEL,
        threads_for_runtime_to_runtime_messages: int = SENTINEL,
        timeout_for_escalating_cluster_issue: int = SENTINEL,
        timeout_for_queued_executions_per_node: int = SENTINEL,
        timeout_for_queued_forked_executions_per_node: int = SENTINEL,
        trace_logging: bool = SENTINEL,
        use_local_storage_for_runtime_assets: bool = SENTINEL,
        worker_heartbeat_timeout: int = SENTINEL,
        working_data_local_storage_directory: str = SENTINEL,
        xml_entity_processing: bool = SENTINEL,
        xml_external_entity_processing: bool = SENTINEL,
        **kwargs,
    ):
        """StandardProperties - see class docstring for parameter details."""
        if account_working_data_directories is not SENTINEL:
            self.account_working_data_directories = account_working_data_directories
        if allow_browsing is not SENTINEL:
            self.allow_browsing = allow_browsing
        if allow_user_logs is not SENTINEL:
            self.allow_user_logs = allow_user_logs
        if archive_processed_documents is not SENTINEL:
            self.archive_processed_documents = archive_processed_documents
        if async_message_poller_timeout_for_cluster_scale_down is not SENTINEL:
            self.async_message_poller_timeout_for_cluster_scale_down = (
                async_message_poller_timeout_for_cluster_scale_down
            )
        if auto_restart_on_out_of_memory is not SENTINEL:
            self.auto_restart_on_out_of_memory = auto_restart_on_out_of_memory
        if auto_restart_on_too_many_files_error is not SENTINEL:
            self.auto_restart_on_too_many_files_error = (
                auto_restart_on_too_many_files_error
            )
        if aws_secrets_manager is not SENTINEL:
            self.aws_secrets_manager = aws_secrets_manager
        if aws_secrets_manager_region is not SENTINEL:
            self.aws_secrets_manager_region = aws_secrets_manager_region
        if azure_secrets_manager is not SENTINEL:
            self.azure_secrets_manager = azure_secrets_manager
        if clean_up_custom_script_engine_data_on_completion is not SENTINEL:
            self.clean_up_custom_script_engine_data_on_completion = (
                clean_up_custom_script_engine_data_on_completion
            )
        if cloud_partition_replicas is not SENTINEL:
            self.cloud_partition_replicas = cloud_partition_replicas
        if cloud_partition_size is not SENTINEL:
            self.cloud_partition_size = cloud_partition_size
        if cluster_bootstrap_timeout is not SENTINEL:
            self.cluster_bootstrap_timeout = cluster_bootstrap_timeout
        if cluster_network_bind_address is not SENTINEL:
            self.cluster_network_bind_address = cluster_network_bind_address
        if cluster_network_transport_type is not SENTINEL:
            self.cluster_network_transport_type = self._enum_matching(
                cluster_network_transport_type,
                ClusterNetworkTransportType.list(),
                "cluster_network_transport_type",
            )
        if cluster_problem_automatic_delete_delay is not SENTINEL:
            self.cluster_problem_automatic_delete_delay = (
                cluster_problem_automatic_delete_delay
            )
        if cluster_problem_automatic_shutdown_delay is not SENTINEL:
            self.cluster_problem_automatic_shutdown_delay = (
                cluster_problem_automatic_shutdown_delay
            )
        if cluster_rolling_restart_percentage is not SENTINEL:
            self.cluster_rolling_restart_percentage = cluster_rolling_restart_percentage
        if compress_history_after_x_days is not SENTINEL:
            self.compress_history_after_x_days = compress_history_after_x_days
        if connector_browsing_idle_timeout is not SENTINEL:
            self.connector_browsing_idle_timeout = connector_browsing_idle_timeout
        if connector_browsing_max_thread_count is not SENTINEL:
            self.connector_browsing_max_thread_count = (
                connector_browsing_max_thread_count
            )
        if connector_browsing_maximum_browse_time is not SENTINEL:
            self.connector_browsing_maximum_browse_time = (
                connector_browsing_maximum_browse_time
            )
        if connector_browsing_time_to_live is not SENTINEL:
            self.connector_browsing_time_to_live = connector_browsing_time_to_live
        if connector_server_startup_timeout is not SENTINEL:
            self.connector_server_startup_timeout = connector_server_startup_timeout
        if connector_trace_logging is not SENTINEL:
            self.connector_trace_logging = connector_trace_logging
        if container_force_restart is not SENTINEL:
            self.container_force_restart = container_force_restart
        if container_host_name is not SENTINEL:
            self.container_host_name = container_host_name
        if container_name is not SENTINEL:
            self.container_name = container_name
        if container_purge_days is not SENTINEL:
            self.container_purge_days = container_purge_days
        if container_purge_immediately is not SENTINEL:
            self.container_purge_immediately = container_purge_immediately
        if control_id_cache_idle_timeout is not SENTINEL:
            self.control_id_cache_idle_timeout = control_id_cache_idle_timeout
        if control_id_cache_time_to_live is not SENTINEL:
            self.control_id_cache_time_to_live = control_id_cache_time_to_live
        if counter_file_lock_retry is not SENTINEL:
            self.counter_file_lock_retry = counter_file_lock_retry
        if counter_lock_retry_maximum_retries is not SENTINEL:
            self.counter_lock_retry_maximum_retries = (
                counter_lock_retry_maximum_retries
            )
        if counter_lock_retry_wait_time is not SENTINEL:
            self.counter_lock_retry_wait_time = counter_lock_retry_wait_time
        if customized_procbrowser_script_file_name is not SENTINEL:
            self.customized_procbrowser_script_file_name = (
                customized_procbrowser_script_file_name
            )
        if customized_procrunner_script_file_name is not SENTINEL:
            self.customized_procrunner_script_file_name = (
                customized_procrunner_script_file_name
            )
        if customized_procworker_script_file_name is not SENTINEL:
            self.customized_procworker_script_file_name = (
                customized_procworker_script_file_name
            )
        if customized_restart_script_file_name is not SENTINEL:
            self.customized_restart_script_file_name = (
                customized_restart_script_file_name
            )
        if debug_log_level_threshold is not SENTINEL:
            self.debug_log_level_threshold = self._enum_matching(
                debug_log_level_threshold,
                DebugLogLevelThreshold.list(),
                "debug_log_level_threshold",
            )
        if debug_logging is not SENTINEL:
            self.debug_logging = debug_logging
        if decommission_time_for_post_pause_sleep is not SENTINEL:
            self.decommission_time_for_post_pause_sleep = (
                decommission_time_for_post_pause_sleep
            )
        if default_time_zone_for_account_schedules is not SENTINEL:
            self.default_time_zone_for_account_schedules = (
                default_time_zone_for_account_schedules
            )
        if disk_space_monitoring is not SENTINEL:
            self.disk_space_monitoring = disk_space_monitoring
        if disk_space_monitoring_account_auto_suspension is not SENTINEL:
            self.disk_space_monitoring_account_auto_suspension = (
                disk_space_monitoring_account_auto_suspension
            )
        if disk_space_monitoring_frequency is not SENTINEL:
            self.disk_space_monitoring_frequency = disk_space_monitoring_frequency
        if disk_space_monitoring_threads is not SENTINEL:
            self.disk_space_monitoring_threads = disk_space_monitoring_threads
        if disk_space_monitoring_verbose_logging is not SENTINEL:
            self.disk_space_monitoring_verbose_logging = (
                disk_space_monitoring_verbose_logging
            )
        if disk_space_warning_limit is not SENTINEL:
            self.disk_space_warning_limit = disk_space_warning_limit
        if dump_to_file_when_exceeding_open_file_threshold is not SENTINEL:
            self.dump_to_file_when_exceeding_open_file_threshold = (
                dump_to_file_when_exceeding_open_file_threshold
            )
        if early_stale_execution_worker_ttl_percentage is not SENTINEL:
            self.early_stale_execution_worker_ttl_percentage = (
                early_stale_execution_worker_ttl_percentage
            )
        if elastic_worker_directory_level is not SENTINEL:
            self.elastic_worker_directory_level = elastic_worker_directory_level
        if elastic_worker_metrics_polling_period is not SENTINEL:
            self.elastic_worker_metrics_polling_period = (
                elastic_worker_metrics_polling_period
            )
        if execute_processes_as_forked_jvms is not SENTINEL:
            self.execute_processes_as_forked_jvms = self._enum_matching(
                execute_processes_as_forked_jvms,
                ExecuteProcessesAsForkedJvms.list(),
                "execute_processes_as_forked_jvms",
            )
        if execution_worker_idle_timeout is not SENTINEL:
            self.execution_worker_idle_timeout = execution_worker_idle_timeout
        if execution_worker_local_port_range is not SENTINEL:
            self.execution_worker_local_port_range = execution_worker_local_port_range
        if execution_worker_pending_updates_queue_size is not SENTINEL:
            self.execution_worker_pending_updates_queue_size = (
                execution_worker_pending_updates_queue_size
            )
        if execution_worker_startup_timeout is not SENTINEL:
            self.execution_worker_startup_timeout = execution_worker_startup_timeout
        if execution_worker_thread_pool_idle_timeout is not SENTINEL:
            self.execution_worker_thread_pool_idle_timeout = (
                execution_worker_thread_pool_idle_timeout
            )
        if execution_worker_time_to_live is not SENTINEL:
            self.execution_worker_time_to_live = execution_worker_time_to_live
        if execution_workers_enabled is not SENTINEL:
            self.execution_workers_enabled = execution_workers_enabled
        if external_hostname is not SENTINEL:
            self.external_hostname = external_hostname
        if force_restart_override_for_cluster_scale_down is not SENTINEL:
            self.force_restart_override_for_cluster_scale_down = (
                force_restart_override_for_cluster_scale_down
            )
        if force_start_shared_web_server is not SENTINEL:
            self.force_start_shared_web_server = force_start_shared_web_server
        if generate_heap_dump_on_low_memory is not SENTINEL:
            self.generate_heap_dump_on_low_memory = generate_heap_dump_on_low_memory
        if https_protocols is not SENTINEL:
            self.https_protocols = https_protocols
        if initial_hosts_for_unicast is not SENTINEL:
            self.initial_hosts_for_unicast = initial_hosts_for_unicast
        if jgroups_debug_logging is not SENTINEL:
            self.jgroups_debug_logging = jgroups_debug_logging
        if listener_startup_mode is not SENTINEL:
            self.listener_startup_mode = self._enum_matching(
                listener_startup_mode,
                ListenerStartupMode.list(),
                "listener_startup_mode",
            )
        if logger_queue_size is not SENTINEL:
            self.logger_queue_size = logger_queue_size
        if logger_timeout is not SENTINEL:
            self.logger_timeout = logger_timeout
        if low_latency_warning_threshold is not SENTINEL:
            self.low_latency_warning_threshold = low_latency_warning_threshold
        if low_memory_mode_threshold is not SENTINEL:
            self.low_memory_mode_threshold = low_memory_mode_threshold
        if low_remaining_open_files_threshold is not SENTINEL:
            self.low_remaining_open_files_threshold = (
                low_remaining_open_files_threshold
            )
        if mapping_expand_child_elements_legacy is not SENTINEL:
            self.mapping_expand_child_elements_legacy = (
                mapping_expand_child_elements_legacy
            )
        if max_cached_control_ids is not SENTINEL:
            self.max_cached_control_ids = max_cached_control_ids
        if max_cached_transaction_keys is not SENTINEL:
            self.max_cached_transaction_keys = max_cached_transaction_keys
        if max_document_elements_cache_size is not SENTINEL:
            self.max_document_elements_cache_size = max_document_elements_cache_size
        if max_execution_threads_per_connector_browser is not SENTINEL:
            self.max_execution_threads_per_connector_browser = (
                max_execution_threads_per_connector_browser
            )
        if max_execution_threads_per_execution_worker is not SENTINEL:
            self.max_execution_threads_per_execution_worker = (
                max_execution_threads_per_execution_worker
            )
        if max_execution_threads_per_forked_execution is not SENTINEL:
            self.max_execution_threads_per_forked_execution = (
                max_execution_threads_per_forked_execution
            )
        if max_flow_control_units is not SENTINEL:
            self.max_flow_control_units = max_flow_control_units
        if max_forked_execution_time_in_cloud is not SENTINEL:
            self.max_forked_execution_time_in_cloud = (
                max_forked_execution_time_in_cloud
            )
        if max_number_of_active_batches_per_listener is not SENTINEL:
            self.max_number_of_active_batches_per_listener = (
                max_number_of_active_batches_per_listener
            )
        if max_queued_executions_per_node is not SENTINEL:
            self.max_queued_executions_per_node = max_queued_executions_per_node
        if max_queued_forked_executions_per_node is not SENTINEL:
            self.max_queued_forked_executions_per_node = (
                max_queued_forked_executions_per_node
            )
        if max_simultaneous_executions_per_node is not SENTINEL:
            self.max_simultaneous_executions_per_node = (
                max_simultaneous_executions_per_node
            )
        if max_simultaneous_forked_executions_per_node is not SENTINEL:
            self.max_simultaneous_forked_executions_per_node = (
                max_simultaneous_forked_executions_per_node
            )
        if max_simultaneous_forked_jvms_per_node is not SENTINEL:
            self.max_simultaneous_forked_jvms_per_node = (
                max_simultaneous_forked_jvms_per_node
            )
        if max_size_for_update_operation is not SENTINEL:
            self.max_size_for_update_operation = max_size_for_update_operation
        if milliseconds_logging is not SENTINEL:
            self.milliseconds_logging = milliseconds_logging
        if min_number_of_hosts_for_unicast_autodetect is not SENTINEL:
            self.min_number_of_hosts_for_unicast_autodetect = (
                min_number_of_hosts_for_unicast_autodetect
            )
        if monitor_number_of_open_files is not SENTINEL:
            self.monitor_number_of_open_files = monitor_number_of_open_files
        if multicast_address is not SENTINEL:
            self.multicast_address = multicast_address
        if multicast_port is not SENTINEL:
            self.multicast_port = multicast_port
        if persisted_connector_cache is not SENTINEL:
            self.persisted_connector_cache = persisted_connector_cache
        if process_execution_directory_level is not SENTINEL:
            self.process_execution_directory_level = process_execution_directory_level
        if processed_document_archive_directory is not SENTINEL:
            self.processed_document_archive_directory = (
                processed_document_archive_directory
            )
        if proxy_user_id is not SENTINEL:
            self.proxy_user_id = proxy_user_id
        if purge_manager is not SENTINEL:
            self.purge_manager = purge_manager
        if purge_manager_threads is not SENTINEL:
            self.purge_manager_threads = purge_manager_threads
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
        if rolling_restart_force_timeout is not SENTINEL:
            self.rolling_restart_force_timeout = rolling_restart_force_timeout
        if rolling_restart_next_in_line_timeout is not SENTINEL:
            self.rolling_restart_next_in_line_timeout = (
                rolling_restart_next_in_line_timeout
            )
        if runtime_data_directory_level is not SENTINEL:
            self.runtime_data_directory_level = runtime_data_directory_level
        if runtime_pending_shutdown_delay is not SENTINEL:
            self.runtime_pending_shutdown_delay = runtime_pending_shutdown_delay
        if save_swagger_template_in_work_folder is not SENTINEL:
            self.save_swagger_template_in_work_folder = (
                save_swagger_template_in_work_folder
            )
        if security_policy is not SENTINEL:
            self.security_policy = self._enum_matching(
                security_policy, SecurityPolicy.list(), "security_policy"
            )
        if sequential_processing_of_custom_script_engine_data is not SENTINEL:
            self.sequential_processing_of_custom_script_engine_data = (
                sequential_processing_of_custom_script_engine_data
            )
        if show_runtime_icon_in_system_tray is not SENTINEL:
            self.show_runtime_icon_in_system_tray = show_runtime_icon_in_system_tray
        if ssl_debug_logging is not SENTINEL:
            self.ssl_debug_logging = ssl_debug_logging
        if standard_error_log_level is not SENTINEL:
            self.standard_error_log_level = self._enum_matching(
                standard_error_log_level,
                StandardErrorLogLevel.list(),
                "standard_error_log_level",
            )
        if standard_output_and_error_logging is not SENTINEL:
            self.standard_output_and_error_logging = standard_output_and_error_logging
        if tcp_port_for_unicast is not SENTINEL:
            self.tcp_port_for_unicast = tcp_port_for_unicast
        if threads_for_account_initialization is not SENTINEL:
            self.threads_for_account_initialization = (
                threads_for_account_initialization
            )
        if threads_for_account_initialization_during_starting_and_stopping_plugins is not SENTINEL:
            self.threads_for_account_initialization_during_starting_and_stopping_plugins = (
                threads_for_account_initialization_during_starting_and_stopping_plugins
            )
        if threads_for_recovering_executions_during_container_startup is not SENTINEL:
            self.threads_for_recovering_executions_during_container_startup = (
                threads_for_recovering_executions_during_container_startup
            )
        if threads_for_runtime_scheduling is not SENTINEL:
            self.threads_for_runtime_scheduling = threads_for_runtime_scheduling
        if threads_for_runtime_to_platform_messages is not SENTINEL:
            self.threads_for_runtime_to_platform_messages = (
                threads_for_runtime_to_platform_messages
            )
        if threads_for_runtime_to_platform_polling is not SENTINEL:
            self.threads_for_runtime_to_platform_polling = (
                threads_for_runtime_to_platform_polling
            )
        if threads_for_runtime_to_runtime_messages is not SENTINEL:
            self.threads_for_runtime_to_runtime_messages = (
                threads_for_runtime_to_runtime_messages
            )
        if timeout_for_escalating_cluster_issue is not SENTINEL:
            self.timeout_for_escalating_cluster_issue = (
                timeout_for_escalating_cluster_issue
            )
        if timeout_for_queued_executions_per_node is not SENTINEL:
            self.timeout_for_queued_executions_per_node = (
                timeout_for_queued_executions_per_node
            )
        if timeout_for_queued_forked_executions_per_node is not SENTINEL:
            self.timeout_for_queued_forked_executions_per_node = (
                timeout_for_queued_forked_executions_per_node
            )
        if trace_logging is not SENTINEL:
            self.trace_logging = trace_logging
        if use_local_storage_for_runtime_assets is not SENTINEL:
            self.use_local_storage_for_runtime_assets = (
                use_local_storage_for_runtime_assets
            )
        if worker_heartbeat_timeout is not SENTINEL:
            self.worker_heartbeat_timeout = worker_heartbeat_timeout
        if working_data_local_storage_directory is not SENTINEL:
            self.working_data_local_storage_directory = (
                working_data_local_storage_directory
            )
        if xml_entity_processing is not SENTINEL:
            self.xml_entity_processing = xml_entity_processing
        if xml_external_entity_processing is not SENTINEL:
            self.xml_external_entity_processing = xml_external_entity_processing
        self._kwargs = kwargs
