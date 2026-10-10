# Alternative conservative finite-time estimate

The main [observation-time theorem](OBSERVATION_TIME.md) supplies the sharper sufficient regime used in the scientific account. A separately derived estimate is retained here because its explicit constants and critical-energy controls provide a different proof route. It does not add a second physical model or a stronger operational claim.

## Same event, more conservative sufficient condition

Use the same local onsite source, unconditional sharp coincidence measurement, and parameters

$$
\delta=J(U_c^{-1}-U^{-1})>0,\qquad
\alpha_z=\frac{4z-1}{1-z},\qquad \frac12<z<1.
$$

The alternative argument cuts out energy collars around the free-fiber critical values, bounds their mass, and integrates by parts on the regular complement. It gives a momentum-uniform pointwise estimate

$$
|b_P(t)|\le\min\{1,\mathcal C_z(Jt)^{-\gamma_z}\},\qquad
\gamma_z=\frac{4z-2}{10-z},
$$

with explicit, deliberately nonoptimized constants in Section 3 of the [preserved proof](../archive/coarse-time-2026-10-10/research/FINITE_TIME.md). This is compatible with the faster momentum-integrated decay in the main theorem: the estimates control different norms and neither is asserted to be optimal.

Combined with conservative band bounds and event-local interference accounting, the alternative proof establishes

$$
Jt_\delta\,\delta^{M_z}\longrightarrow\infty
\quad\Longrightarrow\quad
\frac{p_\delta(t_\delta;\theta)}{\delta^{\alpha_z}}
\longrightarrow \left(\frac J{U_c}\right)^4\mathcal H_z(\theta K_z),
$$

where

$$
M_z=\frac{(4z-1)(10-z)}{4(1-z)(2z-1)},\qquad 0<\theta<1.
$$

At $z=3/4$, this sufficient exponent is $37$. The main theorem instead supplies the substantially less restrictive sufficient regime $Jt\gg\delta^{-7}\sqrt{\log(2/\delta)}$. These are upper-bound constructions, not competing predictions for an optimal waiting time. No actual infinite-lattice evolution at either diverging time scale was simulated.

The alternative proof also includes the exact minimum-gap identity, cusp-safe second band derivative, and the Fourier-sandwich estimate. The current [finite-time certificate](FINITE_TIME_CERTIFICATE.md) and [observation-time theorem](OBSERVATION_TIME.md) remain the direct reading route for the accumulated result.

## Preserved sources and separate reproduction

The [source snapshot](../archive/coarse-time-2026-10-10/README.md) retains the exact proof, helper, checker, and review record from the parallel finite-time branch. These original bytes are neither rewritten to match the newer notation nor allowed to overwrite the current helper with the same historical filename. Its six scientific regression groups run unchanged in an isolated temporary layout, using the already preserved spectral solver.

```bash
python tools/verify_alternative_time.py --output-dir /absolute/new/path/outside/repository
```

The runner checks every imported blob and confirms that its source files remain unchanged. It keeps the raw six-group report and log. Its success is author-side reproduction, not an independent theorem audit or a certificate for a practical waiting time. The main 33-group suite is still run separately by `tools/verify.py`; hosted verification requires both suites.

[Results index](RESULTS.md) · [Main finite-time result](OBSERVATION_TIME.md) · [Reproducibility](../REPRODUCIBILITY.md)
