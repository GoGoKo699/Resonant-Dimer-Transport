# Scientific results and proof index

## Fixed physical task

Two distinguishable particles move on the infinite one-dimensional lattice with dispersion

```math
\epsilon_z(k)=J[2-2\cos k]^{z/2},\qquad J > 0,\quad \frac12 < z < 1,
```

and contact attraction $`-U\delta_{x_a,x_b}`$. The preparation is $`|0,0\rangle`$. The measured probability is $`C_j(t)=|\langle j,j|e^{-itH}|0,0\rangle|^2`$, per initially prepared pair. Unequal final positions remain in the normalization. There is no band-prepared source, energy filtering, or time-averaged detector.

This index connects each result to its complete proof. The
[author account](AUTHOR_ACCOUNT.md) supplies the physical explanation and
primary references.

## Result map

| Result | Precise content | Complete derivation |
|---|---|---|
| Rest resonance and moving bound branch | At $`U_c=2^{1+z}J\sqrt\pi\,\Gamma(1-z/2)/\Gamma((1-z)/2)`$ there is no normalizable rest dimer, while every nonzero total momentum has one below-continuum relative bound state. | [Spectral foundation](SPECTRAL_PROOF.md) |
| Resonant energy, velocity, and source weight | $`E_d(P)\sim c_zJ\lvert P\rvert^z`$, $`\lvert E'_d(P)\rvert\sim zc_zJ\lvert P\rvert^{z-1}`$, and $`Z(P)\sim B_z\lvert P\rvert^{2z-1}`$. The derivative has its own controlled derivation. | [Spectral foundation](SPECTRAL_PROOF.md) |
| Correct threshold endpoint | The endpoint resolvent expansion uses $`E_{\rm th}(P)=\epsilon_z(P)`$, not the continuum approximation $`J\lvert P\rvert^z`$ that lies above the lattice edge. | [Exact-threshold lemma](THRESHOLD_ENDPOINT.md) |
| Source-resolved coincidence law | The long-time measure is the pushforward of $`Z(P)^2dP/(2\pi)`$ by $`E'_d(P)`$. The contact continuum contribution vanishes, not the full scattering state. | [Transport proof](TRANSPORT_PROOF.md) |
| Resonance contrast | The resonant limiting coincidence tail has exponent $`(4z-1)/(1-z)`$. At each fixed $`U>U_c`$, limiting velocities have bounded support. | [Transport proof](TRANSPORT_PROOF.md), [spectral foundation](SPECTRAL_PROOF.md) |
| Internal preparation size | The scaled normalized relative wavefunction has an $`L^2`$ limit. Fixed capture probability requires radius $`\Theta(\lvert P\rvert^{-1})=\Theta((v/J)^{1/(1-z)})`$. | [Theorem, Section 4](THEOREM.md) |
| Detuning crossover | For $`\delta=J(U_c^{-1}-U^{-1})>0`$, $`v_{\max}\sim K_zJ/\delta`$ and every maximizing momentum is $`\Theta(\delta^{1/(1-z)})`$. The near-cutoff probability and full scaled profile include both overlaps. | [Detuning theorem](DETUNING_CROSSOVER.md) |
| Rest residue and effective mass | With $`\rho=\delta^{1/(1-z)}`$, the rest contact weight is proportional to $`\rho^{2z-1}`$ and the curvature to $`J\rho^{z-2}`$, with explicit coefficients. The curvature limit is proved directly from the lattice integral. | [Rest crossover coefficients](DETUNING_CROSSOVER.md#explicit-rest-residue-and-curvature) |
| Finite-time certificate | A deterministic-time error bound for the sharp position event combines a velocity-shell mass, band norms, and event-local continuum amplitude. | [Finite-time certificate](FINITE_TIME_CERTIFICATE.md) |
| Uniform observation-time regime | Momentum-integrated continuum amplitude is bounded by $`C/(Jt)`$ uniformly near resonance. Sharper band norms give the sufficient time profile below. | [Observation-time theorem](OBSERVATION_TIME.md) |
| Alternative conservative time estimate | A critical-energy collar argument gives explicit continuum constants and a more conservative sufficient time requirement. | [Alternative estimate](ALTERNATIVE_TIME_BOUND.md) |
| Continuous spectral-peak control | A narrow peak above an interior continuum maximum makes a momentum-uniform variation bound false. Its height, shift, and width are calculated without treating it as another eigenstate. | [Observation-time theorem, Section 5](OBSERVATION_TIME.md) |
| Boundary resolvent estimates | Cusp Cauchy transforms, full-coefficient Morse decomposition, and simple-root principal-value subtraction justify the continuum estimates used in the finite-time proofs. | [Boundary resolvent derivation](BOUNDARY_RESOLVENT.md) |

## Two distinct finite-time statements

The static certificate controls the same sharp detector through

```math
|p_t(s)-q(s)|\le d_t+2\sqrt{q(s)+d_t}\,e_t+e_t^2,
```

where $`d_t`$ is the band-event error budget and $`e_t`$ is the contact-continuum amplitude budget. The event-local square root is essential: an event of probability $`q`$ needs amplitude error small relative to $`\sqrt q`$, not necessarily $`q`$. The explicit static prescription and its margins are in [the certificate](FINITE_TIME_CERTIFICATE.md).

The [uniform theorem](OBSERVATION_TIME.md) then controls those budgets as the detuning vanishes. With fixed $`0<\theta<1`$, set

```math
p_{\delta,t}=\Pr_U(x_a=x_b,|X| > \theta v_{\max}(U)t),\qquad
q_\delta=Q_U(\theta v_{\max}(U))\sim C_{z,\theta}\delta^{(4z-1)/(1-z)}.
```

For each fixed relative accuracy there are detuning-independent constants such that $`Jt\ge C\mathcal T_z(\delta)`$ is sufficient, where

```math
\mathcal T_z(\delta)=
\begin{cases}
\delta^{-(3z-1/2)/(1-z)},&1/2 < z < 3/4,\\
\delta^{-7}\sqrt{\log(2/\delta)},&z=3/4,\\
\delta^{-(5z-2)/(1-z)},&3/4 < z < 1.
\end{cases}
```

Along $`Jt/\mathcal T_z(\delta)\to\infty`$, the ratio $`p_{\delta,t}/q_\delta`$ tends to one. These are sufficient bounds for relative accuracy. The case distinction comes from the band norms in the proof.

## Interpretation and evidence

Binding is relative to the continuum at the conserved total momentum. Same-site detection, bound-sector population, and overlap with a selected extended eigenstate are different quantities. Unbounded support of a limiting velocity law is not a finite-weight superballistic front, a strict finite-time light cone, or an efficient loading protocol. The sufficient joint regime does not prove that shorter times are inadequate.

The contact scattering framework, momentum-induced lattice binding, fractional kinetic operator, and nearby-pair detection have explicit predecessors. The [contribution account](CONTRIBUTION.md) and primary-source sections give those attributions.

The [reproduction guide](../REPRODUCIBILITY.md) maps the 33 main scientific check groups, six alternative-estimate groups, three rest-crossover groups, and eight infrastructure checks to their scripts and reports. The numerical checks support the analytical account through exact identities, finite-scale comparisons, and quadrature diagnostics.

[Reader entry point](../README.md) · [Proof dependencies](PROOF_MAP.md)
