# Component XML byte-safety: audit & allowlist

This document records the audit behind the v3.0.0 "opaque / raw-only" redesign:
which endpoints carry **open-ended XML payloads** that cannot be losslessly
represented by a generated model (and were therefore converted to raw bytes),
and which endpoints deserialize **well-defined, spec-enumerated models** and are
safe to keep typed.

The OpenAPI specification under `/openapi/` remains the source of truth. The
classification criterion is whether a model embeds an open-ended config subtree
(a Component `<object>`, or connector/EDI communication config) versus a closed,
fully-enumerated schema.

## OPAQUE — converted to raw `bytes` (create/get/update)

These send and return raw XML byte-for-byte; write bodies must be raw
`str`/`bytes`. Their `query_*`, `bulk_*`, and `delete_*` methods remain typed.

| Service | Why opaque |
| :------ | :--------- |
| `ComponentService` | The `<object>` subtree is arbitrary per component type (process, profile, connector, map, …). |
| `TradingPartnerComponentService` | Embeds `PartnerCommunication` (AS2/Disk/FTP/HTTP/MLLP/OFTP/SFTP) and `PartnerInfo` (X12/EDIFACT/HL7/Odette/RosettaNet/Tradacoms/Custom) — open-ended EDI/connector config. |
| `SharedCommunicationChannelComponentService` | Embeds the same open-ended `PartnerCommunication` transport-config subtree; its query path had already abandoned the typed parser for hand-rolled XML. |
| `OrganizationComponentService` | Part of the component family; previously returned `Union[..., str, dict]` with a raw fallback (the author had already hit the lossiness). Aligned with the family for consistency and safety. |

## TYPED-SAFE — kept typed (allowlist)

Every other XML-deserializing service deserializes a closed, spec-enumerated
model with no open-ended config subtree, so it is safe to keep returning typed
models. The v3.0.0 transport fixes make this correct regardless of response
charset:

- Content-type matching is normalized to the bare media type, so
  `application/xml; charset=UTF-8` is treated as `application/xml` everywhere
  (previously such responses fell through to a deserialization error).

Representative categories (non-exhaustive; see `src/boomi/services/`):

- Account & governance: `account`, `account_group*`, `account_user_role`,
  `account_sso_config`, `role`, `environment_role`, …
- Runtime / atom: `atom*`, `cloud`, `runtime_*`, `shared_web_server`,
  `shared_server_information`, `listener_status`, `list_queues`, …
- Component metadata & references (NOT the Component XML itself):
  `component_metadata`, `component_reference`, `component_diff_request`,
  `component_atom_attachment`, `component_environment_attachment`,
  `packaged_component*`, `process*`, `folder`, `branch`, `merge_request`, …
- Deployment & integration packs: `deployment`, `deployed_*`, `environment*`,
  `integration_pack*`, `connector`, …
- Connector / EDI **records** (read-only query): `*_connector_record`,
  `generic_connector_record`, `execution_connector`, …
- Execution / monitoring / reporting: `execution_*`, `event`, `audit_log`,
  `*_count_*`, `throughput_*`, `connector_document`, `rerun_document`, …
- `trading_partner_processing_group` — a typed grouping of partner refs/ids,
  **not** an embedded connector config; stays typed.

## Notes

- `parse_xml_to_dict` (in `net/transport/utils.py`) is retained — it is used by
  the typed services above and by `api_error` error-detail extraction.
- The lossy `parse_xml_to_dict_with_preservation`, `Component.to_xml`,
  `Component.set_object_xml`, and the `*_etree` helpers were removed.
- No opaque-XML deserialization exists outside `src/boomi/services/` (confirmed
  for `net/` and `models/`).
