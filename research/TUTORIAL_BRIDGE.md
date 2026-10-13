# From a single-impurity tutorial to locally observed dimer transport

The teaching source for this route is E. N. Economou,
[*Green's Functions in Quantum Physics*, third edition](https://link.springer.com/book/10.1007/3-540-28841-4)
(Springer, 2006). Its one-body Green's-function methods provide the starting
point: a fixed-total-momentum two-particle problem becomes a relative-coordinate
lattice with one attractive impurity. The additional steps below connect that
construction to the source, detector, and fractional resonance in this project.

The [author account](AUTHOR_ACCOUNT.md) gives the physical question and complete
claims. The [proof map](PROOF_MAP.md) locates the arguments behind this bridge.
Lattice spacing and Planck's constant are one throughout.

## 1. Focused reading in Economou

| Read in the third edition | What to learn | Where it enters here |
|---|---|---|
| Sections 1.1 and 1.3; Section 3.1, pp. 41–42 | Resolvents, discrete poles, eigenfunction residues, and local spectral density | The contact resolvent and its normalized bound-state weight |
| Section 2.1, pp. 21–25 | Frequency Green's functions, boundary prescriptions, and time propagation | The atom-plus-continuum contact amplitude |
| Sections 4.1–4.2, pp. 55–70 | Resolvent identities, the T-matrix, scattering, and shallow bound levels | Summing the contact interaction exactly |
| Sections 5.2–5.3, pp. 80–101 | Tight-binding Hamiltonians and lattice Green's functions | Momentum integrals for the relative kinetic operator |
| Sections 6.1–6.2, pp. 111–124 | A single impurity, its scalar pole equation, and its residue | The exact fiber pole and contact probability |
| Appendix D, pp. 351–353 | Principal-value boundary values and power-law band-edge singularities | Cusp and smooth-edge spectral-density estimates |

The [Chapter 6 preview](https://page-one.springer.com/pdf/preview/10.1007/3-540-28841-4_6)
contains the scalar T-matrix, pole condition, and derivative residue in
Eqs. (6.6), (6.9), and (6.10). Appendix D is in the publisher's
[back matter](https://link.springer.com/content/pdf/bbm:978-3-540-28841-1/1).
These are parts of the same book. Its conductivity and disorder/localization
chapters address other transport questions; the coincidence-velocity theorem
below requires its own argument.

## 2. Translate the notation and the resolvent sign

Use $`w`$ for a complex energy so that $`z`$ remains the fractional exponent.
Let $`\chi(q)=1`$ denote the normalized constant relative-momentum function.
It is the relative-position vector at $`r=0`$; the proof files write this
same vector as $`|1\rangle`$.

| Economou's impurity problem | This project's fiber |
|---|---|
| Free Hamiltonian $`H_0`$ | Multiplication by $`A_P(q)`$ |
| Impurity strength $`\varepsilon`$ | $`-U`$, with $`U>0`$ |
| Impurity site $`\ell`$ | Relative position $`r=0`$, represented by $`\chi`$ |
| Free Green's function $`G_0(w)=(w-A_P)^{-1}`$ | Free resolvent $`R_{0,P}(w)=(A_P-w)^{-1}=-G_0(w)`$ |
| Impurity-site matrix element $`g_{0,P}(w)`$ | $`-I_P(w)`$ |
| Pole energy $`E_p`$ | Relative bound energy $`E_d(P;U)`$ |
| Diagonal pole weight | $`Z(P;U)`$, the normalized contact probability |

The scalar contact integral is

```math
I_P(w)=\langle\chi,(A_P-w)^{-1}\chi\rangle
=\int_{-\pi}^{\pi}\frac{dq}{2\pi}\frac1{A_P(q)-w}.
```

For real $`E`$ below the free band, $`I_P(E)>0`$ and $`I'_P(E)>0`$.
The energy derivative of the book's $`g_{0,P}(E)=-I_P(E)`$ is negative.
At the upper boundary $`w=E+i0`$, the imaginary part of $`I_P`$ is positive,
whereas that of $`g_{0,P}`$ is negative. Thus both conventions give the same
positive free contact density:

```math
\rho_{0,P}(E)=\frac1\pi\mathrm{Im}I_P(E+i0)
=-\frac1\pi\mathrm{Im}g_{0,P}(E+i0).
```

The operator $`(h_P-w)^{-1}`$ has a bound atom proportional to
$`(E_d-w)^{-1}`$; the book's $`(w-h_P)^{-1}`$ has positive residue $`Z`$
in front of $`(w-E_d)^{-1}`$. Switching conventions changes this sign,
not the physical probability.

## 3. Reduce two particles to one impurity at fixed total momentum

Translation invariance conserves total momentum $`P`$. Write the individual
momenta as $`P/2+q`$ and $`P/2-q`$. Their free energies add:

```math
\epsilon_z(k)=J[2-2\cos k]^{z/2},\qquad J > 0,\quad \frac12 < z < 1,
\qquad
A_P(q)=\epsilon_z(q+P/2)+\epsilon_z(q-P/2).
```

The relative coordinate is $`r=x_a-x_b`$. Attraction acts only at $`r=0`$,
so its momentum-space matrix element is constant. Each fiber is therefore

```math
h_P=A_P-U|\chi\rangle\langle\chi|,
\qquad \int_{-\pi}^{\pi}\frac{dq}{2\pi}|\chi(q)|^2=1.
```

The centered coordinates obey $`A_{P+2\pi}(q)=A_P(q+\pi)`$.
Translation of the relative-momentum circle leaves $`\chi`$ unchanged, so
these fibers are unitarily equivalent and $`E_d`$ and $`Z`$ are
$`2\pi`$-periodic in physical total momentum.

This is the book's single-site impurity algebra, with a $`P`$-dependent free
dispersion. The reduction and the fractional dispersion are specified here;
they are not additional models taught by the book.

For this exponent window the free lower edge is $`T_P=\epsilon_z(P)`$.
A relative bound state means $`E_d(P;U)<T_P`$. At resonance and $`P\ne0`$
its energy is positive relative to the global free minimum, while still
below its own fiber continuum. These two energy comparisons are distinct.

## 4. Obtain the pole, normalize its state, and identify contact weight

Summing the rank-one perturbation gives

```math
\langle\chi,(h_P-w)^{-1}\chi\rangle
=\frac{I_P(w)}{1-U I_P(w)},
\qquad I_P(E_d)=\frac1U.
```

These are the book's scalar resolvent and pole condition after the sign
translation above. The bound-state equation also gives its wavefunction
without a separate ansatz:

```math
[A_P(q)-E_d]\psi_P(q)=U\langle\chi,\psi_P\rangle,
\qquad
I'_P(E_d)=\int\frac{dq}{2\pi}\frac1{[A_P(q)-E_d]^2}.
```

Choose a real positive contact amplitude. Normalization and the pole equation
then imply

```math
\psi_P(q)=\frac1{\sqrt{I'_P(E_d)}[A_P(q)-E_d]},
\qquad
\psi_P(r=0)=\int\frac{dq}{2\pi}\psi_P(q)
=\frac1{U\sqrt{I'_P(E_d)}},
\qquad
Z(P;U)=\frac1{U^2I'_P(E_d)}.
```

This is also the contact diagonal of the eigenfunction residue described in
the book's Section 3.1 and Eq. (6.10). It is a probability in a normalized
microscopic eigenstate. A scattering T-matrix or an auxiliary dimer field
can have a different residue normalization; matching its pole alone does
not identify that residue with $`Z`$.

## 5. Work through an ordinary nearest-neighbor control

For this section only, replace the fractional dispersion by
$`\epsilon_{\rm nn}(k)=2J(1-\cos k)`$. This is a separate ordinary lattice
control, outside $`1/2<z<1`$; the fractional threshold formulas do not apply.
For $`-\pi\le P\le\pi`$, put $`a_P=4J\cos(P/2)\ge0`$. Then

```math
A_P^{\rm nn}(q)=4J-a_P\cos q,\qquad
I_P^{\rm nn}(E)=\frac1{\sqrt{(4J-E)^2-a_P^2}},
\qquad E < 4J-a_P.
```

The integral follows from $`\tan(q/2)`$ substitution. Its pole condition and
energy derivative immediately give

```math
E_d^{\rm nn}(P)=4J-\sqrt{U^2+16J^2\cos^2(P/2)},
\qquad
Z^{\rm nn}(P)=\frac{U}{\sqrt{U^2+16J^2\cos^2(P/2)}},
\qquad
\partial_P E_d^{\rm nn}(P)
=\frac{4J^2\sin P}{\sqrt{U^2+16J^2\cos^2(P/2)}}.
```

For every $`U>0`$ the branch is below its continuum and has bounded velocity.
At rest there is a bound state for arbitrarily weak attraction: its threshold
is $`U_c^{\rm nn}=0`$. As $`U\to\infty`$, the contact probability tends to
one and the velocity tends to zero. At $`P=\pi`$ the relative free band is
flat: the contact state itself is the bound eigenstate, with energy
$`4J-U`$ and weight one. The displayed formulas include that endpoint.

This control teaches how poles, normalization, and band velocity fit together.
The fractional result requires a finite rest threshold and a different
low-momentum singularity; ordinary one-dimensional weak binding does not
supply either of those facts.

## 6. Carry both local overlaps into the observed probability

Prepare $`|0,0\rangle`$ and measure the probability $`C_j(t)`$ of both
particles being at site $`j`$. For the fractional model take $`U\ge U_c`$;
the rest fiber at resonance has no bound atom and zero momentum measure.
In each bound fiber both source and detector are
$`\chi`$. The contact spectral amplitude is

```math
c_P(t)=\langle\chi,e^{-ith_P}\chi\rangle
=Z(P)e^{-itE_d(P)}+b_P(t),
\qquad
b_P(t)=\int e^{-itE}w_P(E)\,dE,
\qquad
w_P(E)=\frac{\rho_{0,P}(E)}{|1-U I_P(E+i0)|^2}.
```

The book's pole and continuum language motivates this decomposition. The
[transport proof](TRANSPORT_PROOF.md#2-a-contact-measurement-separates-the-bound-branch-from-the-continuum)
establishes it for this particular dispersion, including the absence of
source-coupled continuum atoms and singular continuous contact spectrum.
Rank one alone would not establish those exclusions for an arbitrary model.

The pole coefficient is already the product of the two amplitudes
$`\langle\chi,\psi_P\rangle`$ and $`\langle\psi_P,\chi\rangle`$.
Fourier-transforming total momentum to the coincident site gives

```math
A_j^d(t)=\int_{-\pi}^{\pi}\frac{dP}{2\pi}
Z(P)e^{iPj-itE_d(P)},\qquad
C_j(t)=|\langle j,j|e^{-itH}|0,0\rangle|^2.
```

After continuum removal, Parseval and the band characteristic-function
argument yield, for every bounded continuous $`f`$,

```math
\lim_{t\to\infty}\sum_j f(j/t)C_j(t)
=\int\frac{dP}{2\pi}Z(P)^2f(E'_d(P)).
```

One factor $`Z`$ is the bound-state excitation probability; the second is
same-site detection probability. Consequently the conserved bound-sector
population and the limiting coincidence mass are

```math
W_b=\int\frac{dP}{2\pi}Z(P),\qquad
W_c=\int\frac{dP}{2\pi}Z(P)^2.
```

All prepared trials remain in the normalization, including noncoincidences.
The projected pole component is not the local initial state by itself.
The continuum cancels its nonlocal part at $`t=0`$, and later disappears only
from the contact amplitude in the stated long-time sense.

## 7. Replace the ordinary band edge by the fractional resonance

At rest $`A_0(q)\sim2J|q|^z`$. Thus $`I_0(0)`$ is finite because $`z<1`$,
giving $`U_c=I_0(0)^{-1}>0`$. The formal threshold wavefunction has divergent
norm because $`\int |q|^{-2z}dq`$ diverges for $`z>1/2`$.

At $`U=U_c`$, subtract the rest loop and scale $`q=|P|x`$:

```math
F_z(e)=\int_{\mathbb{R}}\frac{dx}{2\pi}
\left[\frac1{|x+1/2|^z+|x-1/2|^z-e}-\frac1{2|x|^z}\right],
\qquad F_z(c_z)=0,\quad 0 < c_z < 1.
```

The [spectral proof](SPECTRAL_PROOF.md) justifies the lattice limit and a
separate differentiated limit; it does not differentiate an unspecified
energy remainder. Its conclusions are

```math
E_d(P)\sim Jc_z|P|^z,\qquad
E'_d(P)\sim Jzc_z\mathrm{sgn}(P)|P|^{z-1},\qquad
Z(P)\sim B_z|P|^{2z-1},\qquad
B_z=\frac{J^2}{U_c^2F'_z(c_z)}.
```

Large velocity selects momenta of order $`(J/v)^{1/(1-z)}`$. Integrating
$`Z^2`$ over that interval gives the unconditional coincidence tail

```math
Q(v)\sim\frac{B_z^2}{\pi(4z-1)}
\left(\frac{zc_zJ}{v}\right)^{(4z-1)/(1-z)}.
```

The infinite lattice comes first, then long time at fixed $`v`$, then large
$`v/J`$. Unbounded limiting support does not imply a finite coincidence
fraction moving faster than every linear scale or a finite-time arrival guarantee.

## 8. Follow the additional proof steps

Economou supplies the resolvent methods and edge vocabulary. The following
model-specific arguments connect them to the complete results. Their inherited
research ingredients are credited in the [contribution assessment](CONTRIBUTION.md).

| Next question | Project proof and essential additional step |
|---|---|
| Why does a moving bound state exist at the rest threshold? | [Spectral foundation](SPECTRAL_PROOF.md): exact fractional lattice edge, pole bracketing, scaled subtraction, and separately controlled derivatives |
| Can the continuum edge be replaced by its leading approximation? | [Threshold endpoint](THRESHOLD_ENDPOINT.md): keep the exact lattice energy at the edge and dominate its cusp zeros before rescaling |
| How does stronger attraction restore a finite cutoff? | [Detuning crossover](DETUNING_CROSSOVER.md): $`\delta=J(U_c^{-1}-U^{-1})`$, $`\rho=\delta^{1/(1-z)}`$; control all momenta to prove $`v_{\max}\sim JK_z/\delta`$ |
| What probability accompanies that cutoff? | [Detuning crossover](DETUNING_CROSSOVER.md#2-crossover-theorem): the same two overlaps give near-cutoff weight of order $`\delta^{(4z-1)/(1-z)}`$ |
| How do rest residue and effective mass approach resonance? | [Explicit rest coefficients](DETUNING_CROSSOVER.md#explicit-rest-residue-and-curvature): a separate cusp-safe curvature integral gives $`Z(0)\asymp\rho^{2z-1}`$ and $`m_d\asymp J^{-1}\rho^{2-z}`$ |
| How much relative support can prepare a fast state? | [Theorem, Section 4](THEOREM.md#4-scaled-relative-wavefunction-and-preparation-size): normalized wavefunction scaling and optimal restricted overlap; fixed capture requires radius of order $`1/\lvert P\rvert`$ |
| How does edge structure affect continuum decay? | [Boundary resolvent](BOUNDARY_RESOLVENT.md): explicit cusp, smooth-maximum, and principal-value estimates; [observation time](OBSERVATION_TIME.md) also treats merging critical energies |
| When does a sharp rare event approach its limiting probability? | [Finite-time certificate](FINITE_TIME_CERTIFICATE.md): event-local amplitude error and band smoothing; [joint observation time](OBSERVATION_TIME.md): uniform momentum-integrated decay and detuning-dependent band norms |

For example, at $`z=3/4`$ the near-cutoff event has probability of order
$`\delta^8`$, while the sufficient joint regime is
$`Jt\delta^7/\sqrt{\log(2/\delta)}\to\infty`$. This is not a necessary or
optimal waiting-time law, and its constants do not provide a certified
numerical operating window.

[Author account](AUTHOR_ACCOUNT.md) · [Results](RESULTS.md) · [Proof map](PROOF_MAP.md)
