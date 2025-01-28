require(ordinal)
library(rcompanion)
library(pscl)

# Put file path to ordinalRegression_Study2_excludingDeepConversation.csv below
df <- read.csv("~/CCR_Scale/Data_Analysis/Data/Study2Data/ordinalRegression_Study2_excludingDeepConversation.csv")

CCR.ord <- clmm(factor(Ranking) ~ CCR + (1|Subject), data=df)
Gratch.ord <- clmm(factor(Ranking) ~ Gratch + (1|Subject), data=df)

CCR.ord
Gratch.ord

anova(CCR.ord, Gratch.ord)

