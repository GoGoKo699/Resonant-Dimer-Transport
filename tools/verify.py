#!/usr/bin/env python3
"""Run unchanged scientific checks and verify the complete repository source."""
from __future__ import annotations
import argparse,hashlib,json,os,re,subprocess,sys,math
from pathlib import Path,PurePosixPath
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[1]
ARCHIVE=ROOT/'archive/review-2026-10-10'
sys.path.insert(0,str(ROOT/'tools'))
import build_reading

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def inventory(root=ROOT):
 result={}
 for p in sorted(root.rglob('*')):
  rel=p.relative_to(root)
  if '.git' in rel.parts or '.venv' in rel.parts:continue
  if p.is_symlink():raise ValueError('Source symlink: '+str(rel))
  if p.is_file():result[rel.as_posix()]=sha(p)
 return result

def member(base,name):
 rel=PurePosixPath(name)
 if rel.is_absolute() or '..' in rel.parts or '\\' in name:raise ValueError('Unsafe manifest path')
 p=base.joinpath(*rel.parts)
 if p.is_symlink() or not p.resolve().is_relative_to(base.resolve()):raise ValueError('Escaping manifest path')
 return p

def static_checks():
 spec=json.loads((ROOT/'maintenance/SOURCE_IMPORT.json').read_text())
 if sha(ARCHIVE/'MANIFEST.json')!=spec['manifest_sha256']:raise ValueError('Changed root source manifest')
 manifest=json.loads((ARCHIVE/'MANIFEST.json').read_text())
 if set(inventory(ARCHIVE))!=set(manifest)|{'MANIFEST.json'}:raise ValueError('Archive membership mismatch')
 checked=[]
 for m in sorted(ARCHIVE.rglob('MANIFEST.json')):
  data=json.loads(m.read_text())
  for name,ref in data.items():
   p=member(m.parent,name)
   if sha(p)!=ref['sha256'] or p.stat().st_size!=ref['bytes']:raise ValueError('Archived bytes changed: '+str(p))
  checked.append({'path':str(m.relative_to(ARCHIVE)),'members':len(data)})
 if len(inventory(ARCHIVE))!=77 or len(checked)!=3:raise ValueError('Source counts changed')
 if sha(ROOT/'LICENSE')!=spec['license_sha256']:raise ValueError('License changed')
 for name,data in build_reading.expected().items():
  if (ROOT/name).read_bytes()!=data:raise ValueError('Generated reading mismatch: '+name)
 links=0
 for p in ROOT.rglob('*.md'):
  if p.is_relative_to(ARCHIVE) or '.git' in p.parts:continue
  for target in re.findall(r'\[[^\]\n]*\]\(([^\s)]+)\)',p.read_text()):
   target=target.split('#',1)[0]
   if not target or re.match(r'^[a-zA-Z][\w+.-]*:',target):continue
   link=(p.parent/target).resolve()
   if not link.is_relative_to(ROOT) or not link.exists():raise ValueError('Broken reading link: '+str(p)+' '+target)
   links+=1
 return {'archive_files':77,'manifests':checked,'generated_pages':4,'local_links':links,'license_unchanged':True}

def differences(a,b,path=''):
 out=[]
 if isinstance(a,dict) and isinstance(b,dict):
  if a.keys()!=b.keys():out.append({'path':path,'kind':'keys','reference':sorted(a),'run':sorted(b)})
  for k in sorted(a.keys()&b.keys()):out.extend(differences(a[k],b[k],path+'/'+str(k)))
 elif isinstance(a,list) and isinstance(b,list):
  if len(a)!=len(b):out.append({'path':path,'kind':'length','reference':len(a),'run':len(b)})
  for i,(x,y) in enumerate(zip(a,b)):out.extend(differences(x,y,path+'/'+str(i)))
 elif type(a)!=type(b) or a!=b:
  item={'path':path,'kind':'value','reference':a,'run':b}
  if type(a)==type(b) and type(a) in (int,float) and math.isfinite(a) and math.isfinite(b):
   item.update(kind='numeric',absolute_difference=abs(a-b))
  out.append(item)
 return out

def git(*args):
 p=subprocess.run(['git','-C',str(ROOT),*args],capture_output=True,text=True)
 return p.stdout.strip() if p.returncode==0 else None

def main():
 ap=argparse.ArgumentParser(description=__doc__)
 ap.add_argument('--output-dir',type=Path,required=True)
 ap.add_argument('--allow-numeric-report-differences',action='store_true')
 args=ap.parse_args();out=args.output_dir.resolve()
 if out.exists() or out==ROOT or ROOT in out.parents:ap.error('Use a new directory outside the repository')
 before=inventory();static=static_checks();out.mkdir(parents=True)
 env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1')
 with (out/'infrastructure.log').open('xb') as log:
  infra=subprocess.run([sys.executable,str(ROOT/'tools/check_repository.py'),'--output',str(out/'infrastructure.json')],
    cwd=ROOT,env=env,stdout=log,stderr=subprocess.STDOUT,timeout=120)
 with (out/'scientific.log').open('xb') as log:
  science=subprocess.run([sys.executable,str(ARCHIVE/'verify.py'),'--output-dir',str(out/'scientific')],
    cwd=ROOT,env=env,stdout=log,stderr=subprocess.STDOUT,timeout=900)
 with (out/'endpoint.log').open('xb') as log:
  endpoint=subprocess.run([sys.executable,str(ROOT/'tools/check_endpoint.py'),'--output',str(out/'endpoint.json')],
    cwd=ROOT,env=env,stdout=log,stderr=subprocess.STDOUT,timeout=120)
 endpoint_path=out/'endpoint.json'
 endpoint_report=json.loads(endpoint_path.read_text()) if endpoint_path.exists() else {}
 endpoint_ok=endpoint.returncode==0 and endpoint_report.get('status')=='PASS' and endpoint_report.get('test_groups')==3
 with (out/'detuning.log').open('xb') as log:
  detuning=subprocess.run([sys.executable,str(ROOT/'tools/check_detuning.py'),'--output',str(out/'detuning.json')],
    cwd=ROOT,env=env,stdout=log,stderr=subprocess.STDOUT,timeout=180)
 detuning_path=out/'detuning.json'
 detuning_report=json.loads(detuning_path.read_text()) if detuning_path.exists() else {}
 detuning_ok=detuning.returncode==0 and detuning_report.get('status')=='PASS' and detuning_report.get('test_groups')==5
 with (out/'finite_time.log').open('xb') as log:
  finite_time=subprocess.run([sys.executable,str(ROOT/'tools/check_finite_time.py'),'--output',str(out/'finite_time.json')],
    cwd=ROOT,env=env,stdout=log,stderr=subprocess.STDOUT,timeout=180)
 finite_time_path=out/'finite_time.json'
 finite_time_report=json.loads(finite_time_path.read_text()) if finite_time_path.exists() else {}
 finite_time_ok=finite_time.returncode==0 and finite_time_report.get('status')=='PASS' and finite_time_report.get('test_groups')==6
 path=out/'scientific/receipt.json';receipt=json.loads(path.read_text()) if path.exists() else {}
 comparisons=[]
 for name,reference,generated in [('review','evidence/final.json','review.json'),('transport','prior/evidence/final3.json','preserved/transport.json'),('pilot','prior/prior/evidence/first.json','preserved/pilot.json')]:
  new=out/'scientific'/generated;ref=ARCHIVE/reference
  diff=differences(json.loads(ref.read_text()),json.loads(new.read_text())) if new.exists() else [{'kind':'missing'}]
  comparisons.append({'suite':name,'reference':reference,'report':generated,'byte_identical':new.exists() and new.read_bytes()==ref.read_bytes(),'differences':diff})
 all_diff=[d for c in comparisons for d in c['differences']]
 identical=all(c['byte_identical'] for c in comparisons)
 numeric=bool(all_diff) and all(d.get('kind')=='numeric' for d in all_diff)
 preserved_assertions=receipt.get('all_assertions_pass') is True and receipt.get('scientific_groups')==15
 assertions=preserved_assertions and endpoint_ok and detuning_ok and finite_time_ok
 unchanged=before==inventory() and receipt.get('source_unchanged') is True
 report_ok=identical or (args.allow_numeric_report_differences and numeric)
 passed=infra.returncode==0 and assertions and unchanged and report_ok
 report={'status':('PASS' if identical else 'PASS_REQUIRES_NUMERIC_REVIEW') if passed else 'FAIL',
  'repository':'GoGoKo699/Resonant-Dimer-Transport','commit':git('rev-parse','HEAD'),'index_tree':git('write-tree'),
  'static_checks':static,'infrastructure_tests':json.loads((out/'infrastructure.json').read_text()).get('tests_run'),
  'infrastructure_returncode':infra.returncode,
  'scientific_groups':receipt.get('scientific_groups',0)+endpoint_report.get('test_groups',0)+detuning_report.get('test_groups',0)+finite_time_report.get('test_groups',0),
  'preserved_scientific_groups':receipt.get('scientific_groups'),'preserved_assertions_pass':preserved_assertions,
  'endpoint_scientific_groups':endpoint_report.get('test_groups'),'endpoint_assertions_pass':endpoint_ok,
  'detuning_scientific_groups':detuning_report.get('test_groups'),'detuning_assertions_pass':detuning_ok,
  'detuning_returncode':detuning.returncode,
  'finite_time_scientific_groups':finite_time_report.get('test_groups'),'finite_time_assertions_pass':finite_time_ok,
  'finite_time_returncode':finite_time.returncode,
  'scientific_assertions_pass':assertions,'original_wrapper_returncode':science.returncode,
  'all_canonical_reports_byte_identical':identical,'report_comparisons':comparisons,
  'numeric_report_review_required':not identical,'allow_numeric_report_differences':args.allow_numeric_report_differences,
  'source_unchanged':unchanged,'source_files':len(before),'source_sha256':before,
  'scope':'Author-side reproducibility, not external peer review or priority clearance.'}
 with (out/'verification.json').open('x') as f:json.dump(report,f,indent=2,sort_keys=True,allow_nan=False);f.write('\n')
 print(json.dumps({k:v for k,v in report.items() if k not in ('source_sha256','report_comparisons')},indent=2))
 raise SystemExit(0 if passed else 1)
if __name__=='__main__':main()
