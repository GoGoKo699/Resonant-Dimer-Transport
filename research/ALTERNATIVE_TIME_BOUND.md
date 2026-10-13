# Alternative conservative finite-time estimate

The [observation-time theorem](OBSERVATION_TIME.md) supplies the sharper sufficient regime. This estimate gives a complementary proof route with explicit constants and critical-energy controls for the same physical event.

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

with explicit constants in Section 3 of the [complete proof](../archive/coarse-time-2026-10-10/research/FINITE_TIME.md). This is compatible with the faster momentum-integrated decay in the main theorem: the estimates control different norms.

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

At $z=3/4$, this sufficient exponent is $37$. The main theorem supplies the less restrictive sufficient regime $Jt\gg\delta^{-7}\sqrt{\log(2/\delta)}$. Both are sufficient bounds obtained by different estimates.

The alternative proof also includes the exact minimum-gap identity, cusp-safe second band derivative, and the Fourier-sandwich estimate. The [finite-time certificate](FINITE_TIME_CERTIFICATE.md) and [observation-time theorem](OBSERVATION_TIME.md) give the static error budget and the sharper joint regime.

## Proof and reproduction

The [complete derivation](../archive/coarse-time-2026-10-10/research/FINITE_TIME.md)
contains the explicit constants. Its six scientific regression groups run in
an isolated temporary layout using the scalar spectral solver.

```bash
python tools/verify_alternative_time.py --output-dir /absolute/new/path/outside/repository
```

The runner verifies source integrity and retains the raw six-group report and
log. The [reproduction guide](../REPRODUCIBILITY.md) includes this suite in the
42 scientific groups.

[Results index](RESULTS.md) · [Main finite-time result](OBSERVATION_TIME.md) · [Reproducibility](../REPRODUCIBILITY.md)
