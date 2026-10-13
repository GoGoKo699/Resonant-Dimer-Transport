#!/usr/bin/env python3
"""Generate the scientific reading route from immutable supplied sources."""
from __future__ import annotations
import argparse, hashlib, json, re
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
ARCHIVE=ROOT/'archive/review-2026-10-10'
PAGES=[
 ('THEOREM.md','research/THEOREM.md','Resonant dimer transport: local observation and preparation size','## 1. Fixed physical task','## 6. Attribution and assessment'),
 ('prior/FOLLOWUP.md','research/TRANSPORT_PROOF.md','Local-source transport proof','## 1. Same model; specified source and detector','## 8. Verification'),
 ('prior/prior/PILOT.md','research/SPECTRAL_PROOF.md','Spectral foundation of the resonant dimer','## 1. A fully specified microscopic model','## 10. What the next bounded calculation must decide'),
 ('REVIEW.md','research/CONTRIBUTION.md','Contribution and attribution','## Review outcome',None),
]
CONTRIBUTION_TEXT="""## Source-resolved resonance contrast

The result connects the exact fractional-lattice contact pole to a specified
local source and same-site detector. At the rest-binding resonance, the
persistent coincidence signal has an algebraic velocity tail; at each fixed
stronger attraction its limiting support is bounded. The calculation retains
both contact overlaps and the unconditional probability per prepared pair.
The scaled relative wavefunction quantifies the source support required for
fixed overlap, while the finite-time proofs control the sharp event at a
deterministic observation time.

## Established ingredients

| Source | Ingredient and relevant model |
|---|---|
| [Sun, Feng, and Zhang](https://www.nature.com/articles/s42005-026-02580-0) · [preprint v1](https://arxiv.org/html/2502.20759v1) | Their finite-momentum contact loop and resonance subtraction supply the continuum pole equation. Homogeneity predicts the pole, residue, and detuning powers. Their microscopic hard-core spin model and auxiliary-field residues require a separate normalization from the onsite contact probability used here. |
| [Albeverio, Lakaev, Makarov, and Muminov](https://arxiv.org/abs/math-ph/0501013) | Theorem 5.4 establishes motion-induced lattice binding under smooth three-dimensional positivity-preserving hypotheses. Section 3 of the spectral foundation gives the explicit one-dimensional fractional-cusp proof. |
| [Ciaurri, Roncal, Stinga, Torrea, and Varona](https://arxiv.org/abs/1608.08913) | The fractional discrete Laplacian, its exact hopping kernel, and long-distance power law are established model ingredients. |
| [Domínguez-Castro](https://www.mdpi.com/2218-2004/11/8/110) | The two-species power-law hopping model with onsite interaction includes a total-momentum scattering equation and disappearance of attractive rest dimers. |
| [Kranzl and collaborators](https://arxiv.org/html/2212.03899v2) | Local neighboring-magnon preparation and nearby-pair position measurements distinguish bound and scattering propagation. Their selected repulsive hard-core branch has finite velocity in a different interaction and exponent regime. |
| [Fukuhara and collaborators](https://arxiv.org/pdf/1305.6598) | Local two-spin preparation and position correlations resolve free and bound motion in the short-range Heisenberg chain. |
| [Frymark and Liaw](https://arxiv.org/pdf/1904.09833) | The Aronszajn–Krein resolvent identity, point-mass weights, and continuous densities provide the rank-one spectral formulas. |

The [author account](AUTHOR_ACCOUNT.md#relationship-to-established-work)
gives the claim-by-claim comparison, including the published supplements,
public author response, and the local-pair dynamics of Macrì and collaborators.
The exact loop specialization is in
[the spectral foundation](SPECTRAL_PROOF.md#9-relationship-to-established-work).

## What the proofs establish

The additional control is microscopic and measurement-specific: lattice
limits for energy, velocity, and normalized contact weight; continuum contact
separation; the velocity pushforward with two overlaps; the global detuning
cutoff and its absolute probability; and the growing relative-support capture
profile. The [finite-time certificate](FINITE_TIME_CERTIFICATE.md) bounds
sharp-event error through static spectral budgets, and
[the joint observation-time theorem](OBSERVATION_TIME.md) proves a sufficient
simultaneous time–detuning regime.

The pole equation, local-pair observation, and motion-induced binding remain
attributed to the sources above. The high-speed coincidence events are rare,
and their internal preparation radius grows with velocity. The resonance
velocity tail takes long time at fixed velocity before high velocity; the
joint theorem states its own simultaneous sufficient regime. Fixed-support
overlap and the sharp-event error bound concern the specified preparation
and detector. The [proof map](PROOF_MAP.md) locates each complete derivation.
"""
REPLACEMENTS={
 'THEOREM.md': [
  ('Both particle numbers are fixed at one. There is no bath, disorder, external force, many-body background, changing interaction, or measurement during evolution. Lattice spacing and $\\hbar$ are one. The kinetic operator is the established fractional discrete Laplacian, not an exact pure power hopping at short distance and not a claim that an identified apparatus implements its full kernel.',
   'Both particle numbers are fixed at one, and the Hamiltonian is time independent and translation invariant. Lattice spacing and $\\hbar$ are one. The kinetic operator is the established fractional discrete Laplacian, with the exact short-distance kernel specified in the [spectral foundation](SPECTRAL_PROOF.md).'),
  ('They concern the infinite lattice followed by long time. They are not assertions of zero finite-time tails or a finite-density transport transition.',
   'They concern the infinite lattice followed by long time, with finite-time accuracy controlled separately in the [finite-time certificate](FINITE_TIME_CERTIFICATE.md).'),
  ('## 2. Spectral inputs and what has been reviewed','## 2. Spectral inputs'),
  ('The preserved pilot supplies complete proofs of the following facts.',
   'The [spectral foundation](SPECTRAL_PROOF.md) supplies complete proofs of the following facts.'),
  ('The pilot proves, including a separate differentiation argument,',
   'The spectral foundation proves, including a separate differentiation argument,'),
  ('The finite curvature was derived through the autocorrelation', 'The finite curvature follows from the autocorrelation'),
  ('The proof review checks why its contact spectral measure here is one atom plus an integrable density, rather than invoking that conclusion for arbitrary rank-one perturbations.',
   'The contact spectral measure has one atom plus an integrable density, as follows from the explicit dispersion and threshold structure.'),
  ('This verifies the specific spectral step used below. It is an author-side proof review, not external independent review.',
   'These dispersion-specific properties establish the spectral decomposition used below.'),
  ('For $z=3/4$, the preserved values are', 'For $z=3/4$, numerical quadrature gives'),
  ('The exponent in (3) is not a second universality mechanism. Whenever', 'Whenever'),
  ('## 4. New corollary: the whole relative wavefunction has a controlled size scaling','## 4. Scaled relative wavefunction and preparation size'),
  ('The preceding notes controlled the root-mean-square size and fixed finite supports. They did not assert a result for support growing with $1/P$. This section derives that result from the same normalized eigenfunction; it introduces no new Hamiltonian or pulse/preparation dynamics.',
   'The normalized eigenfunction determines the optimal overlap for relative support growing with $1/P$.'),
  ('This is a kinematic overlap result, not a protocol for loading the state, not a bound on preparation time, and not a normalized exact-total-momentum state on the infinite center-of-mass lattice. It applies fiberwise and to suitably narrow normalizable momentum wave packets.',
   'This is a kinematic overlap optimum. It applies fiberwise and to suitably narrow normalizable momentum wave packets; its radius quantifies state support rather than preparation dynamics.'),
  ('The new diagnostic reconstructs (4) without importing the previous scalar solver.',
   'An independent quadrature diagnostic reconstructs (4).'),
  ('Equation (1) is also explicit in the continuum amplitude, but this review does not produce a usable uniform rate for $\\eta(t)$. Thus (3) still takes long time at fixed $v$, followed by large $v$. A bound of order $10^{-2}$ on total continuum error would not certify a rare $10^{-8}$ coincidence tail. No assertion of a finite-time high-velocity experimental window, strict finite-time light cone, or advantageous information transfer follows. These are restrictions on the stated interpretation, not requirements to add another model before reviewing the present theorem.',
   'The [joint observation-time theorem](OBSERVATION_TIME.md) proves a uniform momentum-integrated bound $\\eta_U(t)\\le C/(Jt)$ near resonance and combines it with band-norm estimates to give a sufficient simultaneous time–detuning regime. The resonance tail (3) retains its long-time-at-fixed-velocity, then high-velocity order. Relative accuracy for a rare event requires the [event-local error bound](FINITE_TIME_CERTIFICATE.md), which compares continuum amplitude with the square root of its probability.'),
 ],
 'REVIEW.md': [],
 'prior/FOLLOWUP.md': [
  ('## 1. Same model; specified source and detector', '## 1. Model, source, and detector'),
  ('Set \\(U=U_c\\), with the exact value in the preserved pilot.',
   'Set \\(U=U_c\\), with the exact value in [the spectral foundation](SPECTRAL_PROOF.md).'),
  ('There is no spectral filtering, prior projection onto dimers, momentum postselection, or spatially extended preparation. At time t measure both positions.',
   'At time t measure both positions after unitary evolution from this onsite source.'),
  ('The detector can recognize which lattice sites the two distinguishable particles occupy. It is not a proposed implementation of the precise fractional hopping kernel.',
   'The detector resolves the lattice positions of both distinguishable particles.'),
  ('The pilot proves a unique relative-coordinate bound state',
   'The [spectral foundation](SPECTRAL_PROOF.md) proves a unique relative-coordinate bound state'),
  ('These spectral facts are inputs from `prior/PILOT.md`; the statements below about preparation and propagation are additional derivations.',
   'These spectral facts are the inputs to the preparation and propagation derivations below.'),
  ('the pilot gives \\(I_P(E_{th})>1/U_c\\)', 'the spectral foundation gives \\(I_P(E_{th})>1/U_c\\)'),
  ('The pilot gives the unique eigenvalue below it.', 'The spectral foundation gives the unique eigenvalue below it.'),
  ('E\'_d was established separately in the pilot.', 'E\'_d is established separately in the spectral foundation.'),
  ('**Order of limits:** t tends to infinity at fixed v first; then v/J tends to infinity. We have not bounded the relative continuum error uniformly when v grows with t. A fixed-time far-spatial-tail expansion need not have exponent eight. This is not a finite-time arrival guarantee or an optimal signal-discrimination protocol.',
   '**Order of limits:** t tends to infinity at fixed v first; then v/J tends to infinity. The exponent belongs to this limiting velocity measure. The [finite-time certificate](FINITE_TIME_CERTIFICATE.md) and [joint observation-time theorem](OBSERVATION_TIME.md) control the sharp event at deterministic times under their stated conditions.'),
  ('the pilot\'s expansion', 'the spectral expansion'),
  ('At finite times they can coincide; they have not been declared absent from the full wave function.',
   'At finite times they can coincide, and their scattering component remains in the full wavefunction.'),
  ('by the same local/tail splitting as in the pilot.', 'by the local/tail splitting in the spectral foundation.'),
  ('The pilot\'s resolvent Fourier coefficients give', 'The resolvent Fourier coefficients give'),
  ('The source/measurement roles are substantial, not decorative citations.',
   'The contact scattering framework, local-pair measurement, and spectral identities have the following predecessors.'),
  ('the arbitrary-momentum contact T-matrix and its resonance subtraction already supply the continuum pole equation used in the pilot. The present propagation tail is obtained from that branch and its contact residue using standard spectral/Fourier arguments. It is not a newly invented dimer field or effective scattering theory. The current primary published two-magnon section was inspected, including Eqs. (5)--(8). Its discussion evaluates the rest pole and then treats three magnons; absence of a printed local-quench tail is not a priority certificate.',
   'the arbitrary-momentum contact T-matrix and its resonance subtraction supply the continuum pole equation. The propagation law here combines the normalized lattice contact residue with the specified source and detector through spectral/Fourier arguments.'),
  ('The primary preprint\'s preparation discussion and coincidence geometry were read. This is another direct predecessor for the observable, not the fractional threshold asymptotic.',
   'This is a direct predecessor for the local-pair observable.'),
  ('The source comparison uses the readable primary text. A screenshot request for the Kranzl figure failed; no graph coordinate, fit or figure-only parameter was extracted from it. The numerical values in this note are calculations of the stipulated model, not experimental values. This is a targeted comparison, not exhaustive priority clearance or external proof review.',
   'The [author account](AUTHOR_ACCOUNT.md#relationship-to-established-work) compares the models and observables in detail.'),
 ],
 'prior/prior/PILOT.md': [
  ('There is no bath, drive, preparation by acceleration, many-body background, disorder or changing interaction.',
   'The Hamiltonian is time independent and translation invariant.'),
  ('This is **not** the exact pure-power kernel J/|r|^(1+z) at short distances. It is a convenient standard microscopic regularization with the same long-wavelength power. No current apparatus is asserted to implement every coefficient or independently tunable interaction in this model.',
   'The gamma-function kernel fixes the microscopic short-distance hopping; its long-distance power is J/|r|^(1+z) times the stated coefficient.'),
  ('This proof does not turn a finite ring\'s lowest level into an infinite-lattice bound state. It establishes a fiber eigenvalue separated from that fiber\'s continuum. It also does not say that adding center-of-mass momentum dynamically converts an arbitrary scattering preparation into the eigenstate.',
   'This establishes an infinite-lattice relative-coordinate eigenstate separated from the continuum at its conserved total momentum.'),
  ('At e=1 the same argument holds after isolating the two moving cusps and dominating them by |x-1/2|^(-z) and |x+1/2|^(-z).',
   'At the endpoint use the exact lattice energy $E=E_{\\rm th}(P)=\\epsilon_z(P)$, not $E=J|P|^z$. The latter is above the lattice edge, so Eq. (8) cannot be extended by substituting e=1. The [exact-threshold lemma](THRESHOLD_ENDPOINT.md) proves the endpoint expansion with coefficient F_z(1), using uniform cusp domination and the same tail splitting.'),
  ('It is a diverging **spectral group velocity**. No relativistic causality statement, guaranteed fast state transfer, ballistic front, or local-quench probability has been deduced from it.',
   'It is a diverging **spectral group velocity**. Its local-source coincidence weight is derived in [the transport proof](TRANSPORT_PROOF.md).'),
  ('The exact momentum is essential. Momentum-changing disorder or an external operation can provide decay channels not present in this translation-invariant problem. No such operation is added here. Bound wave functions in a long-range hopping model need not decay exponentially.',
   'Total momentum is conserved in this translation-invariant problem. Bound wavefunctions in a long-range hopping model need not decay exponentially.'),
  ('## 9. Strongest predecessor reconstruction', '## 9. Relationship to established work'),
  ('### [SFZ] already supplies the universal pole equation', '### [SFZ] Finite-momentum pole equation'),
  ('### [ALMM] already establishes motion-induced lattice binding', '### [ALMM] Motion-induced lattice binding'),
  ('### [K23] already observes momentum-selective magnon binding', '### [K23] Momentum-selective magnon binding'),
  ('The short fractional proof in Section 3 extends the specific calculation outside those smooth hypotheses; it does not discover that mechanism.',
   'Section 3 supplies the explicit calculation for the fractional cusp outside those smooth hypotheses.'),
  ('We neither reanalyze their data nor refute their specified finite-velocity result. Their spectroscopy provides relevant context, not a demonstrated realization of our model or an unrestricted theorem that all bound pairs have finite velocity.',
   'Their spectroscopy establishes finite velocity for the specified branch and provides context for the resonance contrast in this contact model.'),
  ('It removes any claim that using mobile distinguishable particles or a finite binding threshold is new. [CRSTV] supplies the fractional lattice kinetic operator and exact kernel, so that operator is inherited too.',
   '[CRSTV] supplies the fractional lattice kinetic operator and exact kernel. These model ingredients remain attributed to the respective sources.'),
  ('Thus (7) is an **exact specialization of their effective theory**, not a newly invented scattering equation. The factor 1/2 changes T normalization, not the pole. The existence of a root between 0 and 1, its interpretation as a fractional bound branch, the lattice convergence proof, and the matrix-resolvent controls are the calculations made here. The cited passages evaluate the rest bound pole and use nonzero momenta for the three-body equation; they do not spell out this positive-energy below-continuum branch. That absence does not make consequences of their equation independent conceptual inventions.',
   'Thus (7) is an **exact specialization of their effective theory**. The factor 1/2 changes T normalization, while the pole equation is unchanged. Sections 3–6 establish the root between 0 and 1, its below-fixed-momentum-continuum interpretation, lattice convergence, differentiated velocity, and normalized contact weight.'),
  ('**Contribution under assessment:** a controlled resonance-to-bound-pair dispersion contrast, with the fractional moving pole and its vanishing local spectral weight made explicit in microscopic models. The central sign/residue calculations are short consequences of an existing two-body framework. No claim of a new Efimov effect, first motion-bound dimer, experimental contradiction, or independent invention of the contact effective theory is justified.',
   'The spectral result is a controlled resonance-to-bound-pair dispersion contrast in the exact lattice model, with a fractional moving pole and vanishing local spectral weight. Its scattering framework and motion-induced binding mechanism remain attributed above. The [transport proof](TRANSPORT_PROOF.md) carries the normalized local overlaps into the observed probability law.'),
  ('Read the introduction, Hypotheses 3.1 and 5.1, and Theorem 5.4/proof.',
   'Introduction, Hypotheses 3.1 and 5.1, and Theorem 5.4/proof.'),
  ('Read the published two-magnon section and its arbitrary-momentum T-matrix, compared with preprint v1 and the accessible combined PDF. Source equations are identified by version. No figure or table values are used.',
   'Published two-magnon section and arbitrary-momentum T-matrix; preprint v1 provides the indicated alternative equation numbering.'),
  ('Read Sec. III and Appendix E--F, including the sign of the bound branch, stated velocity behavior and preparation. Figure screenshots were unavailable; no plotted points were digitized or used to infer a numerical parameter not stated in prose.',
   'Section III and Appendices E–F: bound-branch sign, velocity behavior, and preparation.'),
  ('Read the two-body construction, Eqs. (8)--(10), and its zero-momentum analysis. The many-body polaron result is not used here.',
   'Two-body construction, Eqs. (8)–(10), and zero-momentum analysis.'),
  ('Read Theorem 1.1, kernel (1.7), and power-law bounds (1.8).',
   'Theorem 1.1, kernel (1.7), and power-law bounds (1.8).'),
  ('The source comparison is targeted, not exhaustive priority clearance or external proof review. Sources are not redistributed in this package.',
   'Primary sources are linked under their own publication and distribution terms.'),
 ],
}

def sha(data):return hashlib.sha256(data).hexdigest()
def equations(text):
 # Delimiter conversion only; no equation contents are normalized.
 return re.findall(r'\\\[(.*?)\\\]|\$\$(.*?)\$\$',text,re.S)
def expected():
 output={};ledger={'archive':str(ARCHIVE.relative_to(ROOT)),'pages':[]}
 for source,dest,title,start,stop in PAGES:
  raw=(ARCHIVE/source).read_text();selected=raw[raw.index(start):]
  if stop is not None:selected=selected[:selected.index(stop)]
  if source=='prior/prior/PILOT.md':selected+='\n'+raw[raw.index('## Primary sources'):]
  if source=='prior/FOLLOWUP.md':selected=selected[:selected.index('\n**What changed:**')]
  if source=='REVIEW.md':
   selected=selected[:selected.index('\nSuggested working repository name:')]
   begin=selected.index('**GO for a bounded project record')
   end=selected.index('\n\n',begin)
   selected=selected[:begin]+selected[end+2:]
  replacements = [(selected, CONTRIBUTION_TEXT)] if source=='REVIEW.md' else REPLACEMENTS[source]
  transformed=selected
  for old,new in replacements:
   if transformed.count(old)!=1:raise ValueError('Nonunique literal transform: '+old)
   transformed=transformed.replace(old,new,1)
  if equations(selected)!=equations(transformed):raise ValueError('Equation changed')
  transformed=transformed.replace('\\[','$$').replace('\\]','$$').replace('\\(','$').replace('\\)','$')
  footer='\n\n---\n\n[Proof map](PROOF_MAP.md) · [Reproducibility](../REPRODUCIBILITY.md)\n'
  data=('# '+title+'\n\n'+transformed.strip()+footer).encode()
  output[dest]=data
  ledger['pages'].append({'source':source,'destination':dest,'source_sha256':sha(raw.encode()),'start':start,'stop':stop,
   'append_sources':source=='prior/prior/PILOT.md','remove_repository_allocation':source=='REVIEW.md',
   'omit_historical_allocation_tail':source=='prior/FOLLOWUP.md',
   'omit_editorial_planning_sentence':source=='REVIEW.md',
   'presentation_cleanup':'Reader-facing scientific account; source attribution and equation content preserved.',
   'scientific_correction':('research/THRESHOLD_ENDPOINT.md' if source=='prior/prior/PILOT.md' else 'research/OBSERVATION_TIME.md' if source in ('THEOREM.md','prior/FOLLOWUP.md') else None),
   'literal_replacements':replacements,'display_equations':len(equations(selected)),
   'equations_sha256':sha(json.dumps(equations(selected)).encode()),'output_sha256':sha(data),
   'footer_links':['research/PROOF_MAP.md','REPRODUCIBILITY.md'],
   'formatting':'Convert LaTeX math delimiters to GitHub dollar delimiters; preserve equation contents.'})
 output['maintenance/READING_TRANSFORMS.json']=(json.dumps(ledger,indent=2,sort_keys=True)+'\n').encode()
 return output

def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--check',action='store_true');a=ap.parse_args()
 failures=[]
 for name,data in expected().items():
  p=ROOT/name
  if a.check:
   if not p.exists() or p.read_bytes()!=data:failures.append(name)
  else:p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(data)
 if failures:raise SystemExit('Reading mismatch: '+', '.join(failures))
 print(('Checked' if a.check else 'Generated')+' four scientific reading pages and their transform ledger.')
if __name__=='__main__':main()
