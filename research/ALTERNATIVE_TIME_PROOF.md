# Alternative finite-time proof for the near-resonance coincidence event

## 1. Result and meaning of the time bound

Keep the infinite-lattice Hamiltonian, onsite source $`|0,0\rangle`$, and
unconditional same-site position measurement. Fix $`J>0`$ and $`1/2<z<1`$.
As in the [detuning theorem](DETUNING_CROSSOVER.md), write

```math
\delta=J(U_c^{-1}-U^{-1}) > 0,\quad
\rho=\delta^{1/(1-z)},\quad
\alpha_z=\frac{4z-1}{1-z},\quad \tau=Jt.
```

For $`0<\theta<1`$ fixed, define the **finite-time** probability

```math
p_\delta(t;\theta)=\sum_{|j| > \theta v_{\max}(U)t}
|\langle j,j|e^{-itH_U}|0,0\rangle|^2.
```

Theorem. Set

```math
\gamma_z=\frac{4z-2}{10-z} > 0,\qquad
M_z=\frac{\alpha_z}{2\gamma_z}
=\frac{(4z-1)(10-z)}{4(1-z)(2z-1)}.
```

**(F1)**

For any deterministic choice of finite times $`t_\delta`$ satisfying

```math
\boxed{Jt_\delta\,\delta^{M_z}\longrightarrow\infty,}
```

**(F2)**

one has the **joint time-detuning limit**

```math
\boxed{\frac{p_\delta(t_\delta;\theta)}{\delta^{\alpha_z}}
\longrightarrow
\left(\frac J{U_c}\right)^4\mathcal H_z(\theta K_z) > 0.}
```

**(F3)**

Here $`K_z`$ and $`\mathcal H_z`$ are the velocity-cutoff constant and
source/detector-weighted crossover function. Equivalently,
$`p_\delta(t_\delta;\theta)/Q_U(\theta v_{\max}(U))\to1`$.
The time need not be selected from a subsequence of favorable oscillations;
there is no time average, randomized waiting time, band-prepared source,
or changed detector.

For $`z=3/4`$, $`\gamma_z=4/37`$, $`M_z=37`$, and $`\alpha_z=8`$. Thus
$`Jt_\delta=\delta^{-37}\log(1/\delta)`$ is one sufficient choice as
$`\delta\downarrow0`$. **The exponent 37 is not an optimal or necessary waiting
time, a physical relaxation exponent, or an experimental operating estimate.**
It comes from deliberately coarse uniform bounds below. Constants are large;
a quantitative apparatus proposal or a useful finite-parameter observation
time would require much sharper estimates. The infinite lattice is still
part of the model; this result does not interchange lattice size with time.

Sections 2–5 prove a nonasymptotic event-error bound; Section 6 deduces (F3).

## 2. Uniform decay of the contact continuum amplitude

Use dimensionless energy $`e=E/J`$, coupling $`u=U/J`$, and dispersion
$`f(q)=|2\sin(q/2)|^z`$. Put

```math
a_P(q)=f(q+P/2)+f(q-P/2),\qquad
m_P(w)=\int_{-\pi}^{\pi}\frac{dq}{2\pi}\frac1{a_P(q)-w}.
```

The [contact spectral decomposition](TRANSPORT_PROOF.md) supplies

```math
c_P(t)=Z(P)e^{-i\tau\lambda(P)}+b_P(t),\quad
\lambda(P)=E_d(P;U)/J,
```
```math
b_P(t)=\int e^{-i\tau e}w_{P,u}(e)\,de,\quad
w_{P,u}(e)=\frac{r_P(e)}{|1-u m_P(e+i0)|^2},\quad
\mathrm{Im}m_P(e+i0)=\pi r_P(e).
```

**(F4)**

Here $`r_P`$ is the free density obtained by pushing forward $`dq/(2\pi)`$
under $`a_P`$. The decomposition has no additional source-coupled singular
component. The single exceptional rest fiber at resonance can be ignored
in momentum integrals. The estimate below is uniform in $`P`$ and $`u\ge u_c`$,
where $`u_c=U_c/J>0`$ at fixed $`z`$:

```math
\boxed{|b_P(t)|\le\min\{1,\mathcal C_z\tau^{-\gamma_z}\}
\quad(\tau\ge1).}
```

**(F5)**

In particular $`\eta(t)^2=\int |b_P(t)|^2dP/(2\pi)`$ satisfies the same squared
bound. An explicit, nonoptimized $`\mathcal C_z`$ is given in Section 3.

### 2.1 Free geometry and a density envelope

By symmetry it suffices to take $`0\le P\le\pi`$. The critical energy values are

```math
T_P=f(P),\qquad B_{0,P}=2f(P/2),\qquad
B_{\pi,P}=2f(\pi-P/2),\qquad
T_P\le B_{0,P}\le B_{\pi,P} < 4.
```

On $`(0,P/2)`$ the function $`a_P`$ decreases from $`B_{0,P}`$ to $`T_P`$;
on $`(P/2,\pi)`$ it increases from $`T_P`$ to $`B_{\pi,P}`$. The first arc
vanishes at $`P=0`$; the two maxima have equal energy at $`P=\pi`$.
On both open arcs,

```math
a_P''(q)\le-m_z,\qquad m_z=z(1-z)2^{z-1} > 0.
```

**(F6)**

Indeed, for $`0<k<2\pi`$,
$`f''(k)=-z2^{z-2}\sin^{z-2}(k/2)[1-z\cos^2(k/2)]`$.
The upper arc alone provides a preimage at every interior band energy.
Write $`q=P/2+d`$ on this arc and $`s=e-T_P>0`$. Hölder continuity gives
$`s\le2d^z`$, while

```math
0 < a_P'(q)\le2L_1d^{z-1},\qquad
L_1=z(2/\pi)^{z-1}.
```

To see the derivative bound, when $`P+d\le\pi`$ both terms are bounded by
$`L_1d^{z-1}`$; when $`P+d>\pi`$ that term has negative derivative and can be
dropped from an upper bound. The even reflected preimage contributes too.
With

```math
r=\frac{1-z}{z}\in(0,1),\quad \beta=1-r=2-1/z > 0,\quad
c=\frac1{\pi\,2^{1+r}L_1},
```

the coarea formula implies

```math
r_P(e)\ge c(e-T_P)^r.
```

Using only the imaginary part of the denominator in (F4),

```math
\boxed{0\le w_{P,u}(e)\le W_0(e-T_P)^{-r},\qquad
W_0=(\pi^2u_c^2c)^{-1}.}
```

**(F7)**

Every energy interval of length $`\ell`$ consequently carries continuous
contact mass at most $`W_0\ell^\beta/\beta`$. This envelope does not assume
that the real part of the resolvent is separated from $`1/u`$.

### 2.2 Regular-energy derivative bounds, uniform at merging critical values

Take $`0<h\le1`$ and restrict to band energies whose distance from each of
$`T_P,B_{0,P},B_{\pi,P}`$ is at least $`h`$. At every preimage, Hölder continuity
of $`a_P`$ implies distance at least $`(h/2)^{1/z}`$ from either momentum cusp.
Strong concavity on each arc, measured from its smooth maximum, implies

```math
|a_P'(q)|^2\ge2m_z h.
```

For example, integrate the derivative of $`a_P'^2`$ along the arc using (F6).
This estimate remains valid for a shrinking arc: if it has no regular
energies left after removing the collars, it makes no contribution.
The ordinary bounds $`|f^{(j)}(k)|\le L_j\mathrm{dist}(k,2\pi\mathbb{Z})^{z-j}`$
for $`j=2,3`$ therefore give, by differentiating inverse branches,

```math
r_P\le C h^{-1/2},\qquad
|r_P'|\le C h^{-(2/z+1/2)},\qquad
|r_P''|\le C h^{-(4/z+1/2)}.
```

**(F8)**

All constants are independent of $`P`$. There are at most two inverse branches
on the half-circle. In particular their number does not grow when critical
energies approach each other.

For completeness, the real principal-value derivative is also controlled,
not replaced by an absolute integral through its pole. Choose an even cutoff
$`\chi_h(s)`$ which is one for $`|s|\le h/4`$, zero for $`|s|\ge h/2`$, and
linear on the intermediate intervals. Split

```math
\mathrm{Re}m_P(e+i0)
=\int\chi_h(s)\frac{r_P(e+s)-r_P(e)}s\,ds
+\int\frac{1-\chi_h(y-e)}{y-e}r_P(y)\,dy.
```

The derivative of the first term is bounded by
$`h\sup_{|s|\le h/2}|r_P''(e+s)|`$. The derivative of the second kernel is
bounded by $`32h^{-2}`$, and $`\int r_P=1`$. Including the imaginary derivative,

```math
|\partial_e m_P(e+i0)|\le C h^{-(4/z-1/2)}.
```

Since $`\partial_e[m_P/(1-u m_P)]=m_P'/(1-u m_P)^2`$, the lower bound
$`r_P\ge ch^r`$ gives

```math
|\partial_e w_{P,u}(e)|\le C h^{-m},\qquad
m=6/z-5/2 > 0.
```

**(F9)**

This also covers the smooth maximum lying inside the full continuum: it
is included in the excluded critical set, not treated as a regular point.

### 2.3 Fourier decay

Remove radius-$`h`$ collars of the three critical energies from the band.
Their combined contact mass is at most $`3W_0(2h)^\beta/\beta`$ by (F7).
On the complement, integration by parts in energy is valid. There are at
most four intervals, their total length is below four, their boundary
values are bounded by $`W_0h^{-r}`$, and (F9) bounds their derivatives.
Consequently

```math
|b_P(t)|\le C\left(h^\beta+\tau^{-1}h^{-m}\right).
```

Set $`h=\tau^{-1/(m+\beta)}`$. Then
$`\beta/(m+\beta)=(4z-2)/(10-z)`$, proving (F5). This is a uniform
pointwise-in-time estimate, including arbitrarily small nonzero $`P`$ and
arbitrarily small positive detuning. No finite-size spectral recurrence
argument is used.

## 3. One explicit continuum constant

The following positive constants make the preceding proof quantitative.
They are intentionally generous; numerical evaluation of them is not a
measurement of the actual decay amplitude. In addition to $`r,\beta,c,m_z,W_0`$
above, set

```math
\begin{aligned}
L_2&=z(2/\pi)^{z-2},\\
L_3&=z(2/\pi)^{z-3}[(1-z)(2-z)+|3z-2|],\\
s_0&=\sqrt{2m_z},\\
A_2&=2L_2\,2^{(2-z)/z},\qquad
A_3=2L_3\,2^{(3-z)/z},\\
R_1&=\frac{2A_2}{\pi s_0^3},\qquad
R_2=\frac2\pi\left(\frac{A_3}{s_0^4}+\frac{3A_2^2}{s_0^5}\right),\\
C_m&=2^{4/z+1/2}R_2+32+\pi R_1,\\
W_1&=\frac{C_m}{\pi^3u_c^2c^2},\\
\mathcal C_z&=\frac{3\,2^\beta W_0}{\beta}+8W_0+4W_1.
\end{aligned}
```

**(F10)**

Here $`R_1,R_2`$ bound the last two quantities in (F8), $`C_m`$ bounds $`m_P'`$,
and $`W_1`$ bounds the coefficient in (F9). The factor $`2^{4/z+1/2}`$ accounts
for replacing distance $`h`$ by $`h/2`$ inside the Hilbert-transform cutoff.
The bounds on $`L_2,L_3`$ follow directly from the differentiated sine power
and $`\sin(d/2)\ge d/\pi`$, $`0<d\le\pi`$. The eight boundary terms and
length bound four explain the last two terms of $`\mathcal C_z`$.
Thus (F10) supplies a finite constant for every fixed exponent in the open
window. No uniformity is asserted as $`z`$ tends to an endpoint.

## 4. Band regularity and an exact global gap identity

For $`U>U_c`$, the minimum gap below the fixed-momentum continuum is exactly
the magnitude of the negative rest energy:

```math
\boxed{\min_P\{E_{\rm th}(P)-E_d(P;U)\}=-E_d(0;U) > 0.}
```

**(F11)**

To prove this, use uncentered relative momentum:
$`a_P(q)=f(q)+f(P-q)\le2f(q)+f(P)`$ by subadditivity. The normalized rest
bound vector is a trial vector in every fiber, so
$`E_d(P;U)\le E_d(0;U)+E_{\rm th}(P)`$. Equality of the minimum follows
from $`P=0`$. This is a variational statement, not an assumed monotonicity
of the gap or velocity.

Put $`g=-\lambda(0)>0`$, $`L=2^{1+z}+u`$, and

```math
F_1=\|f'\|_1=2^z/\pi,\qquad
F_2^2=\|f'\|_2^2
=\frac{z^2 2^{2z-2}}\pi\mathrm B(z-1/2,3/2).
```

All momentum norms use $`dq/(2\pi)`$. On the bound curve,
$`g\le a_P-\lambda\le L`$ and hence $`\mathcal I_e\ge L^{-2}`$,
where $`\mathcal I(P,e)=\int(a_P-e)^{-1}dq/(2\pi)`$ in dimensionless units.
The useful second derivative identity in the uncentered coordinates is

```math
\mathcal I_{PP}(P,e)
=2\int\frac{dq}{2\pi}
\frac{f'(q)f'(P-q)}{[f(q)+f(P-q)-e]^3}.
```

**(F12)**

For smooth $`f`$ it follows by differentiating and integrating by parts on
the circle. For the actual cusp, approximate $`f`$ by periodic smooth
convolutions. They converge uniformly, their first derivatives converge in
$`L^2`$, and the denominator stays gapped. Cauchy–Schwarz and translation
continuity give uniform convergence of the right side of (F12), including
when its two cusp locations coincide. The first derivatives converge too.
This proves that $`\mathcal I`$, and then the simple pole $`\lambda`$, are
$`C^2`$ in $`P`$; it does not require $`f''`$ to be integrable.

For any valid bound $`v_*\ge\|\lambda'\|_\infty`$, implicit differentiation
and (F12) give

```math
\|\lambda''\|_\infty\le
H:=2L^2g^{-3}(F_2^2+2F_1v_*+v_*^2),
```
```math
\|Z'\|_2\le Z_1:=2L^4g^{-3}(F_1+v_*)/u^2.
```

**(F13)**

Indeed $`|\mathcal I_{Pe}|\le2F_1g^{-3}`$,
$`\mathcal I_{ee}\le2g^{-3}`$, and
$`Z'=-u^{-2}(\mathcal I_{eP}+\mathcal I_{ee}\lambda')/\mathcal I_e^2`$.
A wholly conservative static choice is $`v_*=F_1L^2/g^2`$.
For the joint asymptotics use the sharper established cutoff law
$`v_*=v_{\max}/J=O(\delta^{-1})`$ and $`g\sim a_z^*\rho^z`$.
For $`u`$ in a fixed bounded neighborhood above $`u_c`$, this gives

```math
\|Z'\|_2\le C\rho^{-3z}\delta^{-1},\qquad
\|\lambda''\|_\infty\le C\rho^{-3z}\delta^{-2}.
```

**(F14)**

## 5. A deterministic error bound for the original sharp position event

Let $`W_c=\int Z^2dP/(2\pi)`$, $`v_\delta(P)=\delta\lambda'(P)`$, and define

```math
\begin{aligned}
p(t,s)&=\sum_{|\delta j/\tau| > s} C_j(t),\\
q(s)&=\int\frac{dP}{2\pi}Z(P)^2\mathbf{1}_{\{|v_\delta(P)| > s\}},\\
\mathcal B_\delta(s,a)&=\int\frac{dP}{2\pi}Z(P)^2
 \mathbf{1}_{\{\,||v_\delta(P)|-s|\le2a\,\}},\quad0 < a < s/2.
\end{aligned}
```

The boundary-band mass $`\mathcal B_\delta`$ is an explicit static quantity.
Smoothing will only be used to bound this **sharp event**; it does not
replace the measured observable. Define

```math
\mathcal E_\delta(\tau,a)=
\frac{8\delta}{3\tau a}\sqrt{W_c}\,\|Z'\|_2
+\frac{16\log2}{\pi}\frac{\delta^2}{\tau a^2}
 W_c\|\lambda''\|_\infty,
\quad D=\mathcal B_\delta(s,a)+\mathcal E_\delta(\tau,a).
```

Then, with $`B=\min\{1,\mathcal C_z\tau^{-\gamma_z}\}`$,

```math
\boxed{|p(t,s)-q(s)|\le
D+2\sqrt{q(s)+D}\,B+B^2.}
```

**(F15)**

The bounds (F13) can replace the derivative norms in this formula. Use exact
integrals or validated upper bounds for an actual numerical certificate;
unvalidated quadrature/optimization values alone are not certified inputs.

### Proof of the band part

The pole amplitude is $`A_j^d=\int Z(P)e^{iPj-i\tau\lambda(P)}dP/(2\pi)`$.
Its characteristic function at the scaled coordinate $`\delta j/\tau`$ is

```math
\Phi_\tau(\xi)=\int\frac{dP}{2\pi}Z(P)Z(P+h)
 e^{i\tau[\lambda(P+h)-\lambda(P)]},\qquad h=\xi\delta/\tau.
```

Use translation in $`H^1`$ for $`Z`$ and Taylor's formula for the
$`C^2`$ band. Against $`\Phi_\infty(\xi)=\int Z^2e^{i\xi v_\delta}dP/(2\pi)`$,

```math
|\Phi_\tau-\Phi_\infty|
\le\frac{|\xi|\delta}{\tau}\sqrt{W_c}\|Z'\|_2
+\frac{\xi^2\delta^2}{2\tau}W_c\|\lambda''\|_\infty.
```

**(F16)**

Let $`\varphi`$ be the probability density of the sum of four independent
uniform variables on $`[-1/4,1/4]`$. It is nonnegative, supported on $`[-1,1]`$,
and $`\widehat\varphi(\xi)=\mathrm{sinc}(\xi/4)^4`$ for
$`\mathrm{sinc}(x)=\sin(x)/x`$. The two functions
$`\mathbf{1}_{[-(s-a),s-a]}*\varphi_a`$ and
$`\mathbf{1}_{[-(s+a),s+a]}*\varphi_a`$, with $`\varphi_a(y)=a^{-1}\varphi(y/a)`$,
sandwich $`\mathbf{1}_{[-s,s]}`$. Their discrepancies are confined to the
width-$`2a`$ boundary band. Since the interval transform is bounded by
$`2/|\xi|`$, their Fourier moments are at most

```math
\int\frac{d\xi}{2\pi}|\xi|\,|\widehat f_\pm(\xi)|\le\frac{8}{3a},\qquad
\int\frac{d\xi}{2\pi}\xi^2|\widehat f_\pm(\xi)|
\le\frac{32\log2}{\pi a^2}.
```

The first uses $`\varphi(0)=4/3`$; the second follows from
$`\int_0^\infty\sin^4 x/x^3\,dx=\log2`$, obtained by two integrations by
parts and the cosine-difference integral. Applying (F16) and the sandwiches,
then taking complements (both measures have total mass $`W_c`$), proves
$`|\sum_{|\delta j/\tau|>s}|A_j^d|^2-q(s)|\le D`$.

### Proof of the continuum/interference part

Parseval gives $`\|A-A^d\|_2=\eta(t)\le B`$. On the event in question,
Cauchy–Schwarz gives an error at most $`2\sqrt{p_d}B+B^2`$, where
$`p_d=\sum_{|\delta j/\tau|>s}|A_j^d|^2\le q(s)+D`$. This proves (F15).
Using the global pole norm instead of the event norm would yield a weaker
waiting-time exponent and unnecessarily lose the rare-event scale.
The actual source remains local: the continuum that cancels the initially
nonlocal pole component has not been removed from the preparation.

## 6. From the error bound to the joint limit

Set $`s_\delta=\theta\delta v_{\max}(U)/J\to\theta K_z`$ and choose $`a=\delta`$.
For sufficiently small detuning, $`0<a<s_\delta/2`$. The detuning
proof confines the positive-velocity superlevel sets to a compact interval
of $`k=P/\rho`$, uniformly in small $`\delta`$. Its uniform velocity/residue
limits and the zero-measure level set $`\{|V_z|=\theta K_z\}`$ imply

```math
\mathcal B_\delta(s_\delta,\delta)=o(\delta^{\alpha_z}).
```

**(F17)**

Explicitly, on that compact interval the scaled integrand is bounded and
the indicator of the shrinking boundary band tends to zero at every point
outside the limiting level set. This argument needs no nondegeneracy or
uniqueness of extrema, and claims no power-law rate for (F17).

By (F14),

```math
\mathcal E_\delta(\tau,\delta)
\le C\tau^{-1}\delta^{-3z/(1-z)-2}.
```

Relative to $`\delta^{\alpha_z}`$, this is bounded by
$`C\tau^{-1}\delta^{-L_z^{\rm time}}`$, where
$`L_z^{\rm time}=(5z+1)/(1-z)`$. A direct computation gives

```math
M_z-L_z^{\rm time}
=\frac{-44z^2+53z-6}{4(1-z)(2z-1)} > 0
\quad(1/2 < z < 1).
```

The numerator is concave and positive at both endpoints of $`[1/2,1]`$.
Thus (F2) makes the band error $`o(\delta^{\alpha_z})`$. It also implies

```math
B\,\delta^{-\alpha_z/2}
\le\mathcal C_z(\tau\delta^{M_z})^{-\gamma_z}\longrightarrow0.
```

Since $`q(s_\delta)\sim (J/U_c)^4\mathcal H_z(\theta K_z)\delta^{\alpha_z}`$,
every term in (F15) is $`o(\delta^{\alpha_z})`$. This proves (F3), including
relative control of the continuum interference rather than merely an
absolute error tending to zero.

## 7. Attribution, checks, and scope

The finite-momentum contact scattering framework and detuned pole are
inherited from Sun, Feng, and Zhang, *Efimov effect in long-range quantum
spin chains*, Communications Physics **9**, 146 (2026), published Eqs. (6)–(8).
The rank-one spectral formula is standard (Frymark–Liaw, arXiv:1904.09833,
Section 3.2). Cutting out
critical energies, bounding a principal-value transform, integration by
parts, and Fourier smoothing are established analytical methods, not new
physical mechanisms.

For comparison, Pelinovsky–Stefanov, arXiv:0804.1963, and
Egorova–Kopylova–Teschl, J. Spectr. Theory **5**, 663–696 (2015), study
one-dimensional discrete dispersive estimates for nearest-neighbor
Schrödinger operators with potentials. Their results are precedents for
spectral methods, not estimates invoked for this two-cusp fractional fiber
family. Their quoted decay exponents are not transferred to this model.
The present conservative bound is proved above precisely to control merging
critical energies and vanishing detuning uniformly. No optimal decay or
exhaustive priority claim is made.

Primary sources:
https://www.nature.com/articles/s42005-026-02580-0
https://arxiv.org/abs/1904.09833
https://arxiv.org/abs/0804.1963
https://www.mat.univie.ac.at/~gerald/ftp/articles/dSchrDisp.html

`tools/alternative_time/finite_time.py` evaluates the explicit constants and finite diagnostics;
`tools/alternative_time/check_finite_time.py` tests coarea geometry and the density envelope,
principal-value/complex-resolvent consistency, the gapped derivative identity,
Fourier-sandwich constants and characteristic bounds, exact finite-ring
interference accounting, and the exponent algebra. The code does not simulate
an infinite lattice at times of order $`\delta^{-37}`$ or certify an optimal
waiting time. The finite-time theorem rests on the estimates, not a fitted
relaxation exponent or a finite-ring extrapolation.

The slow sufficient power is a limitation of this proof, not evidence that
nature requires that time. The substantive conclusion is deterministic
relative-error control in a simultaneous time-detuning limit of the original
local measurement. It does not establish efficient transport, a finite-weight
superballistic front, a strict finite-time light cone, a finite laboratory
size, or a realistically accessible observation window.

[Author account](AUTHOR_ACCOUNT.md) · [Proof map](PROOF_MAP.md) · [Reproducibility](../REPRODUCIBILITY.md)
