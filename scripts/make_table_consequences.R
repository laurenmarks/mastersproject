#consequences <- c("3_prime_UTR_variant", "5_prime_UTR_variant", "coding_sequence_variant", "downstream_gene_variant", "frameshift_variant", "incomplete_terminal_codon_variant", "inframe_deletion", "inframe_insertion", "intergenic_variant", "intron_variant", "mature_miRNA_variant", "missense_variant", "NMD_transcript_variant", "non_coding_transcript_exon_variant", "non_coding_transcript_variant", "protein_altering_variant", "regulatory_region_variant", "splice_acceptor_variant", "splice_donor_variant", "splice_region_variant", "start_lost", "start_retained_variant", "stop_gained", "stop_lost", "stop_retained_variant", "synonymous_variant", "TF_binding_site_variant", "TFBS_ablation", "transcript_ablation", "upstream_gene_variant")
consequences <- c("3_prime_UTR_variant", "5_prime_UTR_variant", "coding_sequence_variant", "downstream_gene_variant", "frameshift_variant", "incomplete_terminal_codon_variant", "inframe_deletion", "inframe_insertion", "intergenic_variant", "intron_variant", "mature_miRNA_variant", "missense_variant", "NMD_transcript_variant", "non_coding_transcript_exon_variant", "non_coding_transcript_variant", "protein_altering_variant", "regulatory_region_variant", "splice_acceptor_variant", "splice_donor_variant", "splice_region_variant", "start_lost", "start_retained_variant", "stop_gained", "stop_lost", "stop_retained_variant", "synonymous_variant", "TF_binding_site_variant", "TFBS_ablation", "transcript_ablation", "upstream_gene_variant", "TFBS_amplification")

X <- do.call('cbind',
lapply(list.files(path='consequences/',pattern='*.csv',full.names=TRUE), function(f) {
print(f)
d <- read(f)
colnames(d) <- c('ConsequenceType',gsub('.VEP.json_summary.csv','',gsub('consequence_','',gsub('.pass.recode.*','',basename(f)))))
print(dput(d$ConsequenceType))
rownames(d) <- d$ConsequenceType
d <- d[order(rownames(d)),]
i <- setdiff(consequences,rownames(d))
if (length(i)>0) {
d[i,'ConsequenceType'] <- 0
}
print(dim(d))
print(dput(rownames(d)))
d <- d[order(rownames(d)),]
#d <- d[,-1]
return(d)
}))

X <- X[,-which( colnames(X) == 'ConsequenceType')]

X[is.na(X)] <- 0

X <- apply(X,2,function(x) { round(100*x/sum(x),5) } )



write.csv(X,file='all_consequences.csv')
