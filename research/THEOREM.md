# Resonant dimer transport: local observation and preparation size

## 1. Fixed physical task

Two distinguishable particles on the infinite lattice have dispersion

$$
\epsilon_z(k)=J[2-2\cos k]^{z/2},\qquad J>0,\quad \frac12<z<1,
$$

and an onsite attraction $-U\delta_{x_a,x_b}$. The Hamiltonian is bounded and self-adjoint. Both particle numbers are fixed at one. There is no bath, disorder, external force, many-body background, changing interaction, or measurement during evolution. Lattice spacing and $\hbar$ are one. The kinetic operator is the established fractional discrete Laplacian, not an exact pure power hopping at short distance and not a claim that an identified apparatus implements its full kernel.

The source is $|0,0\rangle$. After time $t$, both positions are measured. The unconditional same-site distribution is

$$
C_j(t)=|\langle j,j|e^{-itH}|0,0\rangle|^2.
$$

Noncoincident trials remain in the normalization. On this event the center position $X=(x_a+x_b)/2$ is $j$.

The rest-binding threshold is

$$
U_c=2^{1+z}J\sqrt\pi\,
\frac{\Gamma(1-z/2)}{\Gamma((1-z)/2)}.
$$

The primary claims below compare exactly $U=U_c$ with every fixed $U>U_c$, within the same source, detector and hopping model. They concern the infinite lattice followed by long time. They are not assertions of zero finite-time tails or a finite-density transport transition.

## 2. Spectral inputs and what has been reviewed

In a total-momentum fiber, use

$$
h_P=A_P-U|1\rangle\langle1|,\quad
A_P(q)=\epsilon_z(q+P/2)+\epsilon_z(q-P/2),
$$

on $L^2([ -\pi,\pi],dq/(2\pi))$, with the normalized constant source $|1\rangle$. Write

$$
I_P(E)=\int\frac{dq}{2\pi}\frac1{A_P(q)-E}.
$$

The below-continuum eigenvalue solves $I_P(E_d)=1/U$. The preserved pilot supplies complete proofs of the following facts.

At $U=U_c$, there is no normalizable rest bound state, but for every $P\ne0$ there is exactly one bound eigenvalue with

$$
0<E_d(P)<\epsilon_z(P)=E_{\rm th}(P).
$$

The continuum edge follows from subadditivity of the chord dispersion. The pole is bracketed by $I_P(0)<I_0(0)$ and $I_P(E_{\rm th})>I_0(0)$. The rest threshold state behaves as $|q|^{-z}$; its norm diverges since $2z>1$.

Define

$$
b_z(x)=|x+\tfrac12|^z+|x-\tfrac12|^z,
$$
$$
F_z(e)=\int_{\mathbb R}\frac{dx}{2\pi}
\left[\frac1{b_z(x)-e}-\frac1{2|x|^z}\right].
$$

There is a unique $c_z\in(0,1)$ with $F_z(c_z)=0$. The pilot proves, including a separate differentiation argument,

$$
E_d(P)\sim Jc_z|P|^z,\qquad
E_d'(P)\sim Jzc_z\operatorname{sgn}(P)|P|^{z-1},
$$
$$
Z(P)=|\psi_P(0)|^2=\frac1{U_c^2I'_P(E_d(P))}
\sim B_z|P|^{2z-1},\quad
B_z=\frac{J^2}{U_c^2F'_z(c_z)}.
$$

For every fixed $U>U_c$, the rest eigenvalue is negative and

$$
E_d(P)=E_0+C(U)P^2+o(P^2),\qquad E_d'(P)=2C(U)P+o(P).
$$

The finite curvature was derived through the autocorrelation of $e^{-s\epsilon_z(q)}$, whose first derivative lies in $L^2$ for $z>1/2$. A formal second derivative of the cusp would not justify this result. At fixed stronger attraction the below-continuum gap stays positive on the compact momentum circle, and the branch velocity has a finite supremum.

### Contact spectral measure: no hidden continuum atom

The contact resolvent is the standard rank-one formula

$$
\langle1|(h_P-w)^{-1}|1\rangle=\frac{I_P(w)}{1-U I_P(w)}.
$$

The proof review checks why its contact spectral measure here is one atom plus an integrable density, rather than invoking that conclusion for arbitrary rank-one perturbations. For $0<P<\pi$, $A_P$ is analytic on finitely many arcs, with the cusp minimum at $q=P/2$ on the half-circle and smooth extrema at $0,\pi$. It is strictly decreasing before the cusp and increasing afterward. At $P=\pi$, extrema have equal energy but there is no flat interval.

At regular interior energies the pushforward free density is positive, so the contact resolvent is absolutely continuous there. The possible exceptional energies form a finite set. An eigenvector coupled to the source at an energy within the continuum would have to be proportional to $(A_P-E)^{-1}$. It is not square integrable: at a regular preimage there is a squared inverse linear zero; at a smooth extremum an even stronger singularity; and at a lower cusp the square behaves as $|q-q_0|^{-2z}$ with $2z>1$. An eigenvector uncoupled from the source would be an eigenvector of multiplication by $A_P$, which has no positive-measure level set. Thus the exceptional set carries no contact atoms. It also cannot support a singular continuous measure because it is finite. Above the band an attractive rank-one perturbation has no eigenvalue.

This verifies the specific spectral step used below. It is an author-side proof review, not external independent review.

## 3. What a local source and contact detector actually see

The contact amplitude is the total-momentum Fourier coefficient of

$$
c_P(t)=Z(P)e^{-itE_d(P)}+b_P(t),\qquad
b_P(t)=\int e^{-itE}w_P(E)\,dE,
$$

where

$$
w_P(E)=\frac{\rho_{0,P}(E)}{|1-U I_P(E+i0)|^2}.
$$

The continuum density has mass $1-Z(P)$, so $b_P(t)\to0$ by Riemann--Lebesgue and $|b_P(t)|\le1$. Define

$$
A_j^d(t)=\int\frac{dP}{2\pi}Z(P)e^{iPj-itE_d(P)},\qquad
\eta(t)^2=\int\frac{dP}{2\pi}|b_P(t)|^2.
$$

Dominated convergence gives $\eta(t)\to0$. Parseval and Cauchy--Schwarz give the exact finite-time bound

$$
\sum_j\big|C_j(t)-|A_j^d(t)|^2\big|
\le 2\sqrt{W_c}\,\eta(t)+\eta(t)^2,\qquad
W_c=\int\frac{dP}{2\pi}Z(P)^2. \tag{1}
$$

This controls the whole unnormalized coincidence measure. It does not remove the scattering state from the full wavefunction. The pole component alone is already spatially extended at $t=0$; the continuum cancels it to produce the actual local initial state.

For every bounded continuous $f$,

$$
\lim_{t\to\infty}\sum_j f(j/t)C_j(t)
=\int\frac{dP}{2\pi}Z(P)^2 f(E_d'(P)). \tag{2}
$$

To prove (2), take the characteristic function of $|A_j^d|^2$. A momentum shift $\xi/t$ gives a phase $t[E_d(P+\xi/t)-E_d(P)]\to\xi E_d'(P)$ almost everywhere. Translation continuity of $Z$ in $L^2$, boundedness of the phase, and the continuity theorem for characteristic functions give the weak limit. Equation (1) transfers it to the actual preparation. There is no need for stationary phase at a cusp.

In particular,

$$
\lim_{t\to\infty}\sum_jC_j(t)=W_c,
$$

whereas the conserved bound-sector population is $W_b=\int Z(P)dP/(2\pi)$. The second overlap at the detector is essential: $W_c<W_b$.

At continuity points $v>0$, let $Q(v)$ be the long-time probability of a coincidence outside $|X|\le vt$. Then

$$
Q(v)=\int_{|E_d'(P)|>v}\frac{dP}{2\pi}Z(P)^2,
$$
$$
Q(v)\sim\frac{B_z^2}{\pi(4z-1)}
\left(\frac{zc_zJ}{v}\right)^{(4z-1)/(1-z)}. \tag{3}
$$

For $z=3/4$, the preserved values are $c_z=0.6340774020\ldots$, $B_z=0.6816851254\ldots$,

$$
Q(v)\sim1.9347109013\times10^{-4}(J/v)^8.
$$

At fixed $U>U_c$, (2) instead has bounded velocity support. For $U=0$, $W_c=0$. At resonance, (2) is nevertheless tight: for any $L(t)/t\to\infty$, the coincidence probability outside $L(t)$ tends to zero. This excludes an interpretation as a nonvanishing superballistic fraction. It does not justify passing to exact unbounded spatial moments.

### Generic exponent accounting

The exponent in (3) is not a second universality mechanism. Whenever a local overlap probability scales as $Z(P)\sim B|P|^\eta$ and a band velocity as $v(P)\sim a|P|^{-\kappa}$, the same source/contact detector has a tail exponent $(2\eta+1)/\kappa$. In this problem $\eta=2z-1$ and $\kappa=1-z$. Changing the detector to a spectral projection would remove one overlap factor and describe a different observable.

## 4. Scaled relative wavefunction and preparation size

The preceding notes controlled the root-mean-square size and fixed finite supports. They did not assert a result for support growing with $1/P$. This section derives that result from the same normalized eigenfunction; it introduces no new Hamiltonian or pulse/preparation dynamics.

Choose $P>0$ and the normalized positive momentum wavefunction

$$
\psi_P(q)=\frac1{\sqrt{I'_P(E_d(P))}[A_P(q)-E_d(P)]}.
$$

Set

$$
h_P(x)=\sqrt P\,\psi_P(Px)\,\mathbf1_{|x|\le\pi/P},\qquad
h_z(x)=\frac1{\sqrt{F'_z(c_z)}[b_z(x)-c_z]}.
$$

Both have norm one with measure $dx/(2\pi)$, and

$$
\boxed{h_P\longrightarrow h_z\quad\text{in }L^2(\mathbb R,dx/(2\pi)).} \tag{4}
$$

**Proof.** On bounded $x$ intervals, the already established energy and normalization asymptotics give pointwise convergence. The scaled denominator has a uniform positive gap on bounded intervals because $c_z<1$. Outside a sufficiently large fixed interval, chord bounds on the Brillouin zone give $|h_P(x)|\le C_z(1+|x|)^{-z}$, uniformly for small $P$. Squaring produces an integrable envelope because $2z>1$. Dominated convergence proves (4), including the tail beyond the expanding lattice cutoff. This is stronger than agreement of a few moments and uses no continuum wavefunction sampled as a substitute for the lattice proof.

Let $\phi_z(y)=\int e^{ixy}h_z(x)dx/(2\pi)$, understood initially in $L^2$. Thus $\int|\phi_z|^2dy=1$. Define the step embedding of the actual lattice wavefunction by

$$
s_P(y)=P^{-1/2}\psi_P(r),\quad
P(r-\tfrac12)\le y<P(r+\tfrac12).
$$

Then $s_P\to\phi_z$ in $L^2(\mathbb R,dy)$. To check that lattice sampling has not been silently replaced by interpolation, the inverse Fourier transform of $h_P$ is the normalized band-limited interpolation. Its inner product with $s_P$ is exactly

$$
\int_{-\pi}^{\pi}\frac{dq}{2\pi}|\psi_P(q)|^2\,\operatorname{sinc}(q/2),
\qquad\operatorname{sinc}u=\frac{\sin u}{u}.
$$

The momentum measure concentrates at $q=0$, by (4), so this inner product tends to one. Both norms are one. Fourier isometry proves the step limit. In particular their squared densities converge in $L^1$.

### Exact optimal relative-support overlap

For a normalized relative source supported on $|r|\le R$, the largest possible squared overlap with the bound eigenstate is

$$
M_R(P)=\sum_{|r|\le R}|\psi_P(r)|^2.
$$

This follows from orthogonal projection, with equality for the normalized restricted eigenfunction. For any integer radius sequence with $PR(P)\to a\in[0,\infty]$,

$$
\boxed{M_{R(P)}(P)\longrightarrow\mathcal M_z(a)
:=\int_{-a}^{a}|\phi_z(y)|^2dy.} \tag{5}
$$

Here $\mathcal M_z(0)=0$ and $\mathcal M_z(\infty)=1$. Therefore any fixed target overlap $0<q<1$ requires relative source radius of order $1/P$, and a sufficiently large constant times $1/P$ suffices. More explicitly, $PR\to0$ forces the best overlap to zero; $PR\to\infty$ makes the best overlap tend to one. This is a kinematic overlap result, not a protocol for loading the state, not a bound on preparation time, and not a normalized exact-total-momentum state on the infinite center-of-mass lattice. It applies fiberwise and to suitably narrow normalizable momentum wave packets.

Combining with the branch velocity gives the size scale at large $v$:

$$
R=\Theta\!\left((v/J)^{1/(1-z)}\right) \tag{6}
$$

for fixed capture fraction, with constants depending on that fraction and $z$. At $z=3/4$ this is $R=\Theta((v/J)^4)$. A fixed microscopic source does not meet this scaling; it instead gives the rare tail (3). A large center-of-mass envelope alone does not remove the internal relative-support requirement.

### Small scaled windows

The large-$|x|$ behavior is

$$
h_z(x)=\frac{|x|^{-z}}{2\sqrt{F'_z(c_z)}}+O(|x|^{-2z}).
$$

After subtracting the first term globally, the difference is in $L^1$: $z<1$ controls its origin and $2z>1$ its tail. The Fourier transform of $|x|^{-z}$ therefore gives

$$
\phi_z(y)=D_z|y|^{z-1}+O(1),\qquad
D_z=\frac{\Gamma(1-z)\sin(\pi z/2)}{2\pi\sqrt{F'_z(c_z)}}.
$$

Consequently,

$$
\mathcal M_z(a)\sim\frac{2D_z^2}{2z-1}a^{2z-1}\quad(a\downarrow0). \tag{7}
$$

For $z=3/4$, the coefficient is $0.9986189214\ldots$. This means first take the wavefunction scaling limit, then small scaled support. It does not substitute that continuum coefficient for the already known fixed-$R$ microscopic coefficient. The two match when the fixed-radius coefficient is subsequently expanded for large $R$.

The new diagnostic reconstructs (4) without importing the previous scalar solver. Its overlap with $h_z$ is $0.98127253$, $0.99087532$, and $0.99548046$ at $P=0.2,0.05,0.0125$, respectively, for $z=3/4$. These are quadratures, not rigorous finite-$P$ intervals or the proof of (4).

## 5. Resonance tuning and time remain distinct from the asymptotic theorem

The change $U\mapsto U+\Delta U$ adds $-\Delta U\Pi_c$, where the contact projection has operator norm one. Duhamel therefore gives, for every normalized preparation and any fixed-time position event,

$$
|p_{U+\Delta U}(t)-p_U(t)|\le\min\{1,t|\Delta U|\}. \tag{8}
$$

This is an explicit sufficient stability certificate, not an optimal or necessary tuning law. It establishes finite-time continuity despite the change of asymptotic velocity support at exactly $U_c$.

Equation (1) is also explicit in the continuum amplitude, but this review does not produce a usable uniform rate for $\eta(t)$. Thus (3) still takes long time at fixed $v$, followed by large $v$. A bound of order $10^{-2}$ on total continuum error would not certify a rare $10^{-8}$ coincidence tail. No assertion of a finite-time high-velocity experimental window, strict finite-time light cone, or advantageous information transfer follows. These are restrictions on the stated interpretation, not requirements to add another model before reviewing the present theorem.

---

[Proof map](PROOF_MAP.md) · [Reproducibility](../REPRODUCIBILITY.md) · [Preserved source](../archive/review-2026-10-10/THEOREM.md)
