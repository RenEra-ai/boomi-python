# AccountGroupIntegrationPackExpression

`AccountGroupIntegrationPackExpression` is a query-filter expression union:
either an [AccountGroupIntegrationPackSimpleExpression](#accountgroupintegrationpacksimpleexpression)
or an [AccountGroupIntegrationPackGroupingExpression](#accountgroupintegrationpackgroupingexpression).
Pass either type as the `expression` of an `AccountGroupIntegrationPackQueryConfig`
query filter.

# AccountGroupIntegrationPackSimpleExpression

**Properties**

| Name     | Type                                                | Required | Description |
| :------- | :-------------------------------------------------- | :------- | :---------- |
| operator | AccountGroupIntegrationPackSimpleExpressionOperator | ✅       |             |
| property | AccountGroupIntegrationPackSimpleExpressionProperty | ✅       |             |
| argument | List[str]                                           | ❌       |             |

# AccountGroupIntegrationPackSimpleExpressionOperator

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

# AccountGroupIntegrationPackSimpleExpressionProperty

**Properties**

| Name           | Type | Required | Description      |
| :------------- | :--- | :------- | :--------------- |
| ACCOUNTGROUPID | str  | ✅       | "accountGroupId" |

# AccountGroupIntegrationPackGroupingExpression

**Properties**

| Name              | Type                                                  | Required | Description |
| :---------------- | :---------------------------------------------------- | :------- | :---------- |
| operator          | AccountGroupIntegrationPackGroupingExpressionOperator | ✅       |             |
| nested_expression | List[AccountGroupIntegrationPackExpression]           | ❌       |             |

# AccountGroupIntegrationPackGroupingExpressionOperator

**Properties**

| Name | Type | Required | Description |
| :--- | :--- | :------- | :---------- |
| AND  | str  | ✅       | "and"       |
| OR   | str  | ✅       | "or"        |
