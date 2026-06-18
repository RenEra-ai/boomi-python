# SharedCommunicationChannelComponentService

> **Breaking change (v3.0.0): the component XML payload is now opaque / raw-only.**
> `create_shared_communication_channel_component`,
> `get_shared_communication_channel_component`, and
> `update_shared_communication_channel_component` now send and return **raw XML
> `bytes`** (byte-for-byte identical to a direct REST call) instead of a typed
> `SharedCommunicationChannelComponent` model. Write bodies must be raw
> `str`/`bytes`; passing a model/dict/ElementTree raises
> `UnsafeComponentXmlSerializationError`. Read root attributes from the returned
> bytes with `boomi.extract_component_xml_metadata(xml)`. The `query_*`,
> `bulk_*`, and `delete_*` methods are unchanged (still typed). See
> [ComponentService](./ComponentService.md) for the full rationale and examples.

A list of all methods in the `SharedCommunicationChannelComponentService` service. Click on the method name to view detailed information about that method.

| Methods                                                                                                 | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| :------------------------------------------------------------------------------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| [create_shared_communication_channel_component](#create_shared_communication_channel_component)         | The sample request creates a Shared Communication Component named `Disk Comms Channel`.                                                                                                                                                                                                                                                                                                                                                                                         |
| [get_shared_communication_channel_component](#get_shared_communication_channel_component)               | Send an HTTP GET request where `{accountId}` is the ID of the authenticating account for the request and `{componentId}` is the ID of the component being retrieved.                                                                                                                                                                                                                                                                                                            |
| [update_shared_communication_channel_component](#update_shared_communication_channel_component)         | The sample request updates the component named `Disk Comms Channel`.                                                                                                                                                                                                                                                                                                                                                                                                            |
| [delete_shared_communication_channel_component](#delete_shared_communication_channel_component)         | If the Shared Communication Channel component is deleted successfully, the response is `true`.                                                                                                                                                                                                                                                                                                                                                                                  |
| [bulk_shared_communication_channel_component](#bulk_shared_communication_channel_component)             | To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).                                                                                                                                                                                                                                                                                                                                                                          |
| [query_shared_communication_channel_component](#query_shared_communication_channel_component)           | For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging). The sample request query returns the Shared Communication Channel components using the AS2 standard for the authenticating account. \>**Note:** The name field in a QUERY filter represents the object's `componentName` field. |
| [query_more_shared_communication_channel_component](#query_more_shared_communication_channel_component) | To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).                                                                                                                                                                                                                                                                                                                                                                                  |
| [create_shared_communication_channel_component_json](#create_shared_communication_channel_component_json) | JSON create (additive, v3.0.1). Accepts a typed `SharedCommunicationChannelComponent` or a plain `dict` (sent as-is for a lossless JSON write); returns `Union[SharedCommunicationChannelComponent, str, dict]`. |
| [get_shared_communication_channel_component_json](#get_shared_communication_channel_component_json) | JSON get (additive, v3.0.1). Returns `Union[SharedCommunicationChannelComponent, str, dict]`; a sparse 2xx body falls back to the raw `dict`. |
| [update_shared_communication_channel_component_json](#update_shared_communication_channel_component_json) | JSON update (additive, v3.0.1). Accepts a typed `SharedCommunicationChannelComponent` or a plain `dict`; returns `Union[SharedCommunicationChannelComponent, str, dict]`. |

## create_shared_communication_channel_component

Create a Shared Communication Channel Component from raw XML; returns the raw XML response bytes. The component
XML payload is **opaque / raw-only** — see [ComponentService](./ComponentService.md)
for the full rationale and helpers.

- HTTP Method: `POST`
- Endpoint: `/SharedCommunicationChannelComponent`

**Parameters**

| Name         | Type         | Required | Description                            |
| :----------- | :----------- | :------- | :------------------------------------- |
| request_body | str \| bytes | ✅       | Raw component XML, sent byte-for-byte. |

**Return Type**

`bytes` — the raw XML response exactly as returned by the API. Passing a model,
`dict`, or `ElementTree` raises `UnsafeComponentXmlSerializationError`.

**Example Usage Code Snippet**

```python
from boomi import Boomi, extract_component_xml_metadata

sdk = Boomi(
    account_id="YOUR_ACCOUNT_ID",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000,
)

with open("component.xml", "rb") as f:
    request_body = f.read()  # bytes preserve the exact encoding

raw_xml = sdk.shared_communication_channel_component.create_shared_communication_channel_component(request_body=request_body)
print(extract_component_xml_metadata(raw_xml).get("componentId"))
```

## get_shared_communication_channel_component

Get a Shared Communication Channel Component as raw XML response bytes, without parsing.

- HTTP Method: `GET`
- Endpoint: `/SharedCommunicationChannelComponent/{id}`

**Parameters**

| Name | Type | Required | Description              |
| :--- | :--- | :------- | :----------------------- |
| id_  | str  | ✅       | The ID of the component. |

**Return Type**

`bytes` — the raw XML response exactly as returned by the API.

**Example Usage Code Snippet**

```python
import xml.etree.ElementTree as ET
from boomi import Boomi

sdk = Boomi(account_id="...", username="...", password="...", timeout=10000)

raw_xml = sdk.shared_communication_channel_component.get_shared_communication_channel_component(id_="id")
root = ET.fromstring(raw_xml)            # ET.fromstring accepts bytes
print(root.get("componentName") or root.get("name"))
```

## update_shared_communication_channel_component

Update a Shared Communication Channel Component with raw XML (full updates only); returns the raw XML response
bytes. GET the raw XML, edit it yourself, serialize once, and pass it back.

- HTTP Method: `POST`
- Endpoint: `/SharedCommunicationChannelComponent/{id}`

**Parameters**

| Name         | Type         | Required | Description                            |
| :----------- | :----------- | :------- | :------------------------------------- |
| id_          | str          | ✅       | The ID of the component.               |
| request_body | str \| bytes | ✅       | Raw component XML, sent byte-for-byte. |

**Return Type**

`bytes` — the raw XML response exactly as returned by the API. Passing a model,
`dict`, or `ElementTree` raises `UnsafeComponentXmlSerializationError`.

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(account_id="...", username="...", password="...", timeout=10000)

with open("component.xml", "rb") as f:
    body = f.read()

raw_xml = sdk.shared_communication_channel_component.update_shared_communication_channel_component(id_="id", request_body=body)
print(raw_xml[:200])
```

## delete_shared_communication_channel_component

If the Shared Communication Channel component is deleted successfully, the response is `true`.

- HTTP Method: `DELETE`
- Endpoint: `/SharedCommunicationChannelComponent/{id}`

**Parameters**

| Name | Type | Required | Description                                  |
| :--- | :--- | :------- | :------------------------------------------- |
| id\_ | str  | ✅       | ID of the component that you want to delete. |

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.shared_communication_channel_component.delete_shared_communication_channel_component(id_="id")

print(result)
```

## bulk_shared_communication_channel_component

To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

- HTTP Method: `POST`
- Endpoint: `/SharedCommunicationChannelComponent/bulk`

**Parameters**

| Name         | Type                                                                                                          | Required | Description       |
| :----------- | :------------------------------------------------------------------------------------------------------------ | :------- | :---------------- |
| request_body | [SharedCommunicationChannelComponentBulkRequest](../models/SharedCommunicationChannelComponentBulkRequest.md) | ❌       | The request body. |

**Return Type**

`bytes` — the whole raw XML bulk-response envelope, returned byte-for-byte. The SDK does not split it into per-component fragments (which would be lossy and would drop non-200 entries); parse the envelope yourself if you need individual components.

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import SharedCommunicationChannelComponentBulkRequest

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = SharedCommunicationChannelComponentBulkRequest(
    request=[
        {
            "id_": "56789abc-def0-1234-5678-9abcdef01234"
        }
    ],
    type_="GET"
)

result = sdk.shared_communication_channel_component.bulk_shared_communication_channel_component(request_body=request_body)

print(result)
```

## query_shared_communication_channel_component

For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging). The sample request query returns the Shared Communication Channel components using the AS2 standard for the authenticating account. \>**Note:** The name field in a QUERY filter represents the object's `componentName` field.

- HTTP Method: `POST`
- Endpoint: `/SharedCommunicationChannelComponent/query`

**Parameters**

| Name         | Type                                                                                                          | Required | Description       |
| :----------- | :------------------------------------------------------------------------------------------------------------ | :------- | :---------------- |
| request_body | [SharedCommunicationChannelComponentQueryConfig](../models/SharedCommunicationChannelComponentQueryConfig.md) | ❌       | The request body. |

**Return Type**

`SharedCommunicationChannelComponentQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import SharedCommunicationChannelComponentQueryConfig

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = SharedCommunicationChannelComponentQueryConfig(
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

result = sdk.shared_communication_channel_component.query_shared_communication_channel_component(request_body=request_body)

print(result)
```

## query_more_shared_communication_channel_component

To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/SharedCommunicationChannelComponent/queryMore`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | str  | ✅       | The request body. |

**Return Type**

`SharedCommunicationChannelComponentQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = "ea repre"

result = sdk.shared_communication_channel_component.query_more_shared_communication_channel_component(request_body=request_body)

print(result)
```


## create_shared_communication_channel_component_json

Create a Shared Communication Channel Component from JSON (additive, v3.0.1). JSON counterpart of `create_shared_communication_channel_component` (raw
XML), for callers who prefer JSON over hand-authoring component XML. The endpoint
also accepts/returns JSON in the Boomi Platform API.

- HTTP Method: `POST`
- Endpoint: `/SharedCommunicationChannelComponent`

**Parameters**

| Name         | Type                 | Required | Description                                                               |
| :----------- | :------------------- | :------- | :------------------------------------------------------------------------ |
| request_body | SharedCommunicationChannelComponent \| dict | ❌       | Typed model (serialized via `_map()`) or a plain `dict` (sent as-is, lossless). |

**Return Type**

`Union[SharedCommunicationChannelComponent, str, dict]` — the typed model when the response maps onto it, otherwise
the raw response content (`dict`) on a sparse 2xx body. A `dict` request body is sent
byte-faithfully; a typed model body is model-lossless only for fields the generated
model knows.

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(account_id="...", username="...", password="...", timeout=10000)

result = sdk.shared_communication_channel_component.create_shared_communication_channel_component_json(request_body={"componentName": "Example"})
print(result)
```

## get_shared_communication_channel_component_json

Get a Shared Communication Channel Component as JSON (additive, v3.0.1). JSON counterpart of `get_shared_communication_channel_component` (raw XML).

- HTTP Method: `GET`
- Endpoint: `/SharedCommunicationChannelComponent/{id}`

**Parameters**

| Name | Type | Required | Description              |
| :--- | :--- | :------- | :----------------------- |
| id_  | str  | ✅       | The ID of the component. |

**Return Type**

`Union[SharedCommunicationChannelComponent, str, dict]` — the typed model when the response maps onto it; a sparse
2xx body (the model requires `partner_communication` + `partner_archiving` to hydrate) is returned as the raw `dict` rather than raising.

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(account_id="...", username="...", password="...", timeout=10000)

result = sdk.shared_communication_channel_component.get_shared_communication_channel_component_json(id_="id")
print(result)
```

## update_shared_communication_channel_component_json

Update a Shared Communication Channel Component with JSON (additive, v3.0.1; full updates only). JSON counterpart of
`update_shared_communication_channel_component` (raw XML).

- HTTP Method: `POST`
- Endpoint: `/SharedCommunicationChannelComponent/{id}`

**Parameters**

| Name         | Type                 | Required | Description                                                               |
| :----------- | :------------------- | :------- | :------------------------------------------------------------------------ |
| id_          | str                  | ✅       | The ID of the component.                                                  |
| request_body | SharedCommunicationChannelComponent \| dict | ❌       | Typed model (serialized via `_map()`) or a plain `dict` (sent as-is, lossless). |

**Return Type**

`Union[SharedCommunicationChannelComponent, str, dict]` — see `create_shared_communication_channel_component_json`.

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(account_id="...", username="...", password="...", timeout=10000)

current = sdk.shared_communication_channel_component.get_shared_communication_channel_component_json(id_="id")
result = sdk.shared_communication_channel_component.update_shared_communication_channel_component_json(id_="id", request_body=current)
print(result)
```
