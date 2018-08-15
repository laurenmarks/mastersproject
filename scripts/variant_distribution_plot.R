library(ggplot2)
library(ggridges)


df <- data.frame()
for (f in list.files(path='coverage/',pattern='coverage.*.csv',full.names=TRUE)) {
print(f)
d <- read(f)
d$group <- gsub('.VEP.json_summary.csv','',gsub('coverage_','',gsub('.pass.recode.*','',basename(f))))
df <- rbind(df,d)
}

colnames(df) <- c('count','Position','sample')

ggplot(df, aes(x = Position, y = as.numeric(as.factor(df$sample)), height=count, group = sample)) + geom_density_ridges(stat = "identity", scale = 1, fill='lightblue') + labs(x = "Position (Mb)") + labs(y = "") +  scale_y_continuous(breaks=(1:length(unique(df$sample))), labels=unique(df$sample)) + theme(axis.ticks.y=element_blank())
