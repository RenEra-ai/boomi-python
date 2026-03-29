#!/usr/bin/env bash
set -euo pipefail

echo "=== Schema Update Verification ==="
echo ""

echo "1/5 Running bulk response fix script..."
python3 scripts/fix_bulk_response_result.py
echo ""

echo "2/5 Running async response fix script..."
python3 scripts/fix_async_response_required_args.py
echo ""

echo "3/5 Running int coercion fix script..."
python3 scripts/fix_int_coercion.py
echo ""

echo "4/5 Running regression matrix..."
python3 -m pytest tests/test_model_invariants.py tests/test_xml_int_coercion.py tests/test_bug09_persisted_process_properties.py tests/test_bug10_bulk_response_optional_result.py tests/test_bug11_udf_construction.py -v
echo ""

echo "5/5 Running full test suite..."
python3 -m pytest tests/ -v
echo ""

echo "=== Verification complete ==="
