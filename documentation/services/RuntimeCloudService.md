# RuntimeCloudService

A list of all methods in the `RuntimeCloudService` service. Click on the method name to view detailed information about that method.

| Methods                                                   | Description                                                                                                                                                                                                                                     |
| :-------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [create_runtime_cloud](#create_runtime_cloud)             | Creates a new RuntimeCloud object.                                                                                                                                                                                                              |
| [get_runtime_cloud](#get_runtime_cloud)                   | Retrieves the properties of the RuntimeCloud having the specified ID.                                                                                                                                                                           |
| [update_runtime_cloud](#update_runtime_cloud)             | Updates the RuntimeCloud object having the specified ID.                                                                                                                                                                                        |
| [delete_runtime_cloud](#delete_runtime_cloud)             | Deletes the RuntimeCloud object with the specified ID.                                                                                                                                                                                          |
| [bulk_runtime_cloud](#bulk_runtime_cloud)                 | To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).                                                                                                                                          |
| [query_runtime_cloud](#query_runtime_cloud)               | For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging). |
| [query_more_runtime_cloud](#query_more_runtime_cloud)     | To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).                                                                                                                                                  |

## create_runtime_cloud

Creates a new RuntimeCloud object.

- HTTP Method: `POST`
- Endpoint: `/RuntimeCloud`

**Parameters**

| Name         | Type                                          | Required | Description       |
| :----------- | :-------------------------------------------- | :------- | :---------------- |
| request_body | [RuntimeCloud](../models/RuntimeCloud.md)     | ❌       | The request body. |

**Return Type**

`RuntimeCloud`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import RuntimeCloud

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = RuntimeCloud()

result = sdk.runtime_cloud.create_runtime_cloud(request_body=request_body)

print(result)
```

## get_runtime_cloud

Retrieves the properties of the RuntimeCloud having the specified ID.

- HTTP Method: `GET`
- Endpoint: `/RuntimeCloud/{id}`

**Parameters**

| Name | Type | Required | Description                                              |
| :--- | :--- | :------- | :------------------------------------------------------- |
| id\_ | str  | ✅       | A unique ID assigned by the system to the RuntimeCloud. |

**Return Type**

`RuntimeCloud`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.runtime_cloud.get_runtime_cloud(id_="id")

print(result)
```

## update_runtime_cloud

Updates the RuntimeCloud object having the specified ID.

- HTTP Method: `POST`
- Endpoint: `/RuntimeCloud/{id}`

**Parameters**

| Name         | Type                                          | Required | Description                                              |
| :----------- | :-------------------------------------------- | :------- | :------------------------------------------------------- |
| request_body | [RuntimeCloud](../models/RuntimeCloud.md)     | ❌       | The request body.                                        |
| id\_         | str                                           | ✅       | A unique ID assigned by the system to the RuntimeCloud. |

**Return Type**

`RuntimeCloud`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import RuntimeCloud

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = RuntimeCloud()

result = sdk.runtime_cloud.update_runtime_cloud(
    request_body=request_body,
    id_="id"
)

print(result)
```

## delete_runtime_cloud

Deletes the RuntimeCloud object with the specified ID.

- HTTP Method: `DELETE`
- Endpoint: `/RuntimeCloud/{id}`

**Parameters**

| Name | Type | Required | Description                                              |
| :--- | :--- | :------- | :------------------------------------------------------- |
| id\_ | str  | ✅       | A unique ID assigned by the system to the RuntimeCloud. |

**Return Type**

Returns nothing.

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

sdk.runtime_cloud.delete_runtime_cloud(id_="id")
```

## bulk_runtime_cloud

To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

- HTTP Method: `POST`
- Endpoint: `/RuntimeCloud/bulk`

**Parameters**

| Name         | Type                                                                  | Required | Description       |
| :----------- | :-------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [RuntimeCloudBulkRequest](../models/RuntimeCloudBulkRequest.md)       | ❌       | The request body. |

**Return Type**

`RuntimeCloudBulkResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import RuntimeCloudBulkRequest

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = RuntimeCloudBulkRequest(
    request=[
        {
            "id_": "56789abc-def0-1234-5678-9abcdef01234"
        }
    ],
    type_="GET"
)

result = sdk.runtime_cloud.bulk_runtime_cloud(request_body=request_body)

print(result)
```

## query_runtime_cloud

For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/RuntimeCloud/query`

**Parameters**

| Name         | Type                                                                  | Required | Description       |
| :----------- | :-------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [RuntimeCloudQueryConfig](../models/RuntimeCloudQueryConfig.md)       | ❌       | The request body. |

**Return Type**

`RuntimeCloudQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import RuntimeCloudQueryConfig

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = RuntimeCloudQueryConfig(
    query_filter={
        "expression": {
            "argument": [
                "argument"
            ],
            "operator": "EQUALS",
            "property": "name"
        }
    }
)

result = sdk.runtime_cloud.query_runtime_cloud(request_body=request_body)

print(result)
```

## query_more_runtime_cloud

To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/RuntimeCloud/queryMore`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | str  | ✅       | The request body. |

**Return Type**

`RuntimeCloudQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = "queryToken"

result = sdk.runtime_cloud.query_more_runtime_cloud(request_body=request_body)

print(result)
```
