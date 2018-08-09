setwd(basedir)

source("https://bioconductor.org/biocLite.R")
biocLite("minfi")
biocLite("IlluminaHumanMethylation450kmanifest")
biocLite("IlluminaHumanMethylation450kanno.ilmn12.hg19")
biocLite("FlowSorted.Blood.450k")  #package installed into personal library 3.4

library(minfi)
library(IlluminaHumanMethylation450kmanifest)
library(IlluminaHumanMethylation450kanno.ilmn12.hg19)
library(FlowSorted.Blood.450k)

sheet_all <- read.metharray.sheet("rawdata", pattern = "csv$")
RGset_all <- read.metharray.exp(targets = sheet_all)
colnames(RGset_all) <- sheet_all$Sample_Name
pd_all <- pData(RGset_all)

if(require(FlowSorted.Blood.450k)) {
wh.WBC <- which(FlowSorted.Blood.450k$CellType == "WBC")
wh.PBMC <- which(FlowSorted.Blood.450k$CellType == "PBMC")
RGset_all <- FlowSorted.Blood.450k[, c(wh.WBC, wh.PBMC)]
sampleNames(RGset_all) <- paste(RGset$CellType,
c(seq(along = wh.WBC), seq(along = wh.PBMC)), sep = "_")
counts <- estimateCellCounts(RGset_all, compositeCellType = "Blood", cellTypes = c("CD8T", "CD4T", "NK", "Bcell", "Mono", "Gran"), meanPlot = FALSE)
round(counts, 2)
}
