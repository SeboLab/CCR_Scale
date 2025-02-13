require(ordinal)
library(rcompanion)
library(pscl)

# Put file path to Study2DataForOrdinalRegression.csv below
data <- read.csv("~/CCR_Scale/CCR_Scale_Study_1-3_Data_Analysis/Study_2/Study2DataForOrdinalRegression.csv")

CCR.ord <- clmm(factor(Ranking) ~ CCR + (1|Subject), data=df)
Gratch.ord <- clmm(factor(Ranking) ~ Gratch + (1|Subject), data=df)

CCR.ord
Gratch.ord

anova(CCR.ord, Gratch.ord)

