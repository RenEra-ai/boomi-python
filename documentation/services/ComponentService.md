# ComponentService

A list of all methods in the `ComponentService` service. Click on the method name to view detailed information about that method.

| Methods                                       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| :-------------------------------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [create_component](#create_component)         | - Cannot create components for types not eligible for your account. For example, if your account does not have the B2B/EDI feature, you will not be able to create Trading Partner components. - Request will not be processed in case if the payload has invalid attributes and tags under the \<object\> section. - Include the `branchId` in the request body to specify a branch on which you want to create the component. - \>**Note:** To create or update a component, you must supply a valid component XML format for the given type. The component XML can be rather complex with many optional fields and nested configuration. For this reason we strongly recommend approaching it by first creating the desired component structure/skeleton as you would normally in the Build page UI, then exporting the XML using the Component object GET. This will provide an accurate example or template of the XML you will need to create. You can replace values or continue that pattern as you need for your use case. |
| [get_component](#get_component)               | - When using the GET operation by componentId, it returns the latest component if you do not provide the version. - When you provide the version in the format of `\<componentId\>` ~ `\<version\>`, it returns the specific version of the component. - The GET operation only accepts mediaType `application/xml` for the API response. - The limit is 5 requests for the BULK GET operation. All other API objects have a limit of 100 BULK GET requests. - If you want information for a component on a specific branch, include the branchId in the GET request: `https://api.boomi.com/api/rest/v1/{accountId}/Component/{componentId}~{branchId}`                                                                                                                                                                                                                                                                                                                                                                            |
| [update_component](#update_component)         | - Full updates only. No partial updates. If part of the object’s configuration is omitted, the component will be updated without that configuration. - The only exception is for encrypted fields such as passwords. Omitting an encrypted field from the update request will NOT impact the saved value. - Requests without material changes to configuration will be rejected to prevent unnecessary revisions. - Request will not be processed in case if the payload has invalid attributes and tags under the `\<object\>` section. - For the saved process property components, modifications to the data type are not permitted. - Include the `branchId` in the request body to specify the branch on which you want to update the component. - \>**Note:** To create or update a component, you must supply a valid component XML format for the given type.                                                                                                                                                               |
| [bulk_component_raw](#bulk_component_raw)     | Returns the raw XML response from the Component bulk endpoint without parsing.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [bulk_component](#bulk_component)             | Returns a list of raw component XML strings from successful bulk GET results.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| [get_component_raw](#get_component_raw)       | Returns the raw component XML exactly as the API sends it.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| [update_component_raw](#update_component_raw) | Updates a component using a raw XML payload and returns the raw XML response.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |
| [get_component_etree](#get_component_etree)   | Returns the component XML as an `ElementTree` element for DOM-style edits.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| [update_component_etree](#update_component_etree) | Updates a component from an `ElementTree` element and returns the raw XML response. |

## create_component

- Cannot create components for types not eligible for your account. For example, if your account does not have the B2B/EDI feature, you will not be able to create Trading Partner components. - Request will not be processed in case if the payload has invalid attributes and tags under the \<object\> section. - Include the `branchId` in the request body to specify a branch on which you want to create the component. - \>**Note:** To create or update a component, you must supply a valid component XML format for the given type. The component XML can be rather complex with many optional fields and nested configuration. For this reason we strongly recommend approaching it by first creating the desired component structure/skeleton as you would normally in the Build page UI, then exporting the XML using the Component object GET. This will provide an accurate example or template of the XML you will need to create. You can replace values or continue that pattern as you need for your use case.

- HTTP Method: `POST`
- Endpoint: `/Component`

**Parameters**

| Name         | Type                    | Required | Description       |
| :----------- | :---------------------- | :------- | :---------------- |
| request_body | str                     | ❌       | The request body. |

**Return Type**

`Component`

**Example Usage Code Snippet**

```python
from boomi import Boomi
sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    account_id="YOUR_ACCOUNT_ID",
    timeout=10000
)

with open("file.ext", "r") as f:
    request_body = f.read()

result = sdk.component.create_component(request_body=request_body)

print(result)
```

> **Response handling:** The Component endpoint only supports `application/xml`
> responses, so `create_component`, `get_component`, and `update_component`
> request and parse XML. On success they return a `Component` whose
> `_original_xml` and `object_xml` fields are populated, so the model can be
> round-tripped back through `update_component` via `to_xml()` without losing
> the original structure. If a successful (2xx) XML response cannot be mapped
> onto the model, the raw XML string is returned instead (per the declared
> `Union[Component, str]` return type) so a created component's id is never
> lost.

## get_component

- When using the GET operation by componentId, it returns the latest component if you do not provide the version. - When you provide the version in the format of `\<componentId\>` ~ `\<version\>`, it returns the specific version of the component. - The GET operation only accepts mediaType `application/xml` for the API response. - The limit is 5 requests for the BULK GET operation. All other API objects have a limit of 100 BULK GET requests. - If you want information for a component on a specific branch, include the branchId in the GET request: `https://api.boomi.com/api/rest/v1/{accountId}/Component/{componentId}~{branchId}`

- HTTP Method: `GET`
- Endpoint: `/Component/{componentId}`

**Parameters**

| Name         | Type | Required | Description                                                                                                                                                                                                                                |
| :----------- | :--- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| component_id | str  | ✅       | The ID of the component. The component ID is available on the Revision History dialog, which you can access from the Build page in the service. This must be omitted for the CREATE operation but it is required for the UPDATE operation. |

**Return Type**

`Component`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    account_id="YOUR_ACCOUNT_ID",
    timeout=10000
)

result = sdk.component.get_component(component_id="componentId")

print(result)
```

## update_component

- Full updates only. No partial updates. If part of the object’s configuration is omitted, the component will be updated without that configuration. - The only exception is for encrypted fields such as passwords. Omitting an encrypted field from the update request will NOT impact the saved value. - Requests without material changes to configuration will be rejected to prevent unnecessary revisions. - Request will not be processed in case if the payload has invalid attributes and tags under the `\<object\>` section. - For the saved process property components, modifications to the data type are not permitted. - Include the `branchId` in the request body to specify the branch on which you want to update the component. - \>**Note:** To create or update a component, you must supply a valid component XML format for the given type.

- HTTP Method: `POST`
- Endpoint: `/Component/{componentId}`

**Parameters**

| Name         | Type                    | Required | Description                                                                                                                                                                                                                                |
| :----------- | :---------------------- | :------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| request_body | Component \| str        | ❌       | A `Component` instance with XML preservation support or a raw XML string.                                                                                                                                                                 |
| component_id | str                     | ✅       | The ID of the component. The component ID is available on the Revision History dialog, which you can access from the Build page in the service. This must be omitted for the CREATE operation but it is required for the UPDATE operation. |

**Return Type**

`Component`

**Example Usage Code Snippet**

```python
from boomi import Boomi
sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    account_id="YOUR_ACCOUNT_ID",
    timeout=10000
)

with open("file.ext", "r") as f:
    request_body = f.read()

result = sdk.component.update_component(
    request_body=request_body,
    component_id="componentId"
)

print(result)
```

## bulk_component_raw

Returns the raw XML response from the Component bulk endpoint without parsing.

- HTTP Method: `POST`
- Endpoint: `/Component/bulk`

**Parameters**

| Name         | Type                                                      | Required | Description       |
| :----------- | :-------------------------------------------------------- | :------- | :---------------- |
| request_body | [ComponentBulkRequest](../models/ComponentBulkRequest.md) | ❌       | The request body. |

**Return Type**

`str`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import ComponentBulkRequest

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    account_id="YOUR_ACCOUNT_ID",
    timeout=10000
)

request_body = ComponentBulkRequest(
    request=[
        {
            "id_": "56789abc-def0-1234-5678-9abcdef01234"
        }
    ],
    type_="GET"
)

xml_response = sdk.component.bulk_component_raw(request_body=request_body)

print(xml_response[:200])
```

## bulk_component

The limit for the BULK GET operation is 5 requests. All other API objects have a limit of 100 BULK GET requests. To learn more about `bulk`, refer to [Bulk GET operations](#section/Introduction/Bulk-GET-operations).

- HTTP Method: `POST`
- Endpoint: `/Component/bulk`

**Parameters**

| Name         | Type                                                      | Required | Description       |
| :----------- | :-------------------------------------------------------- | :------- | :---------------- |
| request_body | [ComponentBulkRequest](../models/ComponentBulkRequest.md) | ❌       | The request body. |

**Return Type**

`List[str]`

**Example Usage Code Snippet**

```python
from boomi import Boomi
from boomi.models import ComponentBulkRequest

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    account_id="YOUR_ACCOUNT_ID",
    timeout=10000
)

request_body = ComponentBulkRequest(
    request=[
        {
            "id_": "56789abc-def0-1234-5678-9abcdef01234"
        }
    ],
    type_="GET"
)

result = sdk.component.bulk_component(request_body=request_body)

for component_xml in result:
    print(component_xml[:200])
```

## get_component_raw

Returns the raw component XML exactly as the API sends it.

- HTTP Method: `GET`
- Endpoint: `/Component/{componentId}`

**Parameters**

| Name         | Type | Required | Description          |
| :----------- | :--- | :------- | :------------------- |
| component_id | str  | ✅       | The ID of the component. |

**Return Type**

`str`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    account_id="YOUR_ACCOUNT_ID",
    timeout=10000
)

xml_response = sdk.component.get_component_raw(component_id="componentId")

print(xml_response[:200])
```

## update_component_raw

Updates a component using a raw XML payload and returns the raw XML response.

- HTTP Method: `POST`
- Endpoint: `/Component/{componentId}`

**Parameters**

| Name         | Type | Required | Description              |
| :----------- | :--- | :------- | :----------------------- |
| component_id | str  | ✅       | The ID of the component. |
| xml          | str  | ✅       | Raw XML content to send. |

**Return Type**

`str`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    account_id="YOUR_ACCOUNT_ID",
    timeout=10000
)

with open("component.xml", "r") as f:
    xml_body = f.read()

xml_response = sdk.component.update_component_raw(
    component_id="componentId",
    xml=xml_body
)

print(xml_response[:200])
```

## get_component_etree

Returns the component XML as an `ElementTree` element for DOM-style edits.

- HTTP Method: `GET`
- Endpoint: `/Component/{componentId}`

**Parameters**

| Name         | Type | Required | Description              |
| :----------- | :--- | :------- | :----------------------- |
| component_id | str  | ✅       | The ID of the component. |

**Return Type**

`xml.etree.ElementTree.Element`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    account_id="YOUR_ACCOUNT_ID",
    timeout=10000
)

element = sdk.component.get_component_etree(component_id="componentId")

print(element.tag)
```

## update_component_etree

Updates a component from an `ElementTree` element and returns the raw XML response.

- HTTP Method: `POST`
- Endpoint: `/Component/{componentId}`

**Parameters**

| Name         | Type                           | Required | Description                 |
| :----------- | :----------------------------- | :------- | :-------------------------- |
| component_id | str                            | ✅       | The ID of the component.    |
| element      | xml.etree.ElementTree.Element  | ✅       | The XML element to serialize. |

**Return Type**

`str`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    account_id="YOUR_ACCOUNT_ID",
    timeout=10000
)

element = sdk.component.get_component_etree(component_id="componentId")
xml_response = sdk.component.update_component_etree(
    component_id="componentId",
    element=element
)

print(xml_response[:200])
```
