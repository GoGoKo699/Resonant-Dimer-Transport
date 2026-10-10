#!/usr/bin/env python3
"""Run the five review and ten preserved moving-dimer checks.

Use a new output directory outside the package. No canonical report or source is
overwritten. A scientific assertion pass and exact report identity are distinct.
"""
from __future__ import annotations
import argparse,hashlib,json,os,subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def inventory():return {str(p.relative_to(ROOT)):sha(p) for p in sorted(ROOT.rglob('*')) if p.is_file()}

def main():
    ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output-dir',type=Path,required=True)
    args=ap.parse_args();out=args.output_dir.resolve()
    if out.exists() or out==ROOT or ROOT in out.parents:ap.error('Use a new output directory outside this package')
    original=json.loads((ROOT/'INPUT_HASHES.json').read_text())
    for name,digest in original.items():
        p=(ROOT/'prior'/name).resolve()
        if not p.is_relative_to(ROOT/'prior') or p.is_symlink() or sha(p)!=digest:raise ValueError('Changed incoming file: '+name)
    manifests=[]
    for m in sorted((ROOT/'prior').rglob('MANIFEST.json')):
        data=json.loads(m.read_text())
        for name,record in data.items():
            f=(m.parent/name).resolve()
            if not f.is_relative_to(ROOT/'prior') or f.is_symlink():raise ValueError('Unsafe manifest member')
            if sha(f)!=record['sha256'] or f.stat().st_size!=record['bytes']:raise ValueError('Changed archived member: '+name)
        manifests.append({'path':str(m.relative_to(ROOT)),'members':len(data)})
    before=inventory();out.mkdir(parents=True)
    env=dict(os.environ,PYTHONDONTWRITEBYTECODE='1',OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1')
    with (out/'review.log').open('xb') as log:
        new=subprocess.run([sys.executable,str(ROOT/'check_review.py'),'--output',str(out/'review.json')],
            cwd=ROOT,env=env,stdout=log,stderr=subprocess.STDOUT,timeout=120)
    with (out/'prior_wrapper.log').open('xb') as log:
        old=subprocess.run([sys.executable,str(ROOT/'prior/verify.py'),'--output-dir',str(out/'preserved')],
            cwd=ROOT,env=env,stdout=log,stderr=subprocess.STDOUT,timeout=600)
    review=json.loads((out/'review.json').read_text()) if (out/'review.json').exists() else {}
    oldpath=out/'preserved/receipt.json';prior=json.loads(oldpath.read_text()) if oldpath.exists() else {}
    match=(out/'review.json').exists() and (out/'review.json').read_bytes()==(ROOT/'evidence/final.json').read_bytes()
    assertions=new.returncode==0 and review.get('status')=='PASS' and prior.get('all_assertions_pass') is True
    identities=match and prior.get('all_canonical_bytes_match') is True
    source_same=before==inventory() and prior.get('source_unchanged') is True
    receipt={'all_assertions_pass':assertions,'all_canonical_reports_byte_identical':identities,'source_unchanged':source_same,
        'scientific_groups':review.get('test_groups',0)+prior.get('scientific_groups',0),'review_returncode':new.returncode,
        'prior_wrapper_returncode':old.returncode,'review_report_matches':match,'prior_runs':prior.get('runs',[]),
        'source_sha256':before,'preserved_files':len(original),'preserved_manifests':manifests}
    with (out/'receipt.json').open('x') as f:json.dump(receipt,f,indent=2,sort_keys=True);f.write('\n')
    print(json.dumps({k:v for k,v in receipt.items() if k!='source_sha256'},indent=2))
    raise SystemExit(0 if assertions and identities and source_same else 1)
if __name__=='__main__':main()
