"""Read printed coherence evidence; this does not retrain models. Python 3.9+."""
import argparse,json,re
from pathlib import Path
def audit(path):
 nb=json.loads(Path(path).read_text());scores={}
 for c in nb['cells']:
  for o in c.get('outputs',[]):
   t=o.get('text','');t=''.join(t) if isinstance(t,list) else t
   for name,value in re.findall(r'(lda|lsa|hdp) model Coherence Score:\s*([0-9.]+)',t,re.I):scores[name.upper()]=float(value)
 assert set(scores)=={'LDA','LSA','HDP'}
 source='\n'.join(''.join(c.get('source',[])) for c in nb['cells'] if c['cell_type']=='code')
 return dict(mode='saved_output_audit_not_retraining',coherence_c_v=scores,unseeded_sample_present='df.sample(8000)' in source,dataset_bundled=Path('medium_post_titles.csv').exists())
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--notebook',default='Topic Modelling_Medium Articles.ipynb');print(json.dumps(audit(p.parse_args().notebook),indent=2))
