library(data.table)

HL.hyper <- unique(read.csv('mastersproject/data/HL_hypermethylated.csv')$Gene)
HL.hypo <- unique(read.csv('mastersproject/data/HL_hypomethylated.csv')$Gene)


for (f in list.files(pattern='*.recode.tsv')) {
    print(f)
    d <- fread(f)
    d <- d[which(is.na(d$gnomadTotalCount_all)),]

    hyper.d <- d[which(d$gene %in% HL.hyper),]
    hypo.d <- d[which(d$gene %in% HL.hypo),]


    break
}


