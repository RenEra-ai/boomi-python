# CancelExecutionService

A list of all methods in the `CancelExecutionService` service. Click on the method name to view detailed information about that method.

| Methods                                 | Description                                                  |
| :-------------------------------------- | :----------------------------------------------------------- |
| [cancel_execution](#cancel_execution)   | Cancels the execution having the specified execution ID.     |

## cancel_execution

Cancels the execution having the specified execution ID.

- HTTP Method: `POST`
- Endpoint: `/cancelExecution/{executionId}`

**Parameters**

| Name          | Type | Required | Description                       |
| :------------ | :--- | :------- | :-------------------------------- |
| execution\_id | str  | ✅       | The execution ID to cancel.       |

**Return Type**

`None`

**Example Usage Code Snippet**

```python
from boomi import Boomi

sdk = Boomi(
    access_token="YOUR_ACCESS_TOKEN",
    username="YOUR_USERNAME",
    password="YOUR_PASSWORD",
    timeout=10000
)

sdk.cancel_execution.cancel_execution(execution_id="YOUR_EXECUTION_ID")
```
