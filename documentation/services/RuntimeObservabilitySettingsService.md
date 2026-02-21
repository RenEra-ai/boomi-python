# RuntimeObservabilitySettingsService

A list of all methods in the `RuntimeObservabilitySettingsService` service. Click on the method name to view detailed information about that method.

| Methods                                                                                             | Description                                                                    |
| :-------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------- |
| [update_runtime_observability_settings](#update_runtime_observability_settings)                     | Updates the RuntimeObservabilitySettings object having the specified ID.       |
| [async_get_runtime_observability_settings](#async_get_runtime_observability_settings)               | Returns a token for the specified RuntimeObservabilitySettings.               |
| [async_token_runtime_observability_settings](#async_token_runtime_observability_settings)           | For a response, use the token from the initial GET response in a new request. |

## update_runtime_observability_settings

Updates the RuntimeObservabilitySettings object having the specified ID.

- HTTP Method: `POST`
- Endpoint: `/RuntimeObservabilitySettings/{id}`

**Parameters**

| Name         | Type                                                                                              | Required | Description       |
| :----------- | :------------------------------------------------------------------------------------------------ | :------- | :---------------- |
| request_body | [RuntimeObservabilitySettingsRequest](../models/RuntimeObservabilitySettingsRequest.md)           | ❌       | The request body. |
| id\_         | str                                                                                               | ✅       |                   |

**Return Type**

`RuntimeObservabilitySettings`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import RuntimeObservabilitySettingsRequest

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = RuntimeObservabilitySettingsRequest()

result = sdk.runtime_observability_settings.update_runtime_observability_settings(
    request_body=request_body,
    id_="id"
)

print(result)
```

## async_get_runtime_observability_settings

Returns a token for the specified RuntimeObservabilitySettings.

- HTTP Method: `GET`
- Endpoint: `/async/RuntimeObservabilitySettings/{id}`

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

result = sdk.runtime_observability_settings.async_get_runtime_observability_settings(id_="id")

print(result)
```

## async_token_runtime_observability_settings

For a response, use the token from the initial GET response in a new request.

- HTTP Method: `GET`
- Endpoint: `/async/RuntimeObservabilitySettings/response/{token}`

**Parameters**

| Name  | Type | Required | Description                                                 |
| :---- | :--- | :------- | :---------------------------------------------------------- |
| token | str  | ✅       | Takes in the token from a previous call to return a result. |

**Return Type**

`RuntimeObservabilitySettingsAsyncResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.runtime_observability_settings.async_token_runtime_observability_settings(token="token")

print(result)
```
