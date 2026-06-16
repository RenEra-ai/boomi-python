# ComponentService

> **Breaking change (v3.0.0): Component XML is now opaque / raw-only.**
> `create_component`, `get_component`, `update_component` and `bulk_component`
> send and return **raw XML `bytes`** that are byte-for-byte identical to a
> direct REST call. The SDK never parses, hydrates, normalizes, or
> re-serializes Component XML, because Boomi component objects are open-ended and
> cannot be losslessly represented by a generated Python model — attempting it
> silently corrupted XML (namespaces, CDATA, comments, attribute order, unknown
> attributes).
>
> What changed for callers:
> - Return types are now `bytes` (raw XML), not `Component`. Parse client-side
>   with `xml.etree.ElementTree` or read root attributes with the read-only
>   helper `extract_component_xml_metadata(xml)`.
> - Write bodies must be raw `str` or `bytes`. Passing a `Component`, `dict`,
>   `ElementTree` element, or any other object raises
>   `UnsafeComponentXmlSerializationError` **before** the request is sent.
> - `bulk_component` now returns the **whole raw XML envelope** (`bytes`), not a
>   `List[str]` of re-serialized fragments.
> - **Removed:** `Component.to_xml()`, `Component.set_object_xml()`,
>   `get_component_etree()`, `update_component_etree()`. These performed lossy
>   round-trips. To edit a component, GET the raw XML, edit the string/bytes
>   yourself, and pass it back to `update_component`.
> - For non-UTF-8 byte-exact round-trips, prefer passing `bytes` (a `str` body is
>   transmitted as UTF-8 regardless of any `encoding=` declaration in the XML).

A list of all methods in the `ComponentService` service.

| Methods                                       | Description                                                                 |
| :-------------------------------------------- | :------------------------------------------------------------------------- |
| [create_component](#create_component)         | Create a component from raw XML; returns the raw XML response bytes.       |
| [get_component](#get_component)               | Get a component as raw XML response bytes, without parsing.                |
| [update_component](#update_component)         | Update a component with raw XML (full updates only); returns raw XML bytes.|
| [bulk_component](#bulk_component)             | Get multiple components as the whole raw XML bulk-response envelope bytes. |
| [create_component_raw](#create_component_raw) | Alias of `create_component`.                                               |
| [get_component_raw](#get_component_raw)       | Alias of `get_component`.                                                  |
| [update_component_raw](#update_component_raw) | Alias of `update_component`.                                               |
| [bulk_component_raw](#bulk_component_raw)     | Alias of `bulk_component`.                                                 |
| [extract_component_xml_metadata](#extract_component_xml_metadata) | Read-only helper: root `<Component>` attributes from raw XML. |

## create_component

Cannot create components for types not eligible for your account (for example,
Trading Partner components require the B2B/EDI feature). The request will be
rejected if the payload has invalid attributes/tags under the `<object>`
section. Include `branchId` in the request body to target a branch. You must
supply a valid component XML format for the given type — the easiest way to get
a correct template is to build the component in the Build page UI and export it
via `get_component`.

- HTTP Method: `POST`
- Endpoint: `/Component`

**Parameters**

| Name         | Type            | Required | Description                          |
| :----------- | :-------------- | :------- | :----------------------------------- |
| request_body | str \| bytes    | ✅       | Raw component XML, sent byte-for-byte. |

**Return Type**

`bytes` — the raw XML response exactly as returned by the API.

**Raises**

`UnsafeComponentXmlSerializationError` if `request_body` is not raw `str`/`bytes`.

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

raw_xml = sdk.component.create_component(request_body=request_body)
meta = extract_component_xml_metadata(raw_xml)
print("created", meta["componentId"], meta["name"])
```

## get_component

When using GET by `componentId`, the latest component is returned if no version
is provided. Use the format `<componentId>~<version>` for a specific version, or
`<componentId>~<branchId>` for a branch. The GET operation only emits
`application/xml`.

- HTTP Method: `GET`
- Endpoint: `/Component/{componentId}`

**Parameters**

| Name         | Type | Required | Description              |
| :----------- | :--- | :------- | :----------------------- |
| component_id | str  | ✅       | The ID of the component. |

**Return Type**

`bytes` — the raw XML response exactly as returned by the API.

**Example Usage Code Snippet**

```python
import xml.etree.ElementTree as ET
from boomi import Boomi

sdk = Boomi(account_id="...", username="...", password="...", timeout=10000)

raw_xml = sdk.component.get_component(component_id="componentId")
root = ET.fromstring(raw_xml)          # ET.fromstring accepts bytes
print(root.get("name"), root.get("type"))
```

## update_component

Full updates only — no partial updates. Supply the complete component XML you
want persisted (omitted configuration is dropped, except encrypted fields such
as passwords). Requests without material changes are rejected. Include
`branchId` in the body to target a branch.

To edit a component: GET its raw XML, parse/modify it yourself, serialize it
**once**, and pass the result back. The SDK never parses or re-serializes it.

- HTTP Method: `POST`
- Endpoint: `/Component/{componentId}`

**Parameters**

| Name         | Type         | Required | Description                          |
| :----------- | :----------- | :------- | :----------------------------------- |
| component_id | str          | ✅       | The ID of the component.             |
| request_body | str \| bytes | ✅       | Raw component XML, sent byte-for-byte. |

**Return Type**

`bytes` — the raw XML response exactly as returned by the API.

**Raises**

`UnsafeComponentXmlSerializationError` if `request_body` is not raw `str`/`bytes`.

**Example Usage Code Snippet**

```python
import xml.etree.ElementTree as ET
from boomi import Boomi

sdk = Boomi(account_id="...", username="...", password="...", timeout=10000)

raw_xml = sdk.component.get_component(component_id="componentId")
root = ET.fromstring(raw_xml)
root.set("description", "updated via SDK")
updated_xml = ET.tostring(root, encoding="unicode")   # serialize once, on your side

result = sdk.component.update_component(
    component_id="componentId",
    request_body=updated_xml,
)
print(result[:200])
```

## bulk_component

The limit for the BULK GET operation is 5 requests. The request is a typed JSON
query envelope (`ComponentBulkRequest`); the response is returned as the **whole
raw XML bulk envelope** (`bytes`) — the SDK does not split it into per-component
fragments (which would be lossy and would drop non-200 entries). Parse the
envelope yourself if you need individual components.

- HTTP Method: `POST`
- Endpoint: `/Component/bulk`

**Parameters**

| Name         | Type                                                      | Required | Description       |
| :----------- | :-------------------------------------------------------- | :------- | :---------------- |
| request_body | [ComponentBulkRequest](../models/ComponentBulkRequest.md) | ❌       | The request body. |

**Return Type**

`bytes` — the whole raw XML bulk-response envelope.

**Example Usage Code Snippet**

```python
import xml.etree.ElementTree as ET
from boomi import Boomi
from boomi.models import ComponentBulkRequest

sdk = Boomi(account_id="...", username="...", password="...", timeout=10000)

request_body = ComponentBulkRequest(
    request=[{"id_": "56789abc-def0-1234-5678-9abcdef01234"}],
    type_="GET",
)

envelope = sdk.component.bulk_component(request_body=request_body)
root = ET.fromstring(envelope)
ns = {"bns": "http://api.platform.boomi.com/"}
for resp in root.findall("bns:response", ns):
    if resp.get("statusCode") == "200":
        component = resp.find("bns:Result/bns:Component", ns)
        print(component.get("componentId"), component.get("name"))
```

## create_component_raw

Alias of [create_component](#create_component) (raw XML in, raw XML `bytes` out).

## get_component_raw

Alias of [get_component](#get_component) (raw XML `bytes` out).

## update_component_raw

Alias of [update_component](#update_component) (raw XML in, raw XML `bytes` out).

## bulk_component_raw

Alias of [bulk_component](#bulk_component) (whole raw XML envelope `bytes` out).

## extract_component_xml_metadata

A read-only convenience for reading the root `<Component>` attributes from raw
component XML, without parsing the `<object>` subtree and without any ability to
re-serialize XML. Importable as `from boomi import extract_component_xml_metadata`
or `from boomi.services.component import extract_component_xml_metadata`.

**Signature**

```python
extract_component_xml_metadata(xml: str | bytes) -> dict
```

Returns a flat dict of root attributes (e.g. `componentId`, `name`, `type`,
`subType`, `folderId`, `folderName`, `folderFullPath`, `version`, `branchId`,
`branchName`, `currentVersion`, `deleted`, `createdDate`, `createdBy`,
`modifiedDate`, `modifiedBy`). Returns `{}` on a parse error or bad input. It is
hardened against XML entity-expansion / XXE (documents declaring a DOCTYPE or
custom entities are refused, external entities are disabled) and never reads or
exposes the component's `<object>` payload.

```python
from boomi import extract_component_xml_metadata

raw_xml = sdk.component.get_component(component_id="componentId")
meta = extract_component_xml_metadata(raw_xml)
print(meta.get("componentId"), meta.get("name"), meta.get("type"))
```
