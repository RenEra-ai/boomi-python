# Boomi Python SDK

A modern, intuitive Python SDK for the Boomi Platform API that makes integration development simple and efficient.

[![Python 3.9+](https://img.shields.io/badge/python-3.9+-blue.svg)](https://www.python.org/downloads/)
[![PyPI version](https://badge.fury.io/py/boomi.svg)](https://badge.fury.io/py/boomi)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## 🚀 What is Boomi?

[Boomi](https://boomi.com) is a leading cloud-native integration platform that connects applications, data, and people. The Boomi Platform API provides programmatic access to manage integrations, deploy processes, monitor executions, and control platform resources.

## 📦 Installation

```bash
pip install boomi
```

## ⚡ Quick Start

```python
from boomi import Boomi

# Initialize the SDK
client = Boomi(
    account_id="your-account-id",
    access_token="your-api-token"  # or use username/password
)

# List all environments
environments = client.environment.query_environment()
print(f"Found {len(environments.result)} environments")

# Component XML is opaque: get_component returns RAW bytes (the SDK never parses it)
from boomi import extract_component_xml_metadata

xml = client.component.get_component(component_id="your-process-id")  # -> bytes
print(f"Process: {extract_component_xml_metadata(xml)['name']}")

# Execute a process
from boomi.models import ExecutionRequest

execution = client.execution_request.create_execution_request(
    request_body=ExecutionRequest(
        process_id="your-process-id",
        atom_id="your-atom-id"
    )
)
print(f"Execution ID: {execution.request_id}")
```

## 🔑 Authentication

The SDK supports multiple authentication methods:

### API Token (Recommended)
```python
client = Boomi(
    account_id="your-account-id",
    access_token="your-api-token"
)
```

### Username/Password
```python
client = Boomi(
    account_id="your-account-id",
    username="your-username",
    password="your-password"
)
```

> 💡 **Tip**: Get your API token from the Boomi Platform: **Manage** → **AtomSphere API Tokens**

## 🎯 Key Features

### 📋 **Process Management**
- Create, update, and deploy integration processes
- Manage process components and configurations
- Handle process libraries and shared resources

### 🔄 **Runtime Operations**
- Execute processes on-demand
- Monitor execution status and logs
- Manage Atom and Molecule runtimes

### 🌍 **Environment Control**
- Manage deployment environments
- Handle environment extensions and configurations
- Control environment roles and permissions

### 👥 **Account Administration**
- User and role management
- Account configuration
- License and quota monitoring

### 📊 **Monitoring & Analytics**
- Execution records and logs
- Performance metrics
- Error tracking and debugging

## 🔧 Advanced Usage

### Async Support
```python
import asyncio
from boomi import BoomiAsync

async def main():
    client = BoomiAsync(
        account_id="your-account-id",
        access_token="your-api-token"
    )
    environments = await client.environment.query_environment()
    print(f"Found {len(environments.result)} environments")

asyncio.run(main())
```

### Custom Timeout
```python
client = Boomi(
    account_id="your-account-id",
    access_token="your-api-token",
    timeout=30000  # 30 seconds (default: 60 seconds)
)
```

### Error Handling
```python
from boomi.net.transport.api_error import ApiError

try:
    process = client.component.get_component(component_id="invalid-id")
except ApiError as e:
    print(f"API Error: {e.status} - {e.message}")
```

## 📚 Common Use Cases

### Inspect Deployed Packages
```python
# Preferred deployment surface: packaged components and deployed packages
deployed_packages = client.deployed_package.query_deployed_package()

for deployed_package in deployed_packages.result[:5]:
    print(f"Deployment: {deployed_package.id_}")
```

### Monitor Executions
```python
# Query recent executions
executions = client.execution_record.query_execution_record()

for execution in executions.result[:5]:
    print(f"Execution {execution.execution_id}: {execution.status}")
```

### Manage Atoms
```python
# List all atoms
atoms = client.atom.query_atom()

for atom in atoms.result:
    print(f"Atom: {atom.name} - Status: {atom.status}")
```

## 🏗️ Architecture

The SDK is organized into logical service modules:

- **Component Services**: Process, connector, and component management
- **Runtime Services**: Atom, execution, and deployment management  
- **Platform Services**: Account, environment, and user management
- **Monitoring Services**: Logs, metrics, and audit trails

Each service provides intuitive methods following REST conventions:
- `get_*()` - Retrieve single resources
- `query_*()` - Search and filter resources
- `create_*()` - Create new resources
- `update_*()` - Modify existing resources
- `delete_*()` - Remove resources

## 🔗 Resources

- **[Boomi Platform Documentation](https://help.boomi.com/)**
- **[API Reference](https://help.boomi.com/docs/atomsphere/api/)**
- **[OpenAPI Specification](https://api.boomi.com/docs/)**
- **[SDK Examples](https://github.com/RenEra-ai/boomi-python/tree/main/examples)**

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## ⚠️ Requirements

- Python 3.9 or higher
- Active Boomi account with API access
- Valid API token or username/password credentials

---

**Built with ❤️ for the Boomi developer community**
