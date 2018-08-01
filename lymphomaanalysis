#read in lists of lymphoma cpgs linked to hyper and hypo methylated genes
hlgenes_hyper <- read.csv("hlgeneshyper.csv")
head(hlgenes_hyper)
hlcpgs_hyper <- hlgenes_hyper$CpG.site
dim(hlgenes_hyper)
length(hlcpgs_hyper)

hlgenes_hypo <- read.csv("hlgeneshypo.csv")
head(hlgenes_hypo)
hlcpgs_hypo <- hlgenes_hypo$CpG.site
dim(hlgenes_hypo)
length(hlcpgs_hypo)

hlhyper_betas_pgp <- beta_raw_all[rownames(beta_raw_all) %in%  hlcpgs_hyper, ]
hlhypo_betas_pgp <- beta_raw_all[rownames(beta_raw_all) %in%  hlcpgs_hypo, ]

#create a heatmap
heatmap.2(hlhyper_betas_pgp)
heatmap.2(hlhypo_betas_pgp)
heatmap.2(hlhyper_betas_pgp, margins =c(8,8), labRow=FALSE) #turns off cpg labels
heatmap.2(hlhyper_betas_pgp, margins =c(8,8), labRow=FALSE, dendrogram="column") #also turns off cpg dendrogram
heatmap.2(hlhyper_betas_pgp, margins =c(8,8), labRow=FALSE, dendrogram="column", trace="none") #also turns off trace lines

my_palette <- colorRampPalette(c("green", "yellow", "red"))
jpeg(file = "results/heatmap2.jpeg")
heatmap.2(hlhyper_betas_pgp, col=my_palette, margins =c(8,2),  labRow=FALSE, dendrogram="column", trace="none", key=TRUE, keysize = 0.9, density.info = "none")
dev.off()

col_breaks = c(seq(0,0.39,length=100), seq(0.4,0.59,length=100),seq(0.6,1,length=100))
jpeg(file = "results/hypoheatmap2.jpeg")
heatmap.2(hlhypo_betas_pgp, col=my_palette, breaks=col_breaks, margins =c(8,2),  labRow=FALSE, dendrogram="column", trace="none", key=TRUE, keysize = 0.9, density.info = "none")
dev.off()
