

library(data.table)

HL.hyper <- unique(read.csv('mastersproject/data/HL_hypermethylated.csv')$Gene)
HL.hypo <- unique(read.csv('mastersproject/data/HL_hypomethylated.csv')$Gene)

hyper.d <- list()
hypo.d <- list()

for (f in list.files(pattern='*.tsv')) {
    print(f)
    d <- fread(f)
    print(f <- gsub('.tsv','',gsub('.VEP.json_summary.csv','',gsub('coverage_','',gsub('.pass.recode.*','',basename(f))))))
    d <- d[which(is.na(d$gnomadTotalCount_all)),]
    hyper.d[[f]] <- d[which(d$gene %in% HL.hyper),]
    hypo.d[[f]] <- d[which(d$gene %in% HL.hypo),]
}

d$codingEffect[which(d$codingEffect=='')]<-'none'
coding.effects <- unique(d$codingEffect)

samples <- unique(c(names(hyper.d),names(hypo.d)))
X <- data.frame(matrix(0,nrow=length(samples),ncol=length(coding.effects)))
colnames(X) <- coding.effects
rownames(X) <- samples
for (n in names(hyper.d))
{
    print(n)
    hyper.d[[n]]$codingEffect[which(hyper.d[[n]]$codingEffect=='')] <- 'none'
    print(x<-table(hyper.d[[n]]$codingEffect))
    X[n, names(x)] <- as.numeric(x)
}



X2 <- data.frame(matrix(0,nrow=length(samples),ncol=length(coding.effects)))
colnames(X2) <- coding.effects
rownames(X2) <- samples 
for (n in names(hypo.d))
{
    print(n)
    hypo.d[[n]]$codingEffect[which(hypo.d[[n]]$codingEffect=='')] <- 'none'
    print(x<-table(hypo.d[[n]]$codingEffect))
    X2[n, names(x)] <- as.numeric(x)
}


write.csv(X,file='hyperHL_novel.csv')
write.csv(X2,file='hypoHL_novel.csv')

