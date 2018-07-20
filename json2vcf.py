from __future__ import print_function
import sys
import json

print('##fileformat=VCFv4.1')
headers=['#CHROM','POS','ID','REF','ALT','QUAL','FILTER','INFO','FORMAT','GENO']
print('\t'.join(headers),'most_severe_consequence','kaviar_af','gene_symbol','JSON',sep='\t')

for l in sys.stdin:
    l=l.strip()
    d=json.loads(l)
    input=d['input'].split('\t')
    input=dict(zip(headers,input))
    input['ID']=d['id']
    del d['input']
    d['gene_symbol']=','.join([str(t['gene_symbol']) for t in d.get('transcript_consequences',[]) if d['most_severe_consequence'] in t['consequence_terms']])
    d['kaviar_af']=d.get('custom_annotations',{}).get('kaviar',[{'fields':{'AF':0}}])[0]['fields']['AF']
    print('\t'.join([input[h] for h in headers]),d['most_severe_consequence'],d['kaviar_af'],d['gene_symbol'],json.dumps(d),sep='\t')
