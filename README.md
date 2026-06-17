# Boomi Python SDK

[![Python Version](https://img.shields.io/badge/python-3.9%2B-blue)](https://www.python.org/downloads/)
[![PyPI Version](https://img.shields.io/pypi/v/boomi)](https://pypi.org/project/boomi/)
[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)

A Python SDK for the Boomi Platform API, providing programmatic access to the Boomi Enterprise Platform functionality. This SDK allows you to control and manage various objects associated with your Boomi account including processes, components, deployments, atoms, and more.

## 🚀 Quick Start

### Installation

Install the SDK using pip:

```bash
pip install boomi
```

### Basic Usage

```python
from boomi import Boomi

# Initialize the SDK
sdk = Boomi(
    account_id="your-account-id",
    username="your-username", 
    password="your-password",
    timeout=10000
)

# Get account information
result = sdk.account.get_account(id_="your-account-id")
print(result)
```

### Using API Tokens (Recommended)

```python
from boomi import Boomi

sdk = Boomi(
    account_id="your-account-id",
    access_token="your-api-token",
    timeout=10000
)

# Query component metadata
components = sdk.component_metadata.query_component_metadata()
print(f"Found {len(components.result)} components")
```

### Environment Variables (Best Practice)

Create a `.env` file:

```env
BOOMI_ACCOUNT=your-account-id
BOOMI_USER=your-username
BOOMI_SECRET=your-password-or-token
```

Then use in your code:

```python
import os
from dotenv import load_dotenv
from boomi import Boomi

load_dotenv()

sdk = Boomi(
    account_id=os.getenv("BOOMI_ACCOUNT"),
    username=os.getenv("BOOMI_USER"),
    password=os.getenv("BOOMI_SECRET"),
    timeout=10000
)
```

## 🔐 Authentication

The SDK supports multiple authentication methods:

### API Token Authentication (Recommended)
```python
sdk = Boomi(
    account_id="your-account-id",
    access_token="your-api-token"
)
```

### Username/Password Authentication
```python
sdk = Boomi(
    account_id="your-account-id",
    username="your-username",
    password="your-password"
)
```

> **Note:** API tokens are required for accounts with SSO or 2FA enabled.

## ⚡ Async Support

The SDK includes full async support for non-blocking operations:

```python
import asyncio
from boomi import BoomiAsync

async def main():
    sdk = BoomiAsync(
        account_id="your-account-id",
        access_token="your-api-token"
    )
    
    result = await sdk.account.get_account(id_="your-account-id")
    print(result)

asyncio.run(main())
```

## 🛠️ Core Services

The SDK provides access to all major Boomi Platform API services:

| Service | Description | Example Usage |
|---------|-------------|---------------|
| **Account** | Account management | `sdk.account.get_account()` |
| **Component** | Processes, connectors, maps | `sdk.component_metadata.query_component_metadata()` |
| **Atom** | Runtime management | `sdk.atom.query_atom()` |
| **Deployed Package** | Inspect packaged deployments | `sdk.deployed_package.query_deployed_package()` |
| **Environment** | Environment management | `sdk.environment.query_environment()` |
| **Execution** | Process execution | `sdk.execution_request.create_execution_request()` |

### Example: Working with Components

```python
from boomi.models import (
    ComponentMetadataQueryConfig,
    ComponentMetadataQueryConfigQueryFilter,
    ComponentMetadataSimpleExpression,
    ComponentMetadataSimpleExpressionOperator,
    ComponentMetadataSimpleExpressionProperty,
)

# Query all processes
processes = sdk.component_metadata.query_component_metadata(
    request_body=ComponentMetadataQueryConfig(
        query_filter=ComponentMetadataQueryConfigQueryFilter(
            expression=ComponentMetadataSimpleExpression(
                operator=ComponentMetadataSimpleExpressionOperator.EQUALS,
                property=ComponentMetadataSimpleExpressionProperty.TYPE,
                argument=["process"],
            )
        )
    )
)

# Component XML is opaque: get/create/update send & return RAW bytes,
# byte-for-byte identical to the Boomi API (the SDK never parses it).
from boomi import extract_component_xml_metadata

xml = sdk.component.get_component(component_id="component-id")  # -> bytes

# Read the root <Component> attributes without re-parsing the whole document
meta = extract_component_xml_metadata(xml)
print(meta["componentId"], meta["name"], meta["type"], meta["version"])

# Update by passing the exact raw XML (str/bytes); a model/dict is rejected
# with UnsafeComponentXmlSerializationError.
updated = sdk.component.update_component(
    component_id="component-id",
    request_body=xml,
)
```

### Example: Inspecting Deployed Packages

```python
# Preferred deployment surface: packaged components and deployed packages
deployed_packages = sdk.deployed_package.query_deployed_package()

for deployed_package in deployed_packages.result[:5]:
    print(deployed_package.id_)
```

### Example: Executing Processes

```python
from boomi.models import ExecutionRequest

# Execute a process
execution = sdk.execution_request.create_execution_request(
    request_body=ExecutionRequest(
        process_id="process-id",
        atom_id="atom-id"
    )
)

# Check execution status
status = sdk.execution_record.get_execution_record(
    id_=execution.request_id
)
```

## 🧪 Development

### Setup Development Environment

```bash
# Clone the repository
git clone https://github.com/RenEra-ai/boomi-python.git
cd boomi-python

# Install development dependencies
make install-dev

# Run example scripts (validates setup)
make run-examples

# Run linting
make lint
```

### Validating Your Setup

Use the provided example scripts to verify everything works:

```bash
# Copy environment template
cp examples/.env.example examples/.env

# Edit with your credentials
nano examples/.env

# Run the sample
PYTHONPATH=src python examples/12_utilities/sample.py
```

## 📖 Documentation

- **[API Documentation](documentation/)** - Detailed service and model documentation
- **[Examples](examples/)** - Complete working examples
- **[Boomi Platform API Reference](https://help.boomi.com/docs/Atomsphere/Platform/)** - Official Boomi API docs

## 🏗️ Architecture

This SDK is built on the Boomi Platform API OpenAPI 3.0 specification:

- **Generated SDK**: Auto-generated from OpenAPI spec
- **Type Safety**: Strongly-typed request/response models
- **Async Support**: Full async/await support for all operations
- **Error Handling**: Comprehensive error handling and validation
- **Configurable**: Flexible authentication and timeout settings

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guide](CONTRIBUTING.md) for details.

### Development Commands

```bash
make install          # Install production dependencies
make install-dev      # Install development dependencies
make run-examples     # Run example scripts (validates SDK functionality)
make lint            # Run code quality checks
make format          # Format code
make clean           # Clean temporary files
```

### SDK Validation

This SDK is validated through **69 real-world example scripts** that execute against the actual Boomi Platform API.

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🆘 Support

- **Issues**: [GitHub Issues](https://github.com/RenEra-ai/boomi-python/issues)
- **Documentation**: [Boomi Help Center](https://help.boomi.com/)
- **API Reference**: [Platform API Documentation](https://help.boomi.com/docs/Atomsphere/Platform/)

## 🔗 Related Projects

- **[OpenAPI Specification](openapi/)** - The OpenAPI spec this SDK is based on
- **[Boomi CLI](https://help.boomi.com/docs/Atomsphere/Platform/)** - Official Boomi command line tools
- **[Boomi Flow](https://help.boomi.com/docs/boomiflow/)** - Boomi's low-code application platform

---

**Made with ❤️ for the Boomi Community**
