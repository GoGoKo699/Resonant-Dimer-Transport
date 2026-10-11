# Reproducibility

## Run all checks

Use Python 3.13.5 and the pinned versions in `requirements.txt`, which reproduce the supplied numerical environment.

```bash
python -m pip install -r requirements.txt
python tools/build_reading.py --check
python tools/verify.py --output-dir /absolute/new/path/outside/repository
python tools/check_rest_crossover.py --output /absolute/new/path/rest_crossover.json
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

This runner checks the four exact imported source blobs, copies the original helper and checker into an isolated temporary layout, and executes their unchanged assertions using the preserved spectral solver. Its raw `legacy.json`, `legacy.log`, and `verification.json` remain in the requested new output directory. Hosted verification requires the main 33 scientific groups, these six supplemental groups, and the three rest-crossover groups below, for 42 scientific groups in total, as well as the eight infrastructure checks. The receipts keep their source and report claims separate; the alternative proof is not silently substituted for the sharper main theorem.

## Rest-residue and curvature checks

`tools/check_rest_crossover.py` has three additional groups for the
[explicit rest coefficients](research/DETUNING_CROSSOVER.md#explicit-rest-residue-and-curvature).
It independently integrates the defining continuum normalization and curvature
numerator using reciprocal tails and algebraic endpoint weights, rather than
evaluating a beta-function expression as its numerical reference. It then
checks the exact lattice rest integrals at three decreasing momentum scales
for $z=0.6,0.75,0.9$, and compares the curvature with a separate small-momentum
velocity calculation at $z=0.75$. The preserved scalar energy and velocity
solvers are reused explicitly and remain unchanged.

The report records all quadratures, error indicators, finite-scale corrections,
refinement comparisons, and source hashes. Slow convergence at $z=0.6$ is
retained in the data; a decreasing error on this grid is not a certified
asymptotic remainder. The proof of the limit is the dominated-convergence
argument in the detuning theorem. The three groups run separately from the
main and alternative-proof receipts, without replacing any original assertion
or canonical report.

## Coincidence-tail figure

The [figure](figures/coincidence_tail.svg) evaluates the actual lattice
limiting measure at $z=3/4$, with resonance and detunings
$\delta=0.06,0.09,0.135$. Its [data](figures/coincidence_tail.json) retain
absolute probabilities, momentum intervals, located cutoffs, quadrature
error estimates, refinement comparisons, and source hashes.

To recompute it in a separate output directory, install the optional plotting
environment and run:

```bash
python -m pip install -r requirements-figures.txt
python tools/plot_coincidence.py --output /absolute/new/path/coincidence_tail.svg --data /absolute/new/path/coincidence_tail.json
```

The generator integrates $Z(P)^2dP/\pi$ over scan-detected positive-momentum
velocity intervals. It compares 72- and 144-cell crossing scans and tighter,
subdivided quadratures at three thresholds for every coupling. A separate
cusp-split quadrature checks the pole equation, normalized relative
wavefunction, and contact overlap. Numerical maxima and scans are finite
diagnostics; global support statements follow from the analytical proofs.
Zero probabilities above a located cutoff are recorded separately and are
not replaced by a positive floor on the logarithmic plot. The right panel
uses $Q_U(0.9v_{\max})$ without rescaling its probability.

To render the saved data without repeating the calculation:

```bash
python tools/plot_coincidence.py --from-data figures/coincidence_tail.json --output /absolute/new/path/coincidence_tail.svg
```

The figure represents the infinite lattice followed by long time at each
fixed coupling and velocity threshold. It does not evaluate an observation
time. These figure diagnostics are separate from the 42 scientific groups;
the original assertions, tolerances, and canonical reports are unchanged.

## Three separate conclusions

**Scientific assertions.** Every original test runs unchanged. A passing finite calculation supports a stated identity or diagnostic; it does not replace the infinite-lattice proof or constitute external peer review.

**Source integrity.** The complete 77-file source archive, its exact membership, three nested manifests, and the owner license are checked. The whole repository source inventory must remain unchanged during a run. `maintenance/SOURCE_IMPORT.json` records the original package digest and repository baseline.

**Canonical report identity.** The default local command requires exact equality with all three canonical scientific JSON reports. Hosted CI explicitly uses `--allow-numeric-report-differences` to retain complete evidence across numerical stacks. That option accepts only finite numeric-only report drift while every original scientific assertion remains unchanged. Such a run is labelled `PASS_REQUIRES_NUMERIC_REVIEW`, enumerates every difference, and requires inspection before merging; a green badge alone is not canonical byte identity. Structure, type, source, missing-report, and assertion failures remain failures. The first hosted run and its 89 reviewed numeric differences are documented in [the numerical review record](maintenance/NUMERIC_REPORT_REVIEW.json). The largest difference is 1.67e-10 in a finite-difference curvature diagnostic. No canonical report, archived source, assertion, or tolerance was replaced.

Hosted verification checks the actual PR head. A PR-head run is not a merged-main run: verify the merged revision separately and compare its exact source tree. The workflow is read-only and preserves evidence even when verification fails.

Successful hosted runs also attach `source.tar`, created by `git archive HEAD` after verification. It contains only the tracked source files of the tested commit, without Git history, credentials, or runner-local files. After safe extraction, compare every file against `source_sha256` in `verification.json` before reproducing the checks. Logs and receipts remain available when verification fails; a source snapshot is attached only after both scientific-suite steps pass. The initial PR-head run and earlier workflow artifacts predate this addition.

## Generated scientific reading pages

`tools/build_reading.py` selects the declared scientific sections from the immutable archive, converts math delimiters for GitHub display, and records source hashes, output hashes, selections, and literal substitutions in `maintenance/READING_TRANSFORMS.json`. It verifies unchanged display-equation content. The ledger classifies the endpoint proof-prose correction and links its proof. It also records the theorem page's scientific reconciliation with the uniform observation-time estimate and its proof location. The active contribution page omits an editorial-planning sentence and links the time-dependent proofs; archived text and display equations remain unchanged. The [endpoint lemma](research/THRESHOLD_ENDPOINT.md) explains why the continuum energy approximation must not be substituted at the lattice edge. Edit the generator rather than a generated page, then regenerate and rerun the checks. The author account, endpoint lemma, detuning theorem, time-dependent proofs, and boundary resolvent appendix are maintained directly rather than generated from the archive.

The original chronological notes, numerical repairs, failed runs, and pre-initialization handoff remain in [the archive](archive/review-2026-10-10/README.md). The live continuation instruction is [CURRENT.md](CURRENT.md): continue in Chat, without requiring a workspace.

## Scientific interpretation

The source-size transform diagnostic is not a many-body evolution. Finite-ring spectra and dynamics do not establish the infinite-lattice long-time limit. Numeric quadratures are not interval certificates, and weak probability convergence does not imply convergence of unbounded moments. The [theorem](research/THEOREM.md) and [proof map](research/PROOF_MAP.md) retain these distinctions.
