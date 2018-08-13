from __future__ import print_function
import sys
import json

print('##fileformat=VCFv4.1')
headers=['#CHROM','POS','ID','REF','ALT','QUAL','FILTER','INFO','FORMAT','GENO']
out_headers=['#CHROM','POS','ID','REF','ALT','GENO']
print('\t'.join(headers),'most_severe_consequence','kaviar_af','gnomad_genomes_af','gene_symbol','hgvsc','hgvsp',sep='\t')

for l in sys.stdin:
    l=l.strip()
    d=json.loads(l)
    input=d['input'].split('\t')
    input=dict(zip(headers,input))
    input['ID']=d['id']
    input['GENO']=input['GENO'].split(':')[0]
    del d['input']
    d['gene_symbol']=','.join([str(t['gene_symbol']) for t in d.get('transcript_consequences',[]) if d['most_severe_consequence'] in t['consequence_terms']])
    d['hgvsc']=','.join([str(t.get('hgvsc','')) for t in d.get('transcript_consequences',[]) if d['most_severe_consequence'] in t['consequence_terms']])
    d['hgvsp']=','.join([str(t.get('hgvsp','')) for t in d.get('transcript_consequences',[]) if d['most_severe_consequence'] in t['consequence_terms']])
    d['kaviar_af']=d.get('custom_annotations',{}).get('kaviar',[{'fields':{'AF':0}}])[0]['fields']['AF']
    d['gnomad_genomes_af']=d.get('custom_annotations',{}).get('gnomad_genomes',[{'fields':{'AF_raw':0}}])[0]['fields']['AF_raw']
    print('\t'.join([input[h] for h in out_headers]),d['most_severe_consequence'],d['kaviar_af'],d['gnomad_genomes_af'],d['gene_symbol'],d['hgvsc'],d['hgvsp'],sep='\t')
