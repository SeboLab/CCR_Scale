library(DescTools)
library(MASS)

# Put file path to Study2DataForOrdinalRegression.csv below
data <- read.csv("~/CCR_Scale/CCR_Scale_Study_1-3_Data_Analysis/Study_2/Study2DataForOrdinalRegression.csv")

data$Ranking <- factor(data$Ranking, levels = c(1, 2, 3, 4), ordered = TRUE)

CCR.ord <- polr(Ranking ~ CCR, data = data)

cat("PD pseudo R^2",fill=TRUE)
CCRrsquared <- PseudoR2(CCR.ord, which=c("CoxSnell","Nagelkerke","McFadden"))
print(CCRrsquared)

Gratch.ord <- polr(Ranking ~ Gratch, data = data)

cat("PD pseudo R^2",fill=TRUE)
gratchrsquared <- PseudoR2(Gratch.ord, which=c("CoxSnell","Nagelkerke","McFadden"))
print(gratchrsquared)
