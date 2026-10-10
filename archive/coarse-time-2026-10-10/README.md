# Preserved alternative finite-time estimate

This directory preserves four exact source files from commit `aa27c02fdb694fa8effbac3b670be50ee8b323fd` of the same repository. They supply the independent, conservative critical-energy-collar proof and its six regression groups. They are supporting sources, not replacements for the main observation-time theorem or its helpers.

The [active explanation](../../research/ALTERNATIVE_TIME_BOUND.md) compares the sufficient regimes and gives the reproduction command. The [original proof](research/FINITE_TIME.md), [helper](tools/finite_time.py), [checker](tools/check_finite_time.py), and [review record](maintenance/FINITE_TIME_REVIEW.json) are byte-preserved. `PROVENANCE.json` fixes their Git blob identifiers.

Original relative references in the proof refer to the repository's canonical `research/` directory, and original code references assume its earlier layout. The dedicated runner reproduces that layout only in a new temporary directory outside the source tree. Do not edit an imported source, normalize it, or loosen a test. Current helper modules with overlapping historical filenames remain separate.
