# Reproducibility

## Run all checks

Use Python 3.13.5 and the pinned versions in `requirements.txt`, which reproduce the supplied numerical environment.

```bash
python -m pip install -r requirements.txt
python tools/build_reading.py --check
python tools/verify.py --output-dir /absolute/new/path/outside/repository
```

The output directory must not exist and must lie outside the source tree. The wrapper runs eight infrastructure checks and twenty-nine scientific check groups: the fifteen preserved groups (five each for the spectral pilot, local-source transport, and preparation-size/proof review) plus three exact-threshold regressions in `tools/check_endpoint.py` and five detuning groups in `tools/check_detuning.py`, plus six finite-time groups in `tools/check_finite_time.py`. It does not modify an original assertion or tolerance.

`verification.json` records the tested source hashes, Git revision/index tree when available, assertions, preserved source checks, and all canonical-report comparisons. `scientific/receipt.json` and `scientific/preserved/receipt.json` are the original wrappers' unchanged receipts. All generated reports and logs accompany them. `endpoint.json` and `endpoint.log` record the three additional groups. `detuning.json` and `detuning.log` record the crossover checks. `tools/detuning.py` reuses the preserved scalar implementation explicitly; the derivative test also evaluates the continuum normalization and velocity numerator directly. Maxima and crossing scans are finite diagnostics, not global certificates. Canonical byte comparisons concern the three preserved reports; the new endpoint report is governed by its explicit regression assertions, not an invented historical canonical file.

`finite_time.json` and `finite_time.log` record the six finite-time regression groups. They check the density envelope and critical-energy geometry, a boundary-resolvent limit, the exact minimum-gap and second-derivative identities, Fourier-sandwich constants, finite characteristic/interference identities, and the sufficient exponent algebra. One smooth periodic band fixture tests the general Fourier inequality; it is not a replacement physical dimer model. No numerical simulation at times of order delta^(-37), optimal waiting-time certification, or finite experimental window is claimed. New reports are governed by their explicit assertions, not invented historical reference files.

## Three separate conclusions

**Scientific assertions.** Every original test runs unchanged. A passing finite calculation supports a stated identity or diagnostic; it does not replace the infinite-lattice proof or constitute external peer review.

**Source integrity.** The complete 77-file source archive, its exact membership, three nested manifests, and the owner license are checked. The whole repository source inventory must remain unchanged during a run. `maintenance/SOURCE_IMPORT.json` records the original package digest and repository baseline.

**Canonical report identity.** The default local command requires exact equality with all three canonical scientific JSON reports. Hosted CI explicitly uses `--allow-numeric-report-differences` to retain complete evidence across numerical stacks. That option accepts only finite numeric-only report drift while every original scientific assertion remains unchanged. Such a run is labelled `PASS_REQUIRES_NUMERIC_REVIEW`, enumerates every difference, and requires inspection before merging; a green badge alone is not canonical byte identity. Structure, type, source, missing-report, and assertion failures remain failures. The first hosted run and its 89 reviewed numeric differences are documented in [the numerical review record](maintenance/NUMERIC_REPORT_REVIEW.json). The largest difference is 1.67e-10 in a finite-difference curvature diagnostic. No canonical report, archived source, assertion, or tolerance was replaced.

Hosted verification checks the actual PR head. A PR-head run is not a merged-main run: verify the merged revision separately and compare its exact source tree. The workflow is read-only and preserves evidence even when verification fails.

## Generated scientific reading pages

`tools/build_reading.py` selects the declared scientific sections from the immutable archive, converts math delimiters for GitHub display, and records source hashes, output hashes, selections, and literal substitutions in `maintenance/READING_TRANSFORMS.json`. It verifies unchanged display-equation content. The ledger classifies the endpoint proof-prose correction and the finite-time extension of two limitation paragraphs, linking their respective proofs. The [endpoint lemma](research/THRESHOLD_ENDPOINT.md) explains why the continuum energy approximation must not be substituted at the lattice edge. Edit the generator rather than a generated page, then regenerate and rerun the checks. The author account, endpoint lemma, detuning theorem, and finite-time proof are maintained directly rather than generated from the archive.

The original chronological notes, numerical repairs, failed runs, and pre-initialization handoff remain in [the archive](archive/review-2026-10-10/README.md). The live continuation instruction is [CURRENT.md](CURRENT.md): continue in Chat, without requiring a workspace.

## Scientific interpretation

The source-size transform diagnostic is not a many-body evolution. Finite-ring spectra and dynamics do not establish the infinite-lattice long-time limit. Numeric quadratures are not interval certificates, and weak probability convergence does not imply convergence of unbounded moments. The [theorem](research/THEOREM.md) and [proof map](research/PROOF_MAP.md) retain these distinctions.
