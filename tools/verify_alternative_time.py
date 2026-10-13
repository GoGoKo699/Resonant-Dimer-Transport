#!/usr/bin/env python3
"""Reproduce the six-group alternative finite-time estimate."""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys

sys.dont_write_bytecode = True
import verify
ROOT = Path(__file__).resolve().parents[1]


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def inventory(root: Path) -> dict[str, str]:
    result = {}
    for path in sorted(root.rglob('*')):
        relative = path.relative_to(root)
        if '.git' in relative.parts or '.venv' in relative.parts:
            continue
        if path.is_symlink():
            raise ValueError('Source symlink: ' + str(relative))
        if path.is_file():
            result[relative.as_posix()] = digest(path)
    return result


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output-dir', type=Path, required=True)
    args = parser.parse_args()
    output = args.output_dir.expanduser().resolve()
    if output.exists() or output == ROOT or ROOT in output.parents:
        parser.error('Use a new output directory outside the repository.')
    integrity = verify.static_checks()
    before = inventory(ROOT)
    output.mkdir(parents=True)
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1', OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1')
    with (output / 'alternative.log').open('xb') as log:
        result = subprocess.run(
            [sys.executable, str(ROOT / 'tools/alternative_time/check_finite_time.py'),
             '--output', str(output / 'alternative.json')],
            cwd=ROOT, env=env, stdout=log, stderr=subprocess.STDOUT, timeout=180)
    path = output / 'alternative.json'
    report = json.loads(path.read_text()) if path.exists() else {}
    unchanged = before == inventory(ROOT)
    assertions = result.returncode == 0 and report.get('status') == 'PASS' and report.get('test_groups') == 6
    passed = assertions and unchanged
    receipt = {
        'status': 'PASS' if passed else 'FAIL',
        'repository': 'GoGoKo699/Resonant-Dimer-Transport',
        'commit': verify.git('rev-parse', 'HEAD'),
        'index_tree': verify.git('write-tree'),
        'static_checks': integrity,
        'scientific_groups': report.get('test_groups'),
        'assertions_pass': assertions,
        'source_unchanged': unchanged,
        'source_files': len(before),
        'source_sha256': before,
        'returncode': result.returncode,
        'alternative_report_sha256': digest(path) if path.exists() else None,
        'canonical_byte_identity_claimed': False,
        'scope': 'Six supplemental regression groups for the sufficient finite-time estimate.'}
    with (output / 'verification.json').open('x') as stream:
        json.dump(receipt, stream, indent=2, sort_keys=True, allow_nan=False)
        stream.write('\n')
    print(json.dumps({key: value for key, value in receipt.items() if key != 'source_sha256'}, indent=2, sort_keys=True))
    raise SystemExit(0 if passed else 1)


if __name__ == '__main__':
    main()
