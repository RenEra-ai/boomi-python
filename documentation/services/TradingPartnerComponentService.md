# TradingPartnerComponentService

> **Breaking change (v3.0.0): the component XML payload is now opaque / raw-only.**
> `create_trading_partner_component`, `get_trading_partner_component`, and
> `update_trading_partner_component` now send and return **raw XML `bytes`**
> (byte-for-byte identical to a direct REST call) instead of a typed
> `TradingPartnerComponent` model. Write bodies must be raw `str`/`bytes`;
> passing a model/dict/ElementTree raises `UnsafeComponentXmlSerializationError`.
> Read root attributes from the returned bytes with
> `boomi.extract_component_xml_metadata(xml)`. The `query_*`, `bulk_*`, and
> `delete_*` methods are unchanged (still typed). See
> [ComponentService](./ComponentService.md) for the full rationale and examples.

A list of all methods in the `TradingPartnerComponentService` service. Click on the method name to view detailed information about that method.

| Methods                                                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| :---------------------------------------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [create_trading_partner_component](#create_trading_partner_component)         | - This operation creates a Trading Partner Component object with a specified component name. - The request body requires the standard, classification, and componentName fields. If you omit the folderName field, you must use the folderId field — and vice versa. If you omit the componentID field and the IDs of any certificates you want to create, their values are assigned when you create the components. If you leave off the folderID field when creating a component, it assigns a value. - Includes the organizationId field only if the trading partner is to reference an Organization component, in which case the field value is the ID of the Organization component. A request specifying the organizationId field populates the ContactInformation fields with the data from the referenced Organization component.                                                                                                                                                                         |
| [get_trading_partner_component](#get_trading_partner_component)               | The ordinary GET operation returns a single Trading Partner Component object based on the supplied ID. A GET operation specifying the ID of a deleted Trading Partner component retrieves the component. In the component, the deleted field’s value is true.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [update_trading_partner_component](#update_trading_partner_component)         | This operation overwrites the Trading Partner Component object with the specified component ID except as described: - If the fields are empty, an UPDATE operation specifying the organizationId field populates the ContactInformation fields with the data from the referenced Organization component. However, if those fields have values, they are not overwritten. An UPDATE operation specifying the ID of a deleted Trading Partner component restores the component to a non-deleted state, assuming the request is otherwise valid.                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [delete_trading_partner_component](#delete_trading_partner_component)         | The DELETE operation deletes the Trading Partner Component object with a specific component ID. A DELETE operation specifying the ID of a deleted Trading Partner component returns a false response.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [bulk_trading_partner_component](#bulk_trading_partner_component)             | The bulk GET operation returns multiple Trading Partner Component objects based on the supplied IDs, to a maximum of 100.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [query_trading_partner_component](#query_trading_partner_component)           | The QUERY operation returns each Trading Partner component that meets the specified filtering criteria. - The name field in a QUERY filter represents the object’s componentName field. - Only the LIKE operator is allowed with a name filter. Likewise, you can only use the EQUALS operator with a classification, standard, identifier filter, or a communication method filter (as2, disk, ftp, http, mllp, sftp). Filtering on a communication method field requests Trading Partner components by defining the communication method. - If the QUERY request includes multiple filters, you can connect the filters with a logical AND operator. The QUERY request does not support the logical OR operator. - The QUERY results omit the folderName field. For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging). |
| [query_more_trading_partner_component](#query_more_trading_partner_component) | To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |
| [create_trading_partner_component_json](#create_trading_partner_component_json) | JSON create (additive, v3.0.1). Accepts a typed `TradingPartnerComponent` or a plain `dict` (sent as-is for a lossless JSON write); returns `Union[TradingPartnerComponent, str, dict]`. |
| [get_trading_partner_component_json](#get_trading_partner_component_json) | JSON get (additive, v3.0.1). Returns `Union[TradingPartnerComponent, str, dict]`; a sparse 2xx body falls back to the raw `dict`. |
| [update_trading_partner_component_json](#update_trading_partner_component_json) | JSON update (additive, v3.0.1). Accepts a typed `TradingPartnerComponent` or a plain `dict`; returns `Union[TradingPartnerComponent, str, dict]`. |

## create_trading_partner_component

Create a Trading Partner Component from raw XML; returns the raw XML response bytes. The component
XML payload is **opaque / raw-only** — see [ComponentService](./ComponentService.md)
for the full rationale and helpers.

- HTTP Method: `POST`
- Endpoint: `/TradingPartnerComponent`

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

raw_xml = sdk.trading_partner_component.create_trading_partner_component(request_body=request_body)
print(extract_component_xml_metadata(raw_xml).get("componentId"))
```

## get_trading_partner_component

Get a Trading Partner Component as raw XML response bytes, without parsing.

- HTTP Method: `GET`
- Endpoint: `/TradingPartnerComponent/{id}`

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

raw_xml = sdk.trading_partner_component.get_trading_partner_component(id_="id")
root = ET.fromstring(raw_xml)            # ET.fromstring accepts bytes
print(root.get("componentName") or root.get("name"))
```

## update_trading_partner_component

Update a Trading Partner Component with raw XML (full updates only); returns the raw XML response
bytes. GET the raw XML, edit it yourself, serialize once, and pass it back.

- HTTP Method: `POST`
- Endpoint: `/TradingPartnerComponent/{id}`

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

raw_xml = sdk.trading_partner_component.update_trading_partner_component(id_="id", request_body=body)
print(raw_xml[:200])
```

## delete_trading_partner_component

The DELETE operation deletes the Trading Partner Component object with a specific component ID. A DELETE operation specifying the ID of a deleted Trading Partner component returns a false response.

- HTTP Method: `DELETE`
- Endpoint: `/TradingPartnerComponent/{id}`

**Parameters**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| id\_ | str  | ✅       |             |

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

result = sdk.trading_partner_component.delete_trading_partner_component(id_="id")

print(result)
```

## bulk_trading_partner_component

The bulk GET operation returns multiple Trading Partner Component objects based on the supplied IDs, to a maximum of 100.

- HTTP Method: `POST`
- Endpoint: `/TradingPartnerComponent/bulk`

**Parameters**

| Name         | Type                                                                                  | Required | Description       |
| :----------- | :------------------------------------------------------------------------------------ | :------- | :---------------- |
| request_body | [TradingPartnerComponentBulkRequest](../models/TradingPartnerComponentBulkRequest.md) | ❌       | The request body. |

**Return Type**

`bytes` — the whole raw XML bulk-response envelope, returned byte-for-byte. The SDK does not split it into per-component fragments (which would be lossy and would drop non-200 entries); parse the envelope yourself if you need individual components.

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import TradingPartnerComponentBulkRequest

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = TradingPartnerComponentBulkRequest(
    request=[
        {
            "id_": "56789abc-def0-1234-5678-9abcdef01234"
        }
    ],
    type_="GET"
)

result = sdk.trading_partner_component.bulk_trading_partner_component(request_body=request_body)

print(result)
```

## query_trading_partner_component

The QUERY operation returns each Trading Partner component that meets the specified filtering criteria. - The name field in a QUERY filter represents the object’s componentName field. - Only the LIKE operator is allowed with a name filter. Likewise, you can only use the EQUALS operator with a classification, standard, identifier filter, or a communication method filter (as2, disk, ftp, http, mllp, sftp). Filtering on a communication method field requests Trading Partner components by defining the communication method. - If the QUERY request includes multiple filters, you can connect the filters with a logical AND operator. The QUERY request does not support the logical OR operator. - The QUERY results omit the folderName field. For general information about the structure of QUERY filters, their sample payloads, and how to handle the paged results, refer to [Query filters](#section/Introduction/Query-filters) and [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/TradingPartnerComponent/query`

**Parameters**

| Name         | Type                                                                                  | Required | Description       |
| :----------- | :------------------------------------------------------------------------------------ | :------- | :---------------- |
| request_body | [TradingPartnerComponentQueryConfig](../models/TradingPartnerComponentQueryConfig.md) | ❌       | The request body. |

**Return Type**

`TradingPartnerComponentQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import TradingPartnerComponentQueryConfig

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = TradingPartnerComponentQueryConfig(
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

result = sdk.trading_partner_component.query_trading_partner_component(request_body=request_body)

print(result)
```

## query_more_trading_partner_component

To learn about using `queryMore`, refer to [Query paging](#section/Introduction/Query-paging).

- HTTP Method: `POST`
- Endpoint: `/TradingPartnerComponent/queryMore`

**Parameters**

| Name         | Type | Required | Description       |
| :----------- | :--- | :------- | :---------------- |
| request_body | str  | ✅       | The request body. |

**Return Type**

`TradingPartnerComponentQueryResponse`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

request_body = "sint esse l"

result = sdk.trading_partner_component.query_more_trading_partner_component(request_body=request_body)

print(result)
```


## create_trading_partner_component_json

Create a Trading Partner Component from JSON (additive, v3.0.1). JSON counterpart of `create_trading_partner_component` (raw
XML), for callers who prefer JSON over hand-authoring component XML. The endpoint
also accepts/returns JSON in the Boomi Platform API.

- HTTP Method: `POST`
- Endpoint: `/TradingPartnerComponent`

**Parameters**

| Name         | Type                 | Required | Description                                                               |
| :----------- | :------------------- | :------- | :------------------------------------------------------------------------ |
| request_body | TradingPartnerComponent \| dict | ❌       | Typed model (serialized via `_map()`) or a plain `dict` (sent as-is, lossless). |

**Return Type**

`Union[TradingPartnerComponent, str, dict]` — the typed model when the response maps onto it, otherwise
the raw response content (`dict`) on a sparse 2xx body. A `dict` request body is sent
byte-faithfully; a typed model body is model-lossless only for fields the generated
model knows.

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(account_id="...", username="...", password="...", timeout=10000)

result = sdk.trading_partner_component.create_trading_partner_component_json(request_body={"componentName": "Example"})
print(result)
```

## get_trading_partner_component_json

Get a Trading Partner Component as JSON (additive, v3.0.1). JSON counterpart of `get_trading_partner_component` (raw XML).

- HTTP Method: `GET`
- Endpoint: `/TradingPartnerComponent/{id}`

**Parameters**

| Name | Type | Required | Description              |
| :--- | :--- | :------- | :----------------------- |
| id_  | str  | ✅       | The ID of the component. |

**Return Type**

`Union[TradingPartnerComponent, str, dict]` — the typed model when the response maps onto it; a sparse
2xx body (the model requires `partner_communication` to hydrate) is returned as the raw `dict` rather than raising.

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(account_id="...", username="...", password="...", timeout=10000)

result = sdk.trading_partner_component.get_trading_partner_component_json(id_="id")
print(result)
```

## update_trading_partner_component_json

Update a Trading Partner Component with JSON (additive, v3.0.1; full updates only). JSON counterpart of
`update_trading_partner_component` (raw XML).

- HTTP Method: `POST`
- Endpoint: `/TradingPartnerComponent/{id}`

**Parameters**

| Name         | Type                 | Required | Description                                                               |
| :----------- | :------------------- | :------- | :------------------------------------------------------------------------ |
| id_          | str                  | ✅       | The ID of the component.                                                  |
| request_body | TradingPartnerComponent \| dict | ❌       | Typed model (serialized via `_map()`) or a plain `dict` (sent as-is, lossless). |

**Return Type**

`Union[TradingPartnerComponent, str, dict]` — see `create_trading_partner_component_json`.

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(account_id="...", username="...", password="...", timeout=10000)

current = sdk.trading_partner_component.get_trading_partner_component_json(id_="id")
result = sdk.trading_partner_component.update_trading_partner_component_json(id_="id", request_body=current)
print(result)
```
