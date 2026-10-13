# Boundary resolvent estimates at the scattering energies

This appendix supplies the local Cauchy-transform calculations used in
the [finite-time certificate](FINITE_TIME_CERTIFICATE.md), Eqs. (F13)–(F14),
and the [joint observation-time proof](OBSERVATION_TIME.md), Eqs. (O9)–(O11).
It concerns the existing contact resolvent and its energy derivative. The
Hamiltonian, source, detector, and sufficient-time exponents are unchanged.

Write

```math
I_P(w)=\int\frac{dq}{2\pi}\frac1{A_P(q)-w},\qquad
A_P(q)=\epsilon_z(q+P/2)+\epsilon_z(q-P/2).
```

The upper-half-plane convention is important:

```math
\frac1{s-\omega-i0}=\mathrm{PV}\frac1{s-\omega}
   +i\pi\delta(s-\omega),\qquad
\mathrm{Im}I_P(\omega+i0)=\pi\rho_{0,P}(\omega)\ge0.
```

Thus the continuous contact density is

```math
w_{P,U}(\omega)=\frac1{\pi U^2}
\frac{v(\omega)}{u(\omega)^2+v(\omega)^2},\quad
u=\mathrm{Re}I_P-1/U,\quad v=\mathrm{Im}I_P.
```

All local neighborhoods below can first be chosen with fixed boundaries
in the integration variable. Differentiation then introduces no moving
boundary term. A change of variables is used to estimate the resulting
integrals, not to replace an on-shell principal value by an ordinary integral.

## 1. A cusp threshold

Put $`\beta=(1-z)/z\in(0,1)`$. Near either minimum $`q_0=\pm P/2`$, at a
fixed $`0<P<\pi`$, the free dispersion has the form

```math
A_P(q_0+x)-T_P=J|x|^z+g_P(x),\qquad g_P(x)=O(x).
```

On each side, the analytic regular term and the chord correction allow the
inverse branch to be differentiated. Solving for $`|x|`$ gives
$`|x|=(y/J)^{1/z}[1+O(y^\beta)]`$, with the corresponding first two
derivative bounds. Summing its positive inverse Jacobians gives, on a
sufficiently small energy interval,

```math
\rho_{0,P}(T_P+y)=c_Py^\beta+r_P(y),\qquad c_P > 0,
```
```math
|r_P^{(j)}(y)|\le C y^{\beta+\lambda-j},\qquad j=0,1,2,
```

for some $`\lambda>0`$; $`\lambda=\beta`$ is sufficient. These bounds follow
by differentiating the inverse equation on either side of the cusp, where
the leading derivative $`Jz|x|^{z-1}`$ dominates the regular derivative.
On a compact momentum interval away from zero and $`\pi`$, all constants
are uniform. The same statement holds uniformly near small positive $`P`$
after scaling $`q=Px`$ and $`\omega=JP^ze`$: the two cusp neighborhoods are
then centered at fixed $`x=\pm1/2`$ and their regular coefficients remain
bounded.

The leading local Cauchy integral can be evaluated directly. For a fixed
upper endpoint $`a>0`$ and $`0<y<a/2`$, let

```math
K_\beta(y)=\int_0^a\frac{r^\beta}{r-y-i0}\,dr.
```

Subtracting its edge value before scaling yields

```math
K_\beta(y)-K_\beta(0)
=y^\beta\int_0^{a/y}\frac{x^{\beta-1}}{x-1-i0}\,dx
=\pi[-\cot(\pi\beta)+i]y^\beta+O(y).
```

Here the principal-value integral over $`(0,\infty)`$ is
$`-\pi\cot(\pi\beta)`$ and the on-shell imaginary contribution is
$`+i\pi`$. The omitted large-$`x`$ tail has size $`O(y)`$ and derivative
$`O(1)`$. Consequently

```math
K_\beta'(y)
=\pi\beta[-\cot(\pi\beta)+i]y^{\beta-1}+O(1).
```

The remainder density has the same required, weaker bounds without an
explicit coefficient. To see this, set $`\gamma=\beta+\lambda>\beta`$ and
split its subtracted Cauchy integral into $`r<y/2`$, $`y/2<r<2y`$, and
$`r>2y`$. The first region is estimated using the symbol bounds above. In
the middle region subtract the value at $`r=y`$; for its derivative subtract
also the first Taylor polynomial. The second derivative bound controls
the resulting regular integrand. On the last region use
$`|r-y|\ge r/2`$. The bounds for the remainder difference and derivative are
respectively

```math
\begin{cases}O(y^\gamma),\ O(y^{\gamma-1}),&\gamma < 1,\\
O(y\log(2/y)),\ O(\log(2/y)),&\gamma=1,\\
O(y),\ O(1),&\gamma > 1.
\end{cases}
```

Each is bounded by $`O(y^\beta)`$ and $`O(y^{\beta-1})`$, respectively.
The contribution outside the cusp neighborhoods is $`C^1`$ in energy,
because its denominator stays separated from zero. Therefore

```math
I_P(T_P+y+i0)-I_P(T_P)=O(y^\beta),\qquad
\partial_yI_P(T_P+y+i0)=O(y^{\beta-1}).
```

For the interacting density, the threshold denominator is nonzero:
$`I_P(T_P)>1/U_c\ge1/U`$. On compact positive momentum intervals this
separation is uniform. In small-momentum scaled units the
[exact-threshold lemma](THRESHOLD_ENDPOINT.md) gives the positive limiting
separation $`F_z(1)>0`$; adding $`\lambda=\delta/P^{1-z}\ge0`$ preserves it.
Differentiating the exact quotient hence gives (F13) and the cusp part of
the uniform estimate in the observation-time proof. The density tends to
zero at the edge, so extension by zero adds no jump variation there.

## 2. A smooth maximum and its full analytic coefficient

Consider a nondegenerate local maximum of energy $`M_P`$. In a Morse
coordinate with fixed radius $`a`$, its dispersion is $`M_P-t^2`$. Let
$`j_P(t)`$ be the positive coordinate Jacobian, including the measure
factor $`1/(2\pi)`$. The odd part integrates to zero. Its even part is
$`h_P(t^2)`$, with $`h_P`$ real analytic and $`h_P(0)>0`$. For
$`\zeta=\omega-M_P+i0`$, the exact contribution is

```math
-\int_{-a}^a\frac{h_P(t^2)}{t^2+\zeta}\,dt.
```

Use the analytic division identity

```math
h_P(t^2)=h_P(-\zeta)+(t^2+\zeta)k_P(t^2,\zeta).
```

The divided difference $`k_P`$ is analytic even when $`t^2=-\zeta`$. Also,

```math
\int_{-a}^a\frac{dt}{t^2+\zeta}
=\frac{\pi}{\sqrt\zeta}-\frac2a+O(\zeta),
```

where the square root is positive for $`\zeta>0`$ and has its cut on the
negative real axis. The finite-endpoint remainder is analytic for
$`|\zeta|<a^2`$. Combining the two identities gives the exact local form

```math
-\frac{H_P(\zeta)}{\sqrt\zeta}+R_P^{\mathrm{loc}}(\zeta),\qquad
H_P(\zeta)=\pi h_P(-\zeta).
```

Both coefficient functions are analytic, and $`H_P`$ is positive for small
real $`\zeta`$. A uniform positive curvature and uniform analytic Jacobian
bounds give uniform bounds for $`H_P`$, its first derivative, and the
first derivative of $`R_P^{\mathrm{loc}}`$. Retaining the full $`H_P`$ is
essential: subtracting only $`H_P(0)/\sqrt\zeta`$ leaves a square-root
remainder whose derivative is unbounded.

Below the maximum, $`\sqrt{-y+i0}=i\sqrt y`$, so the singularity is
$`+iH_P(-y)/\sqrt y`$. Above it, the singularity is the negative real term
$`-H_P(y)/\sqrt y`$. At an interior maximum, the other on-shell roots
give a smooth boundary contribution with imaginary part bounded above
and below by positive constants; Section 3 proves its $`C^1`$ regularity.
The resulting normal forms are precisely those of (O9). In particular,
the real part is $`C^1`$ below the maximum and is monotone sufficiently
close to it on the upper side; the imaginary singularity is monotone
sufficiently close to it on the lower side.

Inserting these forms in $`v/(u^2+v^2)`$ gives (F14). Below either maximum
the quotient is $`O(\sqrt y)`$ with derivative $`O(y^{-1/2})`$. Immediately
above an interior maximum, $`u^2\asymp y^{-1}`$ while $`v`$ is bounded
and smooth, giving quotient $`O(y)`$ and derivative $`O(1)`$. These
derivatives are integrable, and the quotient limits are zero.

For small $`P`$, the inner maximum must be treated in the variables
$`q=Px`$, $`\omega=JP^ze`$ before applying this construction. The curvature
of the dimensionless dispersion $`A_P(Px)/(JP^z)`$ at the inner maximum
tends to $`-2z(1-z)2^{2-z}`$, and the outer roots stay
separated from the two cusps. Thus the scaled coefficients are uniform.
For $`P`$ near $`\pi`$, choose two disjoint Morse neighborhoods around the
two upper maxima. The rest of the dispersion lies a fixed energy distance
below them. Its resolvent contribution is then real analytic, and the sum
of the two exact local forms gives the decomposition in Section 2.4 of
the observation-time proof, including its uniformly $`C^1`$ real remainder.
No separation of the two *energies* is required to obtain these uniform
coordinate bounds.

## 3. Simple on-shell roots and the intermediate-energy estimates

The regular boundary transform can be differentiated without an absolute
integral through its pole. Suppose a root neighborhood has been changed
to its dispersion value $`s\in[a,b]`$, and its inverse-branch density is
$`d(s)`$. Let $`e`$ range in a fixed compact subinterval of $`(a,b)`$.
If $`d`$ is $`C^2`$, then

```math
\int_a^b\frac{d(s)}{s-e-i0}\,ds
=d(e)\log\frac{b-e}{e-a}
 +\int_a^b\frac{d(s)-d(e)}{s-e}\,ds+i\pi d(e).
```

The quotient in the regular integral has a continuous value at $`s=e`$.
Its energy derivative is

```math
\frac{d(s)-d(e)-d'(e)(s-e)}{(s-e)^2},
```

bounded by $`\|d''\|_\infty/2`$. The logarithm and its derivative are
bounded because $`e`$ stays away from $`a,b`$. This proves uniform $`C^1`$
boundary bounds from uniform $`C^2`$ inverse densities and root separation.
It also fixes the positive sign of the imaginary term. Such bounds hold
near the outer roots used in Section 2: their dispersion slopes are
nonzero, and their neighborhoods do not meet either cusp.

For the intermediate-energy region of (O10), set $`J=1`$ and choose a
reference energy $`\omega>0`$. Write

```math
h=\omega^{1/z},\qquad k=P/h\le k_0,
\qquad B_{h,k}(x)=\frac{A_P(hx)}\omega.
```

Take $`k_0>0`$ sufficiently small and $`\omega`$ sufficiently small. On fixed
$`x`$ intervals, $`B_{h,k}`$ tends to
$`|x+k/2|^z+|x-k/2|^z`$. Its roots at energy one remain near the two
simple roots of $`2|x|^z=1`$, with uniformly nonzero slopes. They stay a
fixed distance from the cusps at $`\pm k/2`$. The root-neighborhood
construction above therefore has uniform $`C^2`$ inverse densities, with
their values bounded above and below by positive constants. Since
$`dq/d\omega`$ contributes the scale $`h/\omega=\omega^\beta`$, the
on-shell imaginary part obeys

```math
c\omega^\beta\le\mathrm{Im}I_P(\omega+i0)
\le C\omega^\beta.
```

To bound the subtracted real part, use the same fixed root neighborhoods
and their regular principal-value formula. On the scaled complement the
roots are absent. At $`x=0`$ the rest subtraction has the integrable
singularity $`|x|^{-z}`$. For large $`|x|`$, the symmetric shift and chord
bounds give a subtracted integrand bounded by

```math
C\bigl(|x|^{-2z}+k^2|x|^{-z-2}\bigr).
```

This tail is integrable uniformly because $`2z>1`$. Restoring the factor
$`h/\omega`$ gives
$`|\mathrm{Re}I_P(\omega+i0)-I_0(0)|\le C\omega^\beta`$.
The fixed outer lattice region contributes $`O(\omega+P^2)`$; since
$`P\le k_0\omega^{1/z}`$ and $`\beta<1`$, this fits the same bound.

For the energy derivative keep $`P`$ and the integration neighborhoods
fixed at the reference energy, and vary the energy as $`\omega e`$ for
$`e`$ in a fixed neighborhood of one. The regular principal-value formula
proves a uniform derivative with respect to $`e`$. On its off-shell
complement the differentiated scaled kernel has tail $`O(|x|^{-2z})`$;
near the off-shell cusps its denominator is separated from zero. Hence
the energy derivative has the factor $`h/\omega^2`$ and obeys

```math
|\partial_\omega I_P(\omega+i0)|\le C\omega^{\beta-1}.
```

The fixed outer lattice region contributes only $`O(1)`$, also within this
bound. This proves all three estimates of (O10), including the boundary
derivative, without differentiating a pointwise continuum remainder.

Finally, $`I_0(0)-1/U=\delta\ge0`$ in these dimensionless units.
Write $`\mathrm{Re}I_P-I_0(0)=r`$ and
$`v=\mathrm{Im}I_P`$. If $`\delta>2C\omega^\beta`$, then
$`|\delta+r|\ge\delta/2`$. Otherwise $`v\ge c\omega^\beta`$ controls
$`\delta+\omega^\beta`$. Thus

```math
|I_P(\omega+i0)-1/U|\ge c'(\delta+\omega^\beta).
```

The gradient of $`v/(u^2+v^2)`$ has magnitude at most
$`C/(u^2+v^2)`$. Combining the denominator bound with the boundary
derivative yields (O11). Its variation integral is bounded using the
substitution $`x=\omega^\beta`$:

```math
\int_{RP^z}^{\omega_0}
\frac{\omega^{\beta-1}}{(\delta+\omega^\beta)^2}\,d\omega
\le\frac{1}{\beta[\delta+(RP^z)^\beta]}
\le\frac{C}{\delta+P^{1-z}}.
```

Together with the scaled lower-critical-energy region and the global
maximum calculation, these estimates justify the variation envelope
(O4). Its momentum square is integrable for $`z>1/2`$, which is the
precise input for the continuum-amplitude estimate (O6). Restoring $`J`$
uses energy $`\omega/J`$ and multiplies energy variation by $`J^{-1}`$.

[Finite-time certificate](FINITE_TIME_CERTIFICATE.md) ·
[Joint observation-time proof](OBSERVATION_TIME.md) ·
[Exact threshold](THRESHOLD_ENDPOINT.md)
