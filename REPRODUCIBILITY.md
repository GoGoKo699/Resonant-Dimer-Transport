# Reproducibility

## Run all checks

Use Python 3.13.5 and the pinned packages in `requirements.txt`.

```bash
python -m pip install -r requirements.txt
python tools/build_reading.py --check
python tools/verify.py --output-dir /absolute/new/path/main-results
python tools/verify_alternative_time.py --output-dir /absolute/new/path/alternative-results
python tools/check_rest_crossover.py --output /absolute/new/path/rest-crossover.json
```

Each output path must be new and outside the repository. The complete run
contains **42 scientific groups and eight infrastructure checks**:

| Suite | Groups | Script and evidence |
|---|---:|---|
| Spectral, local-source transport, and preparation size | 15 | The source wrappers run through `tools/verify.py`; reports are in `scientific/`. |
| Exact lattice threshold | 3 | `tools/check_endpoint.py`; `endpoint.json` and log. |
| Detuning crossover | 5 | `tools/check_detuning.py`; `detuning.json` and log. |
| Static finite-time certificate | 5 | `tools/check_finite_time.py`; `finite_time.json` and log. |
| Joint observation-time regime | 5 | `tools/check_observation_time.py`; `observation_time.json` and log. |
| Conservative alternative time estimate | 6 | `tools/verify_alternative_time.py`; `legacy.json`, log, and separate `verification.json`. |
| Rest residue and curvature | 3 | `tools/check_rest_crossover.py`; the requested JSON report. |
| Source, generation, links, license, workflow, and scope | 8 | `tools/check_repository.py`, run by the main wrapper; `infrastructure.json` and log. |

The main wrapper covers 33 scientific groups and the eight infrastructure
checks. Its `verification.json` records the exact Git commit and index tree,
source hashes, assertions, and all three canonical-report comparisons.
The alternative and rest suites have separate receipts.

## What the scientific checks verify

The spectral, transport, and preparation suites check the pole equation,
normalized contact residue, velocity and curvature identities, local-source
probabilities, and scaled wavefunction. The endpoint suite compares two
threshold quadratures, excludes substitution of an above-edge energy, and
checks convergence to the exact-edge coefficient.

The detuning suite compares continuum derivatives with an additional
quadrature, rest scaling, lattice profile and residue convergence, maximizing
momentum diagnostics, and a source-weighted fast-velocity interval.
`tools/detuning.py` explicitly uses the scalar spectral solver.

The finite-time suite checks event-local amplitude accounting, Fourier
smoothing, a separately specified smooth-band control, actual dimer
curvature and gap identities, and continuous-density controls at the three
critical energies. The smooth band and triangular density are analytical
benchmarks. The [certificate](research/FINITE_TIME_CERTIFICATE.md) uses valid
static spectral bounds as inputs to its sufficient-time prescription.

The observation-time suite checks quotient variation, coalescing critical
energies, the actual lattice continuum peak with principal-value
quadrature, band-norm powers, continuum-envelope and relative-error
arithmetic, and active Markdown control characters. The
[joint theorem](research/OBSERVATION_TIME.md) proves the simultaneous limit.

The [alternative estimate](research/ALTERNATIVE_TIME_BOUND.md) has six groups
executed in an isolated temporary layout. The runner verifies its four exact
source blobs, uses the scalar spectral solver, and retains raw reports and
logs.

### Rest-residue and curvature checks

The rest suite independently integrates the defining continuum normalization
and curvature numerator using reciprocal tails and algebraic endpoint
weights. It checks lattice rest integrals at decreasing momentum scales for
$`z=0.6,0.75,0.9`$, and compares curvature with a separate velocity calculation
at $`z=0.75`$. The report retains quadrature errors, finite-scale corrections,
refinement comparisons, and source hashes. The convergence proof is the
[dominated-convergence argument](research/DETUNING_CROSSOVER.md#explicit-rest-residue-and-curvature).

These are finite numerical checks of analytical identities and diagnostic
convergence. Quadrature errors and finite grids are numerical evidence;
rigorous asymptotic statements follow from the linked proofs. In particular,
a waiting-time prescription requires rigorous bounds on its constants.

## Coincidence-tail figure

The [figure](figures/coincidence_tail.svg) evaluates the actual lattice
limiting measure at $`z=3/4`$, with resonance and detunings
$`\delta=0.06,0.09,0.135`$. Its [data](figures/coincidence_tail.json) retain
absolute probabilities, momentum intervals, located cutoffs, quadrature
errors, refinement comparisons, and source hashes.

To recompute it outside the repository:

```bash
python -m pip install -r requirements-figures.txt
python tools/plot_coincidence.py --output /absolute/new/path/coincidence_tail.svg --data /absolute/new/path/coincidence_tail.json
```

The generator integrates $`Z(P)^2dP/\pi`$ over scan-detected positive-momentum
velocity intervals. It compares 72- and 144-cell crossing scans and refined
quadratures at three thresholds per coupling. A cusp-split quadrature checks
the pole, normalized relative wavefunction, and source/contact overlap.
Numerical scans locate cutoffs; the global support theorem is analytical.
Zero probabilities above a cutoff are retained separately on the logarithmic
plot. The right panel uses the absolute probability
$`Q_U(0.9v_{\max})`$.

To render the saved data:

```bash
python tools/plot_coincidence.py --from-data figures/coincidence_tail.json --output /absolute/new/path/coincidence_tail.svg
```

The figure takes the infinite lattice followed by long time at each fixed
coupling and velocity threshold. Its diagnostics run separately from the
42 scientific groups.

## Source and report integrity

The complete 77-file source archive, exact membership, three nested
manifests, and license are checked. The whole source inventory must stay
unchanged during verification. `maintenance/SOURCE_IMPORT.json` records the
source-package digest and baseline; `maintenance/READING_TRANSFORMS.json`
records the generated reading pages and every literal transformation.

The default local command requires byte equality with all three canonical
scientific reports. Hosted CI uses `--allow-numeric-report-differences` to
retain evidence across numerical stacks. This accepts only finite
numeric-only drift while all scientific assertions remain unchanged. The
receipt is labelled `PASS_REQUIRES_NUMERIC_REVIEW` and enumerates every
difference for inspection. Structure, type, source, missing-report, and
assertion failures remain failures. The
[numerical review record](maintenance/NUMERIC_REPORT_REVIEW.json) documents
the reviewed stack differences.

Hosted verification checks the actual PR head and retains all reports and
logs. After verification, successful runs attach `source.tar` from
`git archive HEAD`, containing the tracked files of the tested revision.
After safe extraction, compare every file with `source_sha256` in the main
receipt before reproducing the checks. Verify merged main separately and
compare its exact source tree.

## Reading-page generation

`tools/build_reading.py` generates four research pages from immutable source
sections. It verifies source equation content before applying the recorded
presentation transforms, and records source
hashes, output hashes, selections, and literal substitutions in the transform
ledger. Displays use fenced math, upright operator names, and equation labels
outside TeX to support GitHub's native renderer. Inline expressions use
protected dollar-backtick delimiters; symbolic shorthand in the foundational
prose is typeset through recorded replacements. Edit the generator,
regenerate, and run `--check`. Scientific
reconciliations link the [exact-threshold proof](research/THRESHOLD_ENDPOINT.md)
and [observation-time theorem](research/OBSERVATION_TIME.md).

The other research pages are maintained directly. The
[tutorial bridge](research/TUTORIAL_BRIDGE.md) supplies analytical teaching
derivations, including a nearest-neighbor control outside the fractional
exponent window. Economou's textbook is linked rather than redistributed.
