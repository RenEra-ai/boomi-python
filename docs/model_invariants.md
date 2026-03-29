# Model Invariants

Rules for maintaining the 853 model files in `src/boomi/models/`. These files were originally generated and are now manually maintained — there is no code generator in this repo.

## Constructor Rules

### SENTINEL defaults

All model constructor params should default to `SENTINEL` unless there is a proven reason to require them. Assignment must be guarded:

```python
def __init__(self, field_name: SomeType = SENTINEL, **kwargs):
    if field_name is not SENTINEL:
        self.field_name = field_name
```

**Why:** The Boomi API frequently returns sparse payloads where "required" schema fields are omitted. Required positional args cause `TypeError` on deserialization. (BUG-09)

### When required positional args are acceptable

Only for **request models** where the field is truly mandatory to construct a valid API call. Currently these are:

- `*QueryConfig` models — `expression` is always required to form a query
- `QueryFilter` — `expression` is required
- `AsyncToken` — `token` is required
- `SimpleLookupTableRow` — `ref1`, `ref2` are required
- `Privilege` — `name` is required

**Test:** If the model appears in an API _response_ deserialization path, it should NOT have required positional args.

## Bulk Response Pattern

Two-level wrapper: `*BulkResponse` → `*BulkResponseResponse`.

```
*BulkResponse
  └── response: List[*BulkResponseResponse]  (optional, SENTINEL)
        ├── result: *Model  (optional — error items lack this)
        ├── index: int
        ├── id_: str
        ├── status_code: int
        └── error_message: str  (only on errors)
```

All fields in the inner response must be optional. Error items from the API omit `Result`. (BUG-10)

**Fix script:** `scripts/fix_bulk_response_result.py` — applies the pattern across all 45 bulk response models.

## Async Response Pattern

```
*AsyncResponse
  ├── response_status_code: int = SENTINEL  (NOT required)
  ├── number_of_results: int = SENTINEL
  └── result: List[*Model] = SENTINEL
```

The API returns only `responseStatusCode: 202` for in-progress async operations. All fields must be optional. (BUG-09)

**Fix script:** `scripts/fix_async_response_required_args.py` — applies the pattern across all async response models.

## List Auto-Wrap (base_model.py)

When `_define_object()` receives a list and the target class has exactly one `@JsonMap` entry, it auto-wraps: `{wrapper_key: list_data}`.

This handles wrapper models like `MapExtensionsInputs` where the API returns `{"Input": [...]}` but user code may pass `[...]` directly. (BUG-11)

**Guard:** `len(json_mapping) == 1` — only fires for single-field wrapper models.

**False-positive risk:** 280 models have exactly 1 json_mapping entry but aren't wrappers (e.g., `"type_": "type"`). This is safe because `_define_object` only receives list input when the API returns a list where an object is expected, which doesn't happen for these models.

## xmltodict Single-Dict Handling (base_model.py)

`_define_list()` auto-wraps a single dict into `[dict]` because xmltodict returns a bare dict instead of a 1-element list for single XML child elements.

## XML Int Coercion

`parse_xml_to_dict()` returns all values as strings. Fields typed as `int` in the model (`response_status_code`, `number_of_results`) must cast explicitly:

```python
if response_status_code is not SENTINEL:
    self.response_status_code = int(response_status_code)
if number_of_results is not SENTINEL:
    self.number_of_results = int(number_of_results)
```

Applies to all 13 async response models plus `AsyncOperationTokenResult` and `ReleaseIntegrationPackStatus`.

**Fix script:** `scripts/fix_int_coercion.py` — applies `int()` casts across all affected models.

## Batch Fix Scripts

When a bug class affects many models, use a script in `scripts/` rather than hand-editing each file. Pattern:

1. Write a script that uses regex to find and transform the affected pattern
2. Run it, verify the output
3. Run the regression suite
4. Keep the script for future reference (e.g., after a schema update)

Scripts are maintenance tools, not part of the runtime.

## Release Gate Checklist

Before bumping version and publishing:

1. `make test` passes (full suite)
2. `make test-coverage` passes (>=80% coverage)
3. `make verify-schema` passes (all fix scripts idempotent, regression matrix green)
4. No generated model file has been manually patched without a corresponding entry in `scripts/`
5. If BaseModel or JsonMap was modified: run `tests/test_define_object_autowrap.py` and `tests/test_model_invariants.py` explicitly
6. If a new bulk response or async response model was added: verify it follows the patterns above (or run the relevant fix script)

## When to update this document

- New bug class discovered: add a section with the pattern and fix script reference
- Fix script added or modified: update the relevant section
- BaseModel/JsonMap behavior changed: update the relevant section and note the blast radius
