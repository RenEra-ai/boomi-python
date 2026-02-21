# AccountCloudAttachmentPropertiesDefaultService

A list of all methods in the `AccountCloudAttachmentPropertiesDefaultService` service. Click on the method name to view detailed information about that method.

| Methods                                                                                                                         | Description                                                                          |
| :------------------------------------------------------------------------------------------------------------------------------ | :----------------------------------------------------------------------------------- |
| [update_account_cloud_attachment_properties_default](#update_account_cloud_attachment_properties_default)                       | Updates the AccountCloudAttachmentPropertiesDefault object having the specified ID.  |
| [async_get_account_cloud_attachment_properties_default](#async_get_account_cloud_attachment_properties_default)                 | Returns a token for the specified AccountCloudAttachmentPropertiesDefault.           |
| [async_token_account_cloud_attachment_properties_default](#async_token_account_cloud_attachment_properties_default)             | For a response, use the token from the initial GET response in a new request.       |

## update_account_cloud_attachment_properties_default

Updates the AccountCloudAttachmentPropertiesDefault object having the specified ID.

- HTTP Method: `POST`
- Endpoint: `/AccountCloudAttachmentPropertiesDefault/{id}`

**Parameters**

| Name         | Type                                                                                                | Required | Description       |
| :----------- | :-------------------------------------------------------------------------------------------------- | :------- | :---------------- |
| request_body | [AccountCloudAttachmentPropertiesDefault](../models/AccountCloudAttachmentPropertiesDefault.md)     | ❌       | The request body. |
| id\_         | str                                                                                                 | ✅       |                   |

**Return Type**

`AccountCloudAttachmentPropertiesDefault`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import AccountCloudAttachmentPropertiesDefault

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = AccountCloudAttachmentPropertiesDefault()

result = sdk.account_cloud_attachment_properties_default.update_account_cloud_attachment_properties_default(
    request_body=request_body,
    id_="id"
)

print(result)
```

## async_get_account_cloud_attachment_properties_default

Returns a token for the specified AccountCloudAttachmentPropertiesDefault.

- HTTP Method: `GET`
- Endpoint: `/async/AccountCloudAttachmentPropertiesDefault/{id}`

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

result = sdk.account_cloud_attachment_properties_default.async_get_account_cloud_attachment_properties_default(id_="id")

print(result)
```

## async_token_account_cloud_attachment_properties_default

For a response, use the token from the initial GET response in a new request.

- HTTP Method: `GET`
- Endpoint: `/async/AccountCloudAttachmentPropertiesDefault/response/{token}`

**Parameters**

| Name  | Type | Required | Description                                                 |
| :---- | :--- | :------- | :---------------------------------------------------------- |
| token | str  | ✅       | Takes in the token from a previous call to return a result. |

**Return Type**

`AccountCloudAttachmentPropertiesDefaultAsyncResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.account_cloud_attachment_properties_default.async_token_account_cloud_attachment_properties_default(token="token")

print(result)
```
