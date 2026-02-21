
from .utils.json_map import JsonMap
from .utils.base_model import BaseModel
from .utils.sentinel import SENTINEL


@JsonMap(
    {
        "bouncy_castle_library_version": "bouncyCastleLibraryVersion",
        "client_default_connect_timeout": "clientDefaultConnectTimeout",
        "client_default_read_timeout": "clientDefaultReadTimeout",
        "dns_time_to_live": "dnsTimeToLive",
        "endorsed_directories": "endorsedDirectories",
        "file_encoding": "fileEncoding",
        "headless_mode": "headlessMode",
        "heap_dump_on_out_of_memory_error": "heapDumpOnOutOfMemoryError",
        "heap_size": "heapSize",
        "java_class_path": "javaClassPath",
        "java_class_path_prepend": "javaClassPathPrepend",
        "java_library_path": "javaLibraryPath",
        "java_security_compatibility": "javaSecurityCompatibility",
        "jgroups_clustered_library_version": "jgroupsClusteredLibraryVersion",
        "jmx_remote_authentication": "jmxRemoteAuthentication",
        "jmx_remote_port": "jmxRemotePort",
        "jmx_remote_rmi_port": "jmxRemoteRmiPort",
        "jmx_remote_ssl": "jmxRemoteSsl",
        "non_proxy_hosts": "nonProxyHosts",
        "prefer_ipv4_stack": "preferIpv4Stack",
        "proxy_host": "proxyHost",
        "proxy_port": "proxyPort",
        "retry_http_post": "retryHttpPost",
        "temp_directory": "tempDirectory",
    }
)
class SystemProperties(BaseModel):
    """SystemProperties

    :param bouncy_castle_library_version: bouncy_castle_library_version, defaults to None
    :type bouncy_castle_library_version: str, optional
    :param client_default_connect_timeout: client_default_connect_timeout, defaults to None
    :type client_default_connect_timeout: int, optional
    :param client_default_read_timeout: client_default_read_timeout, defaults to None
    :type client_default_read_timeout: int, optional
    :param dns_time_to_live: dns_time_to_live, defaults to None
    :type dns_time_to_live: int, optional
    :param endorsed_directories: endorsed_directories, defaults to None
    :type endorsed_directories: str, optional
    :param file_encoding: file_encoding, defaults to None
    :type file_encoding: str, optional
    :param headless_mode: headless_mode, defaults to None
    :type headless_mode: bool, optional
    :param heap_dump_on_out_of_memory_error: heap_dump_on_out_of_memory_error, defaults to None
    :type heap_dump_on_out_of_memory_error: bool, optional
    :param heap_size: heap_size, defaults to None
    :type heap_size: str, optional
    :param java_class_path: java_class_path, defaults to None
    :type java_class_path: str, optional
    :param java_class_path_prepend: java_class_path_prepend, defaults to None
    :type java_class_path_prepend: str, optional
    :param java_library_path: java_library_path, defaults to None
    :type java_library_path: str, optional
    :param java_security_compatibility: java_security_compatibility, defaults to None
    :type java_security_compatibility: str, optional
    :param jgroups_clustered_library_version: jgroups_clustered_library_version, defaults to None
    :type jgroups_clustered_library_version: int, optional
    :param jmx_remote_authentication: jmx_remote_authentication, defaults to None
    :type jmx_remote_authentication: bool, optional
    :param jmx_remote_port: jmx_remote_port, defaults to None
    :type jmx_remote_port: int, optional
    :param jmx_remote_rmi_port: jmx_remote_rmi_port, defaults to None
    :type jmx_remote_rmi_port: int, optional
    :param jmx_remote_ssl: jmx_remote_ssl, defaults to None
    :type jmx_remote_ssl: bool, optional
    :param non_proxy_hosts: non_proxy_hosts, defaults to None
    :type non_proxy_hosts: str, optional
    :param prefer_ipv4_stack: prefer_ipv4_stack, defaults to None
    :type prefer_ipv4_stack: bool, optional
    :param proxy_host: proxy_host, defaults to None
    :type proxy_host: str, optional
    :param proxy_port: proxy_port, defaults to None
    :type proxy_port: str, optional
    :param retry_http_post: retry_http_post, defaults to None
    :type retry_http_post: bool, optional
    :param temp_directory: temp_directory, defaults to None
    :type temp_directory: str, optional
    """

    def __init__(
        self,
        bouncy_castle_library_version: str = SENTINEL,
        client_default_connect_timeout: int = SENTINEL,
        client_default_read_timeout: int = SENTINEL,
        dns_time_to_live: int = SENTINEL,
        endorsed_directories: str = SENTINEL,
        file_encoding: str = SENTINEL,
        headless_mode: bool = SENTINEL,
        heap_dump_on_out_of_memory_error: bool = SENTINEL,
        heap_size: str = SENTINEL,
        java_class_path: str = SENTINEL,
        java_class_path_prepend: str = SENTINEL,
        java_library_path: str = SENTINEL,
        java_security_compatibility: str = SENTINEL,
        jgroups_clustered_library_version: int = SENTINEL,
        jmx_remote_authentication: bool = SENTINEL,
        jmx_remote_port: int = SENTINEL,
        jmx_remote_rmi_port: int = SENTINEL,
        jmx_remote_ssl: bool = SENTINEL,
        non_proxy_hosts: str = SENTINEL,
        prefer_ipv4_stack: bool = SENTINEL,
        proxy_host: str = SENTINEL,
        proxy_port: str = SENTINEL,
        retry_http_post: bool = SENTINEL,
        temp_directory: str = SENTINEL,
        **kwargs,
    ):
        """SystemProperties - see class docstring for parameter details."""
        if bouncy_castle_library_version is not SENTINEL:
            self.bouncy_castle_library_version = bouncy_castle_library_version
        if client_default_connect_timeout is not SENTINEL:
            self.client_default_connect_timeout = client_default_connect_timeout
        if client_default_read_timeout is not SENTINEL:
            self.client_default_read_timeout = client_default_read_timeout
        if dns_time_to_live is not SENTINEL:
            self.dns_time_to_live = dns_time_to_live
        if endorsed_directories is not SENTINEL:
            self.endorsed_directories = endorsed_directories
        if file_encoding is not SENTINEL:
            self.file_encoding = file_encoding
        if headless_mode is not SENTINEL:
            self.headless_mode = headless_mode
        if heap_dump_on_out_of_memory_error is not SENTINEL:
            self.heap_dump_on_out_of_memory_error = heap_dump_on_out_of_memory_error
        if heap_size is not SENTINEL:
            self.heap_size = heap_size
        if java_class_path is not SENTINEL:
            self.java_class_path = java_class_path
        if java_class_path_prepend is not SENTINEL:
            self.java_class_path_prepend = java_class_path_prepend
        if java_library_path is not SENTINEL:
            self.java_library_path = java_library_path
        if java_security_compatibility is not SENTINEL:
            self.java_security_compatibility = java_security_compatibility
        if jgroups_clustered_library_version is not SENTINEL:
            self.jgroups_clustered_library_version = jgroups_clustered_library_version
        if jmx_remote_authentication is not SENTINEL:
            self.jmx_remote_authentication = jmx_remote_authentication
        if jmx_remote_port is not SENTINEL:
            self.jmx_remote_port = jmx_remote_port
        if jmx_remote_rmi_port is not SENTINEL:
            self.jmx_remote_rmi_port = jmx_remote_rmi_port
        if jmx_remote_ssl is not SENTINEL:
            self.jmx_remote_ssl = jmx_remote_ssl
        if non_proxy_hosts is not SENTINEL:
            self.non_proxy_hosts = non_proxy_hosts
        if prefer_ipv4_stack is not SENTINEL:
            self.prefer_ipv4_stack = prefer_ipv4_stack
        if proxy_host is not SENTINEL:
            self.proxy_host = proxy_host
        if proxy_port is not SENTINEL:
            self.proxy_port = proxy_port
        if retry_http_post is not SENTINEL:
            self.retry_http_post = retry_http_post
        if temp_directory is not SENTINEL:
            self.temp_directory = temp_directory
        self._kwargs = kwargs
