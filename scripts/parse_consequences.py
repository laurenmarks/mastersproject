import sys
import re
import pandas as pd


s=sys.stdin.read()

#var consequences_table = drawTable('consequences_table', 'Consequences (all)', google.visualization.arrayToDataTable([['Consequence type','Count'],['splice_donor_variant',187],['splice_acceptor_variant',140],['stop_gained',79],['frameshift_variant',255],['stop_lost',23],['start_lost',27],['inframe_insertion',187],['inframe_deletion',202],['protein_altering_variant',2],['missense_variant',11667],['splice_region_variant',4423],['incomplete_terminal_codon_variant',1],['stop_retained_variant',12],['start_retained_variant',1],['synonymous_variant',13522],['coding_sequence_variant',21],['mature_miRNA_variant',153],['5_prime_UTR_variant',8235],['3_prime_UTR_variant',38452],['non_coding_transcript_exon_variant',45191],['intron_variant',2643203],['NMD_transcript_variant',32723],['non_coding_transcript_variant',654656],['upstream_gene_variant',512007],['downstream_gene_variant',513957],['TFBS_ablation',4],['TF_binding_site_variant',13133],['regulatory_region_variant',352939],['intergenic_variant',1920979]]));

g=re.compile('var consequences_table = .*google.visualization.arrayToDataTable\((\[.*\])\).*;').search(s).group(1)

l=eval(g)

h1, h2,=l[0]

d={h1:[],h2:[]}

for x in l[1:]:
	d[h1]+=[x[0]]
	d[h2]+=[x[1]]

df = pd.DataFrame(data=d)
print(df.to_csv(index=False))
