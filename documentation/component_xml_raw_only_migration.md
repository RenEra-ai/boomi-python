# Migrating to opaque / raw-only Component XML (v3.0.0)

In v3.0.0 the Component endpoints (and the open-ended component-family
endpoints) treat XML as an **opaque payload**: they send and return raw `bytes`
that are byte-for-byte identical to a direct REST call. This guide shows how to
update calling code.

## What changed

| Before (≤ 2.x)                                             | After (3.0.0)                                                        |
| :-------------------------------------------------------- | :------------------------------------------------------------------ |
| `create/get/update_component` returned a `Component`      | They return raw XML `bytes`                                          |
| `update_component(id, component_model)`                   | `update_component(id, raw_xml_str_or_bytes)`                         |
| `bulk_component(...)` returned `List[str]`                | Returns the whole raw XML envelope (`bytes`)                         |
| `component.name`, `component.component_id`, `component.object` | `extract_component_xml_metadata(raw)["name"]` / `["componentId"]`, or parse with `ElementTree` |
| `component.to_xml()`                                      | The raw GET response **is** the full XML — use it directly          |
| `get_component_etree()` / `update_component_etree()`      | GET raw → edit with `ElementTree` yourself → `update_component(raw)` |

The same applies to `TradingPartnerComponentService`,
`OrganizationComponentService`, and `SharedCommunicationChannelComponentService`
`create_*`/`get_*`/`update_*` (their `query_*`/`bulk_*`/`delete_*` are unchanged).

## Reading fields from a result

```python
from boomi import extract_component_xml_metadata
import xml.etree.ElementTree as ET

raw = sdk.component.get_component(component_id="abc")   # bytes

# Root attributes (read-only, XXE-safe):
meta = extract_component_xml_metadata(raw)
name = meta.get("name")
component_id = meta.get("componentId")

# Or parse the whole document yourself (ET.fromstring accepts bytes):
root = ET.fromstring(raw)
```

## Editing and updating

The SDK never parses or re-serializes your XML — you own that step, and do it
exactly once:

```python
import xml.etree.ElementTree as ET

raw = sdk.component.get_component(component_id="abc")
root = ET.fromstring(raw)
root.set("description", "new description")
updated_xml = ET.tostring(root, encoding="unicode")   # serialize once

sdk.component.update_component(component_id="abc", request_body=updated_xml)
```

## Truthiness / error handling

`get_component` returns truthy bytes on success and raises `ApiError` on
non-2xx. Replace `if not component:` checks with `try/except`:

```python
from boomi.net.transport.api_error import ApiError

try:
    raw = sdk.component.get_component(component_id="abc")
except ApiError as exc:
    print("not found:", exc.status)
```

## Rejected inputs

Passing anything other than raw `str`/`bytes` to a write raises before any HTTP
call is made:

```python
from boomi import UnsafeComponentXmlSerializationError

try:
    sdk.component.update_component("abc", some_component_model)  # or dict / Element
except UnsafeComponentXmlSerializationError:
    ...  # pass the raw XML string/bytes instead
```

## Encoding note

A `str` body is transmitted as UTF-8 regardless of any `encoding="..."`
declaration in the XML. For byte-exact round-trips of non-UTF-8 documents, pass
`bytes` (and read with the bytes returned by `get_component`).

## bulk_component

```python
import xml.etree.ElementTree as ET

envelope = sdk.component.bulk_component(request_body=bulk_request)  # bytes
root = ET.fromstring(envelope)
ns = {"bns": "http://api.platform.boomi.com/"}
for resp in root.findall("bns:response", ns):
    if resp.get("statusCode") == "200":
        comp = resp.find("bns:Result/bns:Component", ns)
        print(comp.get("componentId"))
```
