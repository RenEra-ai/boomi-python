# PublisherIntegrationPackExpression

`PublisherIntegrationPackExpression` is a query-filter expression union:
either a [PublisherIntegrationPackSimpleExpression](#publisherintegrationpacksimpleexpression)
or a [PublisherIntegrationPackGroupingExpression](#publisherintegrationpackgroupingexpression).
Pass either type as the `expression` of a `PublisherIntegrationPackQueryConfig`
query filter.

# PublisherIntegrationPackSimpleExpression

**Properties**

| Name     | Type                                              | Required | Description |
| :------- | :------------------------------------------------ | :------- | :---------- |
| operator | PublisherIntegrationPackSimpleExpressionOperator  | ✅       |             |
| property | PublisherIntegrationPackSimpleExpressionProperty  | ✅       |             |
| argument | List[str]                                         | ❌       |             |

# PublisherIntegrationPackSimpleExpressionOperator

**Properties**

| Name               | Type | Required | Description             |
| :----------------- | :--- | :------- | :---------------------- |
| EQUALS             | str  | ✅       | "EQUALS"                |
| LIKE               | str  | ✅       | "LIKE"                  |
| NOTEQUALS          | str  | ✅       | "NOT_EQUALS"            |
| ISNULL             | str  | ✅       | "IS_NULL"               |
| ISNOTNULL          | str  | ✅       | "IS_NOT_NULL"           |
| BETWEEN            | str  | ✅       | "BETWEEN"               |
| GREATERTHAN        | str  | ✅       | "GREATER_THAN"          |
| GREATERTHANOREQUAL | str  | ✅       | "GREATER_THAN_OR_EQUAL" |
| LESSTHAN           | str  | ✅       | "LESS_THAN"             |
| LESSTHANOREQUAL    | str  | ✅       | "LESS_THAN_OR_EQUAL"    |
| CONTAINS           | str  | ✅       | "CONTAINS"              |
| NOTCONTAINS        | str  | ✅       | "NOT_CONTAINS"          |

# PublisherIntegrationPackSimpleExpressionProperty

**Properties**

| Name             | Type | Required | Description        |
| :--------------- | :--- | :------- | :----------------- |
| NAME             | str  | ✅       | "name"             |
| ID               | str  | ✅       | "id"               |
| INSTALLATIONTYPE | str  | ✅       | "installationType" |

# PublisherIntegrationPackGroupingExpression

**Properties**

| Name              | Type                                                | Required | Description |
| :---------------- | :-------------------------------------------------- | :------- | :---------- |
| operator          | PublisherIntegrationPackGroupingExpressionOperator  | ✅       |             |
| nested_expression | List[PublisherIntegrationPackExpression]            | ❌       |             |

# PublisherIntegrationPackGroupingExpressionOperator

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| AND  | str  | ✅       | "and"       |
| OR   | str  | ✅       | "or"        |
