#!/usr/bin/env bash
set -euo pipefail

echo "=== Schema Update Verification ==="
echo ""

echo "1/4 Running bulk response fix script..."
python3 scripts/fix_bulk_response_result.py
echo ""

echo "2/4 Running async response fix script..."
python3 scripts/fix_async_response_required_args.py
echo ""

echo "3/4 Running regression matrix..."
python3 -m pytest tests/test_model_invariants.py tests/test_bug09_persisted_process_properties.py tests/test_bug10_bulk_response_optional_result.py tests/test_bug11_udf_construction.py -v
echo ""

echo "4/4 Running full test suite..."
python3 -m pytest tests/ -v
echo ""

echo "=== Verification complete ==="
