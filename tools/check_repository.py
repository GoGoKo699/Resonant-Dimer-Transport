#!/usr/bin/env python3
"""Infrastructure checks separate from the fifteen preserved scientific groups."""
from __future__ import annotations
import argparse,hashlib,json,re,sys,tempfile,unittest
from pathlib import Path
sys.dont_write_bytecode=True
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/'tools'))
import verify
class Checks(unittest.TestCase):
 def test_01_source_integrity_and_reading(self):
  r=verify.static_checks();self.assertEqual(r['canonical_reports'],3)
  self.assertEqual(r['research_pages'],15);self.assertGreaterEqual(r['local_links'],25)
 def test_02_owner_license(self):
  b=(ROOT/'LICENSE').read_bytes();self.assertEqual(hashlib.sha1(b'blob '+str(len(b)).encode()+b'\0'+b).hexdigest(),'e17a781bf47c4aadf18b68fc593846a1193b86c1')
 def test_03_proof_format_and_integrity(self):
  records=json.loads((ROOT/'maintenance/SOURCE_INTEGRITY.json').read_text())['files']
  displays=0
  for p in (ROOT/'research').glob('*.md'):
   self.assertIn(str(p.relative_to(ROOT)),records)
   b=p.read_bytes();self.assertEqual(verify.sha(p),records[str(p.relative_to(ROOT))]['sha256'])
   self.assertNotIn(b'\\[',b);self.assertNotIn(b'\\]',b);self.assertNotIn(b'$$',b)
   self.assertEqual(len(re.findall(rb'^```[^\n]*$',b,re.M))%2,0)
   displays+=b.count(b'```math\n')
  self.assertGreater(displays,50)
 def test_04_tampering_and_safe_paths(self):
  with tempfile.TemporaryDirectory() as t:
   p=Path(t);(p/'a').write_text('original');before=verify.inventory(p);(p/'a').write_text('change')
   self.assertNotEqual(before,verify.inventory(p))
   for name in ('../x','/absolute','a/../../x','a\\b'):
    with self.assertRaises(ValueError):verify.member(p,name)
   (p/'link').symlink_to(p/'a')
   with self.assertRaises(ValueError):verify.inventory(p)
 def test_05_report_classification(self):
  self.assertEqual(verify.differences({'x':[1.]},{'x':[1.]}),[])
  self.assertEqual(verify.differences(1.,1.00001)[0]['kind'],'numeric')
  for a,b in ((1,1.),(True,False),('a','b')):self.assertEqual(verify.differences(a,b)[0]['kind'],'value')
  self.assertEqual(verify.differences({'a':1},{'b':1})[0]['kind'],'keys')
 def test_06_read_only_workflow(self):
  text=(ROOT/'.github/workflows/verify.yml').read_text()
  for needed in ('contents: read','persist-credentials: false','github.event.pull_request.head.sha || github.sha','if: always()'):self.assertIn(needed,text)
  for forbidden in ('pull_request_target','contents: write','git push','GITHUB_TOKEN:'):self.assertNotIn(forbidden,text)
  uses=re.findall(r'uses: ([^\s#]+)',text);self.assertEqual(len(uses),3)
  self.assertTrue(all(re.fullmatch(r'actions/[a-z-]+@[a-f0-9]{40}',s) for s in uses))
 def test_07_maintenance_scope_and_contact(self):
  self.assertIn('## Repository scope',(ROOT/'CURRENT.md').read_text())
  for p in ('README.md','llms.txt'):self.assertIn('mailto:gogoko699@gmail.com',(ROOT/p).read_text())
 def test_08_scientific_scope(self):
  s=(ROOT/'README.md').read_text()
  for phrase in ('unconditional','source and detector','fixed velocity','not a loading protocol'):self.assertIn(phrase,s)
  self.assertIn('finite-time rare-event detection guarantee',(ROOT/'CURRENT.md').read_text())
def main():
 ap=argparse.ArgumentParser(description=__doc__);ap.add_argument('--output',type=Path,required=True);args=ap.parse_args();p=args.output.resolve()
 if p.exists() or p==ROOT or ROOT in p.parents:ap.error('Use a new report outside the repository')
 result=unittest.TextTestRunner(verbosity=2).run(unittest.defaultTestLoader.loadTestsFromTestCase(Checks))
 with p.open('x') as f:json.dump({'status':'PASS' if result.wasSuccessful() else 'FAIL','tests_run':result.testsRun,'errors':len(result.errors),'failures':len(result.failures)},f,indent=2,sort_keys=True);f.write('\n')
 raise SystemExit(0 if result.wasSuccessful() else 1)
if __name__=='__main__':main()
