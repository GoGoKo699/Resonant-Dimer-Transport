# Reproducibility

## Run all checks

Use Python 3.13.5 and the pinned versions in `requirements.txt`, which reproduce the supplied numerical environment.

```bash
python -m pip install -r requirements.txt
python tools/build_reading.py --check
python tools/verify.py --output-dir /absolute/new/path/outside/repository
```

The output directory must not exist and must lie outside the source tree. The wrapper runs eight infrastructure checks and thirty-three scientific check groups: the fifteen preserved groups (five each for the spectral pilot, local-source transport, and preparation-size/proof review) plus three exact-threshold regressions in `tools/check_endpoint.py` and five detuning groups in `tools/check_detuning.py`, plus five finite-time groups in `tools/check_finite_time.py` and five joint-regime groups in `tools/check_observation_time.py`. It does not modify an original assertion or tolerance.

`verification.json` records the tested source hashes, Git revision/index tree when available, assertions, preserved source checks, and all canonical-report comparisons. `scientific/receipt.json` and `scientific/preserved/receipt.json` are the original wrappers' unchanged receipts. All generated reports and logs accompany them. `endpoint.json` and `endpoint.log` record the three additional groups. `detuning.json` and `detuning.log` record the crossover checks. `tools/detuning.py` reuses the preserved scalar implementation explicitly; the derivative test also evaluates the continuum normalization and velocity numerator directly. Maxima and crossing scans are finite diagnostics, not global certificates. Canonical byte comparisons concern the three preserved reports; the endpoint, detuning, finite-time, and observation-time reports are governed by their explicit regression assertions, not invented historical canonical files.

`finite_time.json` and `finite_time.log` record the five additional groups.
They test event-local amplitude accounting, compact Fourier smoothing, a
separately specified smooth-band control, actual dimer curvature/gap identities,
and continuous spectral-density controls including samples at the dimer's
three critical energies. The smooth band and exact triangular density are
mathematical benchmarks, not a rare-dimer propagation simulation. The tests
do not numerically enclose the spectral variation budget or certify a physical
waiting time; the sufficient-time arithmetic requires valid static bounds.

`observation_time.json` and `observation_time.log` record five joint-regime
regressions: quotient variation and coalescing critical-energy profiles, a
principal-value calculation of the actual lattice continuum peak, exact
band-norm power accounting, integrated continuum-envelope and relative-error
arithmetic, and active-Markdown control-character checks. These tests are not
a simulation of the joint time limit, interval bounds on its prefactor, or a
proof of optimality. The analytical estimates are in
[the joint theorem](research/OBSERVATION_TIME.md).

## Alternative proof checks

The [alternative conservative time estimate](research/ALTERNATIVE_TIME_BOUND.md) has six additional scientific regression groups from a parallel proof route. Run them without replacing any current module:

```bash
python tools/verify_alternative_time.py --output-dir /absolute/new/alternative/results
```

This runner checks the four exact imported source blobs, copies the original helper and checker into an isolated temporary layout, and executes their unchanged assertions using the preserved spectral solver. Its raw `legacy.json`, `legacy.log`, and `verification.json` remain in the requested new output directory. Hosted verification requires the main 33 scientific groups and these six supplemental groups, for 39 scientific groups in total, as well as the eight infrastructure checks. The two receipts keep their source and report claims separate; the alternative proof is not silently substituted for the sharper main theorem.

## Three separate conclusions

**Scientific assertions.** Every original test runs unchanged. A passing finite calculation supports a stated identity or diagnostic; it does not replace the infinite-lattice proof or constitute external peer review.

**Source integrity.** The complete 77-file source archive, its exact membership, three nested manifests, and the owner license are checked. The whole repository source inventory must remain unchanged during a run. `maintenance/SOURCE_IMPORT.json` records the original package digest and repository baseline.

**Canonical report identity.** The default local command requires exact equality with all three canonical scientific JSON reports. Hosted CI explicitly uses `--allow-numeric-report-differences` to retain complete evidence across numerical stacks. That option accepts only finite numeric-only report drift while every original scientific assertion remains unchanged. Such a run is labelled `PASS_REQUIRES_NUMERIC_REVIEW`, enumerates every difference, and requires inspection before merging; a green badge alone is not canonical byte identity. Structure, type, source, missing-report, and assertion failures remain failures. The first hosted run and its 89 reviewed numeric differences are documented in [the numerical review record](maintenance/NUMERIC_REPORT_REVIEW.json). The largest difference is 1.67e-10 in a finite-difference curvature diagnostic. No canonical report, archived source, assertion, or tolerance was replaced.

Hosted verification checks the actual PR head. A PR-head run is not a merged-main run: verify the merged revision separately and compare its exact source tree. The workflow is read-only and preserves evidence even when verification fails.

Successful hosted runs also attach `source.tar`, created by `git archive HEAD` after verification. It contains only the tracked source files of the tested commit, without Git history, credentials, or runner-local files. After safe extraction, compare every file against `source_sha256` in `verification.json` before reproducing the checks. Logs and receipts remain available when verification fails; a source snapshot is attached only after both scientific-suite steps pass. The initial PR-head run and earlier workflow artifacts predate this addition.

## Generated scientific reading pages

`tools/build_reading.py` selects the declared scientific sections from the immutable archive, converts math delimiters for GitHub display, and records source hashes, output hashes, selections, and literal substitutions in `maintenance/READING_TRANSFORMS.json`. It verifies unchanged display-equation content. The ledger also classifies the endpoint proof-prose correction and links its proof. The active contribution page omits an editorial-planning sentence and links the subsequently completed time-dependent proofs; these presentation transformations leave the archived text and scientific equations unchanged. The [endpoint lemma](research/THRESHOLD_ENDPOINT.md) explains why the continuum energy approximation must not be substituted at the lattice edge. Edit the generator rather than a generated page, then regenerate and rerun the checks. The author account, endpoint lemma, detuning theorem, and time-dependent proofs are maintained directly rather than generated from the archive.

The original chronological notes, numerical repairs, failed runs, and pre-initialization handoff remain in [the archive](archive/review-2026-10-10/README.md). The live continuation instruction is [CURRENT.md](CURRENT.md): continue in Chat, without requiring a workspace.

## Scientific interpretation

The source-size transform diagnostic is not a many-body evolution. Finite-ring spectra and dynamics do not establish the infinite-lattice long-time limit. Numeric quadratures are not interval certificates, and weak probability convergence does not imply convergence of unbounded moments. The [theorem](research/THEOREM.md) and [proof map](research/PROOF_MAP.md) retain these distinctions.
