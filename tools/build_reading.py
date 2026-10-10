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
 ('REVIEW.md','research/CONTRIBUTION.md','Proof and contribution assessment','## Review outcome',None),
]
REPLACEMENTS={
 'THEOREM.md': [('## 4. New corollary: the whole relative wavefunction has a controlled size scaling','## 4. Scaled relative wavefunction and preparation size')],
 'REVIEW.md': [('It does not provide the missing uniform-in-velocity continuum-convergence rate or an optimal tuning requirement.', 'It is not itself a continuum-decay estimate or an optimal tuning requirement. Deterministic event accuracy and the sufficient joint regime are proved separately in the [finite-time certificate](FINITE_TIME_CERTIFICATE.md) and [observation-time theorem](OBSERVATION_TIME.md).')],'prior/FOLLOWUP.md':[],'prior/prior/PILOT.md':[('At e=1 the same argument holds after isolating the two moving cusps and dominating them by |x-1/2|^(-z) and |x+1/2|^(-z).', 'At the endpoint use the exact lattice energy $E=E_{\\rm th}(P)=\\epsilon_z(P)$, not $E=J|P|^z$. The latter is above the lattice edge, so Eq. (8) cannot be extended by substituting e=1. The [exact-threshold lemma](THRESHOLD_ENDPOINT.md) proves the endpoint expansion with coefficient F_z(1), using uniform cusp domination and the same tail splitting.')],
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
  transformed=selected
  for old,new in REPLACEMENTS[source]:
   if transformed.count(old)!=1:raise ValueError('Nonunique literal transform: '+old)
   transformed=transformed.replace(old,new,1)
  if source=='REVIEW.md':
   # Keep physical significance and source attribution; omit editorial planning.
   begin=transformed.index(' Familiar tools and rare events')
   end=transformed.index('\n\n',begin)
   transformed=transformed[:begin]+(' Familiar methods and rare events do not decide physical significance; the assessment rests on the source-resolved transport conclusion.')+transformed[end:]
  if equations(selected)!=equations(transformed):raise ValueError('Equation changed')
  transformed=transformed.replace('\\[','$$').replace('\\]','$$').replace('\\(','$').replace('\\)','$')
  footer=f'\n\n---\n\n[Proof map](PROOF_MAP.md) · [Reproducibility](../REPRODUCIBILITY.md) · [Preserved source](../archive/review-2026-10-10/{source})\n'
  data=('# '+title+'\n\n'+transformed.strip()+footer).encode()
  output[dest]=data
  ledger['pages'].append({'source':source,'destination':dest,'source_sha256':sha(raw.encode()),'start':start,'stop':stop,
   'append_sources':source=='prior/prior/PILOT.md','remove_repository_allocation':source=='REVIEW.md',
   'omit_historical_allocation_tail':source=='prior/FOLLOWUP.md',
   'omit_editorial_planning_sentence':source=='REVIEW.md',
   'scientific_correction':('research/THRESHOLD_ENDPOINT.md' if source=='prior/prior/PILOT.md' else None),
   'literal_replacements':REPLACEMENTS[source],'display_equations':len(equations(selected)),
   'equations_sha256':sha(json.dumps(equations(selected)).encode()),'output_sha256':sha(data),
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
