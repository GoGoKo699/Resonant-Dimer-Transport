#!/usr/bin/env python3
"""Reproduce the five transport and five preserved spectral checks.

The new output directory must be outside this package. Source integrity,
scientific assertions, and canonical report identity are separate receipt fields.
No original report, assertion, or source is changed.
"""
from __future__ import annotations
import argparse,hashlib,json,os,subprocess,sys
from pathlib import Path
ROOT=Path(__file__).resolve().parent

def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def inventory():return {str(p.relative_to(ROOT)):sha(p) for p in sorted(ROOT.rglob('*')) if p.is_file()}

def main():
    p=argparse.ArgumentParser(description=__doc__);p.add_argument('--output-dir',type=Path,required=True);a=p.parse_args()
    out=a.output_dir.resolve()
    if out.exists() or out==ROOT or ROOT in out.parents:p.error('Use a new directory outside the package')
    manifest=json.loads((ROOT/'prior/MANIFEST.json').read_text())
    for name,record in manifest.items():
        f=(ROOT/'prior'/name).resolve()
        if not f.is_relative_to(ROOT/'prior') or f.is_symlink():raise ValueError('Unsafe manifest member')
        if sha(f)!=record['sha256'] or f.stat().st_size!=record['bytes']:raise ValueError('Changed source: '+name)
    before=inventory();out.mkdir(parents=True)
    env=dict(os.environ,OPENBLAS_NUM_THREADS='1',OMP_NUM_THREADS='1',PYTHONDONTWRITEBYTECODE='1')
    runs=[]
    for name,script,ref in [('transport','check_transport.py','evidence/final3.json'),('pilot','prior/check_pilot.py','prior/evidence/first.json')]:
        report=out/(name+'.json')
        with (out/(name+'.log')).open('xb') as f:
            proc=subprocess.run([sys.executable,str(ROOT/script),'--output',str(report)],stdout=f,stderr=subprocess.STDOUT,
                                env=env,cwd=ROOT,timeout=300)
        data=json.loads(report.read_text()) if report.exists() else {}
        runs.append({'name':name,'returncode':proc.returncode,'status':data.get('status'),'groups':data.get('test_groups',0),
                     'canonical_byte_match':report.exists() and report.read_bytes()==(ROOT/ref).read_bytes(),'reference':ref})
    receipt={'runs':runs,'all_assertions_pass':all(r['returncode']==0 and r['status']=='PASS' for r in runs),
             'all_canonical_bytes_match':all(r['canonical_byte_match'] for r in runs),'source_unchanged':inventory()==before,
             'scientific_groups':sum(r['groups'] for r in runs),'source_sha256':before}
    with (out/'receipt.json').open('x') as f:json.dump(receipt,f,indent=2,sort_keys=True);f.write('\n')
    print(json.dumps({k:v for k,v in receipt.items() if k!='source_sha256'},indent=2))
    raise SystemExit(0 if receipt['all_assertions_pass'] and receipt['all_canonical_bytes_match'] and receipt['source_unchanged'] else 1)
if __name__=='__main__':main()
