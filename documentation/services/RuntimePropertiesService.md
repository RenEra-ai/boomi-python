# RuntimePropertiesService

A list of all methods in the `RuntimePropertiesService` service. Click on the method name to view detailed information about that method.

| Methods                                                                         | Description                                                                    |
| :------------------------------------------------------------------------------ | :----------------------------------------------------------------------------- |
| [update_runtime_properties](#update_runtime_properties)                         | Updates the RuntimeProperties object having the specified ID.                 |
| [async_get_runtime_properties](#async_get_runtime_properties)                   | Returns a token for the specified RuntimeProperties.                          |
| [async_token_runtime_properties](#async_token_runtime_properties)               | For a response, use the token from the initial GET response in a new request. |

## update_runtime_properties

Updates the RuntimeProperties object having the specified ID.

- HTTP Method: `POST`
- Endpoint: `/RuntimeProperties/{id}`

**Parameters**

| Name         | Type                                                      | Required | Description       |
| :----------- | :-------------------------------------------------------- | :------- | :---------------- |
| request_body | [RuntimeProperties](../models/RuntimeProperties.md)       | ❌       | The request body. |
| id\_         | str                                                       | ✅       |                   |

**Return Type**

`RuntimeProperties`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import RuntimeProperties

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = RuntimeProperties()

result = sdk.runtime_properties.update_runtime_properties(
    request_body=request_body,
    id_="id"
)

print(result)
```

## async_get_runtime_properties

Returns a token for the specified RuntimeProperties.

- HTTP Method: `GET`
- Endpoint: `/async/RuntimeProperties/{id}`

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

result = sdk.runtime_properties.async_get_runtime_properties(id_="id")

print(result)
```

## async_token_runtime_properties

For a response, use the token from the initial GET response in a new request.

- HTTP Method: `GET`
- Endpoint: `/async/RuntimeProperties/response/{token}`

**Parameters**

| Name  | Type | Required | Description                                                 |
| :---- | :--- | :------- | :---------------------------------------------------------- |
| token | str  | ✅       | Takes in the token from a previous call to return a result. |

**Return Type**

`RuntimePropertiesAsyncResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.runtime_properties.async_token_runtime_properties(token="token")

print(result)
```
