# Reproducibility

## Run all checks

Use Python 3.13.5 and the pinned versions in `requirements.txt`, which reproduce the supplied numerical environment.

```bash
python -m pip install -r requirements.txt
python tools/build_reading.py --check
python tools/verify.py --output-dir /absolute/new/path/outside/repository
```

The output directory must not exist and must lie outside the source tree. The wrapper runs eight infrastructure checks and the original wrapper's fifteen scientific check groups: five each for the spectral pilot, local-source transport, and preparation-size/proof review. It does not modify an original assertion or tolerance.

`verification.json` records the tested source hashes, Git revision/index tree when available, assertions, preserved source checks, and all canonical-report comparisons. `scientific/receipt.json` and `scientific/preserved/receipt.json` are the original wrappers' unchanged receipts. All generated reports and logs accompany them.

## Three separate conclusions

**Scientific assertions.** Every original test runs unchanged. A passing finite calculation supports a stated identity or diagnostic; it does not replace the infinite-lattice proof or constitute external peer review.

**Source integrity.** The complete 77-file source archive, its exact membership, three nested manifests, and the owner license are checked. The whole repository source inventory must remain unchanged during a run. `maintenance/SOURCE_IMPORT.json` records the original package digest and repository baseline.

**Canonical report identity.** The default command and CI require exact equality with all three canonical scientific JSON reports. Environment-dependent numerical differences are reported field by field. An explicit `--allow-numeric-report-differences` option exists for investigating finite numeric-only report drift; it never changes scientific assertions. Such a run is labelled `PASS_REQUIRES_NUMERIC_REVIEW` and is not the default release check. Structure, type, source, missing-report, and assertion failures remain failures. Review any discrepancy before merge rather than replacing canonical reports.

Hosted verification checks the actual PR head. A PR-head run is not a merged-main run: verify the merged revision separately and compare its exact source tree. The workflow is read-only and preserves evidence even when verification fails.

## Generated scientific reading pages

`tools/build_reading.py` selects the declared scientific sections from the immutable archive, converts math delimiters for GitHub display, and records source hashes, output hashes, selections, and literal substitutions in `maintenance/READING_TRANSFORMS.json`. It verifies unchanged display-equation content. Edit the generator rather than a generated page, then regenerate and rerun the checks.

The original chronological notes, numerical repairs, failed runs, and pre-initialization handoff remain in [the archive](archive/review-2026-10-10/README.md). The live continuation instruction is [CURRENT.md](CURRENT.md): continue in Chat, without requiring a workspace.

## Scientific interpretation

The source-size transform diagnostic is not a many-body evolution. Finite-ring spectra and dynamics do not establish the infinite-lattice long-time limit. Numeric quadratures are not interval certificates, and weak probability convergence does not imply convergence of unbounded moments. The [theorem](research/THEOREM.md) and [proof map](research/PROOF_MAP.md) retain these distinctions.
