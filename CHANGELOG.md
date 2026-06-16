# Changelog

## 3.0.0 — Component XML is opaque / byte-faithful (breaking)

Component XML (and the other open-ended component-family endpoints) is now an
**opaque payload**. The SDK sends and returns the exact bytes the Boomi API
emits — byte-for-byte identical to a direct REST call — and never parses,
hydrates, normalizes, or re-serializes it. This removes a class of silent XML
corruption (lost namespaces, CDATA, comments, attribute order, unknown
attributes) that could not be avoided while round-tripping through generated
models.

### Breaking changes

- **`ComponentService` create/get/update/bulk return raw `bytes`** (were
  `Component` / `List[str]`). They no longer parse responses into a `Component`
  model.
- **Write bodies must be raw `str` or `bytes`.** Passing a `Component`, `dict`,
  `ElementTree` element, or any other object raises the new
  `UnsafeComponentXmlSerializationError` **before** the request is sent.
- **`bulk_component` returns the whole raw XML envelope** (`bytes`), not a
  `List[str]` of re-serialized per-component fragments (which was lossy and
  silently dropped non-200 entries).
- **Removed** lossy round-trip APIs: `Component.to_xml()`,
  `Component.set_object_xml()`, the `Component` XML-preservation fields
  (`object_xml`, `_object_element`, `_original_xml`),
  `ComponentService.get_component_etree()`, and
  `ComponentService.update_component_etree()` (sync + async). This reverts the
  direction of the earlier `_deserialize_component_response` / XML-preservation
  fix, which is documented in `docs/archive/create_component_xml_response_unmap.md`.
- **The same opaque/raw-only contract now applies to the other component-family
  endpoints** whose payloads carry open-ended config subtrees:
  `TradingPartnerComponentService`, `OrganizationComponentService`, and
  `SharedCommunicationChannelComponentService` — their `create_*`/`get_*`/
  `update_*` return raw `bytes` and accept raw `str`/`bytes`. Their `query_*`,
  `bulk_*`, and `delete_*` methods are unchanged (still typed).

### Added

- `boomi.extract_component_xml_metadata(xml)` — a read-only helper returning the
  root `<Component>` attributes (componentId, name, type, version, folderId,
  …) from raw `str`/`bytes` XML. It is XXE/entity-expansion hardened and has no
  inverse (it cannot rebuild XML), so it can never reintroduce corruption.
- `boomi.UnsafeComponentXmlSerializationError` (subclass of `RequestError`).
- `BaseService.send_request_raw()` — returns the undecoded response bytes for
  opaque endpoints, bypassing the lossy text-decode path.

### Fixed

- **Byte-faithful transport.** Opaque responses are read from the raw response
  bytes (`response.content`) instead of `requests`' chardet-guessed,
  `errors="replace"` text decoding, so non-UTF-8 / charset-suffixed payloads are
  preserved exactly.
- **SDK-wide charset matching.** Content-type comparisons now ignore parameters,
  so `application/xml; charset=UTF-8` responses are handled the same as
  `application/xml` across all services (previously they fell through to a
  deserialization error).
- **Falsy raw bodies** (e.g. empty bytes) are no longer silently coerced to a
  JSON `{}` in the request handler.
- **Error bodies** are surfaced verbatim; XML error-detail extraction is
  XXE-hardened and tolerant of `bytes` bodies.

### Migration

See `documentation/component_xml_raw_only_migration.md` for caller recipes
(model-field access → `extract_component_xml_metadata` / `ElementTree`, and the
"serialize once on your side, then pass raw" update pattern). For byte-exact
round-trips of non-UTF-8 XML, pass `bytes` rather than `str`.
