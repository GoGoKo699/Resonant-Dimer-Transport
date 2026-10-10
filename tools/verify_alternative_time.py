#!/usr/bin/env python3
"""Reproduce the preserved alternative proof without changing either helper set."""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import shutil
import subprocess
import sys
import tempfile

sys.dont_write_bytecode = True
ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'archive/coarse-time-2026-10-10'


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def blob(path: Path) -> str:
    data = path.read_bytes()
    return hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()


def inventory(root: Path) -> dict[str, str]:
    result = {}
    for path in sorted(root.rglob('*')):
        relative = path.relative_to(root)
        if '.git' in relative.parts:
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
    before = inventory(ROOT)
    record = json.loads((SOURCE / 'PROVENANCE.json').read_text())
    if record['repository'] != 'GoGoKo699/Resonant-Dimer-Transport':
        raise ValueError('Unexpected source repository.')
    expected = record['files']
    checked = {}
    for name, expected_blob in expected.items():
        relative = PurePosixPath(name)
        if relative.is_absolute() or '..' in relative.parts:
            raise ValueError('Invalid source path: ' + name)
        path = SOURCE.joinpath(*relative.parts)
        if blob(path) != expected_blob:
            raise ValueError('Changed imported source: ' + name)
        checked[name] = {'git_blob': expected_blob, 'sha256': digest(path)}
    output.mkdir(parents=True)
    env = dict(os.environ, PYTHONDONTWRITEBYTECODE='1', OPENBLAS_NUM_THREADS='1', OMP_NUM_THREADS='1')
    with tempfile.TemporaryDirectory(prefix='dimer-alternative-') as temporary:
        stage = Path(temporary)
        for name in expected:
            target = stage / name
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(SOURCE / name, target)
        destination = stage / 'archive/review-2026-10-10'
        shutil.copytree(ROOT / 'archive/review-2026-10-10', destination)
        stage_before = inventory(stage)
        with (output / 'legacy.log').open('xb') as log:
            result = subprocess.run(
                [sys.executable, str(stage / 'tools/check_finite_time.py'),
                 '--output', str(output / 'legacy.json')],
                cwd=stage, env=env, stdout=log, stderr=subprocess.STDOUT, timeout=180)
        staged_sources_unchanged = stage_before == inventory(stage)
    path = output / 'legacy.json'
    report = json.loads(path.read_text()) if path.exists() else {}
    unchanged = before == inventory(ROOT)
    passed = (result.returncode == 0 and report.get('status') == 'PASS'
              and report.get('test_groups') == 6 and unchanged and staged_sources_unchanged)
    receipt = {
        'status': 'PASS' if passed else 'FAIL',
        'repository': record['repository'], 'source_commit': record['source_commit'],
        'scientific_groups': report.get('test_groups'), 'assertions_pass': passed,
        'original_checker_modified': False, 'source_unchanged': unchanged,
        'temporary_sources_unchanged': staged_sources_unchanged,
        'imported_sources': checked, 'returncode': result.returncode,
        'legacy_report_sha256': digest(path) if path.exists() else None,
        'canonical_byte_identity_claimed': False,
        'scope': 'Six unchanged supplemental regression groups; not external proof review, optimal-time certification, or a replacement for the main suite.'}
    with (output / 'verification.json').open('x') as stream:
        json.dump(receipt, stream, indent=2, sort_keys=True, allow_nan=False)
        stream.write('\n')
    print(json.dumps(receipt, indent=2, sort_keys=True))
    raise SystemExit(0 if passed else 1)


if __name__ == '__main__':
    main()
