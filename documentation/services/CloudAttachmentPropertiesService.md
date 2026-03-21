# CloudAttachmentPropertiesService

A list of all methods in the `CloudAttachmentPropertiesService` service. Click on the method name to view detailed information about that method.

| Methods                                                                                       | Description                                                                                          |
| :-------------------------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------- |
| [update_cloud_attachment_properties](#update_cloud_attachment_properties)                     | Modifies one or more Cloud attachment properties.                                                    |
| [async_get_cloud_attachment_properties](#async_get_cloud_attachment_properties)               | Use the GET operation to return and view Cloud attachment properties.                                 |
| [async_token_cloud_attachment_properties](#async_token_cloud_attachment_properties)           | Send a second GET request with the token returned in the first GET request.                           |

## update_cloud_attachment_properties

Modifies one or more Cloud attachment properties.

- HTTP Method: `POST`
- Endpoint: `/CloudAttachmentProperties/{id}`

**Parameters**

| Name         | Type                                                                    | Required | Description                                 |
| :----------- | :---------------------------------------------------------------------- | :------- | :------------------------------------------ |
| request_body | [CloudAttachmentProperties](../models/CloudAttachmentProperties.md)     | ✅       | The request body. Must include container_name. |
| id\_         | str                                                                     | ✅       |                                             |

**Return Type**

`CloudAttachmentProperties`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import CloudAttachmentProperties

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = CloudAttachmentProperties(
    archive_processed_documents=True,
    container_name="containerName",
    container_purge_days=30,
    container_purge_immediately=False,
    default_time_zone_for_account_schedules="America/New_York",
    low_latency_warning_threshold=100,
    partial_update=True,
    purge_schedule_for_components=30,
    purge_schedule_for_logs=30,
    purge_schedule_for_processed_documents=30,
    purge_schedule_for_temporary_data=30,
    runtime_id="runtimeId"
)

result = sdk.cloud_attachment_properties.update_cloud_attachment_properties(
    request_body=request_body,
    id_="id"
)

print(result)
```

## async_get_cloud_attachment_properties

Use the GET operation to return and view Cloud attachment properties.

- HTTP Method: `GET`
- Endpoint: `/async/CloudAttachmentProperties/{id}`

**Parameters**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| id\_ | str  | ✅       |             |

**Return Type**

`AsyncOperationTokenResult`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.cloud_attachment_properties.async_get_cloud_attachment_properties(id_="id")

print(result)
```

## async_token_cloud_attachment_properties

Send a second GET request with the token returned in the first GET request.

- HTTP Method: `GET`
- Endpoint: `/async/CloudAttachmentProperties/response/{token}`

**Parameters**

| Name  | Type | Required | Description                                                 |
| :---- | :--- | :------- | :---------------------------------------------------------- |
| token | str  | ✅       | Takes in the token from a previous call to return a result. |

**Return Type**

`CloudAttachmentPropertiesAsyncResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.cloud_attachment_properties.async_token_cloud_attachment_properties(token="token")

print(result)
```
