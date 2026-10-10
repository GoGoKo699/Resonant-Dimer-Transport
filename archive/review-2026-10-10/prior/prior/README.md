# Resonant moving dimers: bounded pilot

Read [the physical question, complete proofs and source comparison](PILOT.md).
The result concerns a two-body spectral branch and its pair-creation weight,
not a demonstrated signal front or an apparatus proposal.

Run the five check groups with a new output filename:

```bash
OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 PYTHONDONTWRITEBYTECODE=1 \
python check_pilot.py --output /absolute/path/to/new-report.json
```

`dimer.py` implements endpoint-regularized quadratures and the contact and
hard-core resolvents in units J=1. The independent continuum calculation
uses 48-digit arithmetic. Numerical constants are not interval certificates.
`RUN_RECORD.json` separates formal checks from preliminary diagnostics.
No earlier research programme or repository is included.
