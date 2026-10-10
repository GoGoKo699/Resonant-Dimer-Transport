# Resonant dimer: local-source transport follow-up

A local pair source reveals the fractional bound branch through a persistent coincidence-velocity distribution. At resonance it has an algebraic unbounded tail; at fixed stronger binding its limiting velocity support is bounded. The source and detector weights suppress the tail but do not remove it. This is not a finite-weight superballistic front or a strict finite-time light cone.

Read [the derivation and contribution assessment](FOLLOWUP.md). The original [spectral pilot](prior/PILOT.md) is preserved byte-for-byte. `check_transport.py` runs five current groups; `prior/check_pilot.py` runs the five original groups. Both require a fresh `--output` JSON path and refuse to overwrite it. `transport.py` explicitly reuses this candidate's original scalar integrals.

The task remains the same two-particle contact model and specified position measurement. No repository was created or changed. See `RUN_RECORD.json` for actual verification, limitations and provenance.
