#!/usr/bin/env python3
"""BUG-10 fix: Make `result` optional in all 45 *BulkResponseResponse model classes.

The Boomi API bulk responses can contain error items that lack a `Result` field.
The SDK models had `result` as a required positional arg, causing TypeError on
deserialization. This script makes `result` optional with SENTINEL default.
"""

import glob
import re
import os

MODEL_DIR = os.path.join(os.path.dirname(__file__), '..', 'src', 'boomi', 'models')


def fix_file(filepath):
    """Returns 'modified', 'already_fixed', or 'skipped'."""
    with open(filepath, 'r') as f:
        content = f.read()

    # Idempotency guard: if result already has = SENTINEL, skip
    if re.search(r'result:.*= SENTINEL', content):
        return 'already_fixed'

    original = content

    # 1. Add = SENTINEL default to the result parameter in __init__ signature
    # Match lines like: "        result: SomeType," that don't already have "= SENTINEL"
    content = re.sub(
        r'^(\s+result: \w+),\s*$',
        r'\1 = SENTINEL,',
        content,
        flags=re.MULTILINE,
    )

    # 2. Wrap self.result = self._define_object(...) in "if result is not SENTINEL:"
    # Variant A: single-line
    content = re.sub(
        r'^( {8})(self\.result = self\._define_object\(result, \w+\))\n',
        r'\1if result is not SENTINEL:\n\1    \2\n',
        content,
        flags=re.MULTILINE,
    )
    # Variant B: multi-line (the one outlier file)
    content = re.sub(
        r'^( {8})(self\.result = self\._define_object\(\n {12}result, \w+\n {8}\))\n',
        r'\1if result is not SENTINEL:\n\1    \2\n',
        content,
        flags=re.MULTILINE,
    )

    # 3. Update docstrings: ":param result: result" -> ":param result: result, defaults to None"
    content = re.sub(
        r':param result: result\n',
        ':param result: result, defaults to None\n',
        content,
    )
    # ":type result: SomeType" -> ":type result: SomeType, optional" (only where not already optional)
    content = re.sub(
        r'(:type result: \w+)\n',
        r'\1, optional\n',
        content,
    )

    if content != original:
        with open(filepath, 'w') as f:
            f.write(content)
        return 'modified'
    return 'skipped'


def main():
    pattern = os.path.join(MODEL_DIR, '*_bulk_response.py')
    files = sorted(glob.glob(pattern))
    print(f"Found {len(files)} bulk response files")

    modified = []
    already_fixed = []
    skipped = []
    errors = []

    for filepath in files:
        basename = os.path.basename(filepath)
        try:
            result = fix_file(filepath)
            if result == 'modified':
                print(f"  Fixed: {basename}")
                modified.append(basename)
            elif result == 'already_fixed':
                print(f"  Already fixed: {basename}")
                already_fixed.append(basename)
            else:
                print(f"  Skipped (no changes): {basename}")
                skipped.append(basename)
        except Exception as e:
            print(f"  Error: {basename}: {e}")
            errors.append(basename)

    print(f"\nSummary:")
    print(f"  Modified: {len(modified)}")
    print(f"  Already fixed: {len(already_fixed)}")
    print(f"  Skipped: {len(skipped)}")
    print(f"  Errors: {len(errors)}")


if __name__ == '__main__':
    main()
