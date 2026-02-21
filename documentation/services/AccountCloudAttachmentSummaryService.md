# AccountCloudAttachmentSummaryService

A list of all methods in the `AccountCloudAttachmentSummaryService` service. Click on the method name to view detailed information about that method.

| Methods                                                                                                   | Description                                                                                                                                                                                                                                     |
| :-------------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [get_account_cloud_attachment_summary](#get_account_cloud_attachment_summary)                             | Retrieves the properties of the AccountCloudAttachmentSummary having the specified ID.                                                                                                                                                          |
| [bulk_account_cloud_attachment_summary](#bulk_account_cloud_attachment_summary)                           | To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).                                                                                                                                          |
| [query_account_cloud_attachment_summary](#query_account_cloud_attachment_summary)                         | For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging). |
| [query_more_account_cloud_attachment_summary](#query_more_account_cloud_attachment_summary)               | To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).                                                                                                                                                  |

## get_account_cloud_attachment_summary

Retrieves the properties of the AccountCloudAttachmentSummary having the specified ID.

- HTTP Method: `GET`
- Endpoint: `/AccountCloudAttachmentSummary/{id}`

**Parameters**

| Name | Type | Required | Description                              |
| :--- | :--- | :------- | :--------------------------------------- |
| id\_ | str  | ✅       | A unique ID assigned by the system.     |

**Return Type**

`AccountCloudAttachmentSummary`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.account_cloud_attachment_summary.get_account_cloud_attachment_summary(id_="id")

print(result)
```

## bulk_account_cloud_attachment_summary

To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

- HTTP Method: `POST`
- Endpoint: `/AccountCloudAttachmentSummary/bulk`

**Parameters**

| Name         | Type                                                                                                  | Required | Description       |
| :----------- | :---------------------------------------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [AccountCloudAttachmentSummaryBulkRequest](../models/AccountCloudAttachmentSummaryBulkRequest.md)     | ❌       | The request body. |

**Return Type**

`AccountCloudAttachmentSummaryBulkResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import AccountCloudAttachmentSummaryBulkRequest

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = AccountCloudAttachmentSummaryBulkRequest(
    request=[
        {
            "id_": "56789abc-def0-1234-5678-9abcdef01234"
        }
    ],
    type_="GET"
)

result = sdk.account_cloud_attachment_summary.bulk_account_cloud_attachment_summary(request_body=request_body)

print(result)
```

## query_account_cloud_attachment_summary

For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/AccountCloudAttachmentSummary/query`

**Parameters**

| Name         | Type                                                                                                    | Required | Description       |
| :----------- | :------------------------------------------------------------------------------------------------------ | :------- | :---------------- |
| request_body | [AccountCloudAttachmentSummaryQueryConfig](../models/AccountCloudAttachmentSummaryQueryConfig.md)       | ❌       | The request body. |

**Return Type**

`AccountCloudAttachmentSummaryQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import AccountCloudAttachmentSummaryQueryConfig

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = AccountCloudAttachmentSummaryQueryConfig(
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

result = sdk.account_cloud_attachment_summary.query_account_cloud_attachment_summary(request_body=request_body)

print(result)
```

## query_more_account_cloud_attachment_summary

To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/AccountCloudAttachmentSummary/queryMore`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | str  | ✅       | The request body. |

**Return Type**

`AccountCloudAttachmentSummaryQueryResponse`

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

result = sdk.account_cloud_attachment_summary.query_more_account_cloud_attachment_summary(request_body=request_body)

print(result)
```
