library(DescTools)
library(MASS)

# Put file path to ordinalRegression_Study2_excludingDeepConversation.csv below
data <- read.csv("~/CCR_Scale/Data_Analysis/Data/Study2Data/ordinalRegression_Study2_excludingDeepConversation.csv")

data$Ranking <- factor(data$Ranking, levels = c(1, 2, 3, 4), ordered = TRUE)

CCR.ord <- polr(Ranking ~ CCR, data = data)

cat("PD pseudo R^2",fill=TRUE)
CCRrsquared <- PseudoR2(CCR.ord, which=c("CoxSnell","Nagelkerke","McFadden"))
print(CCRrsquared)

Gratch.ord <- polr(Ranking ~ Gratch, data = data)

cat("PD pseudo R^2",fill=TRUE)
gratchrsquared <- PseudoR2(Gratch.ord, which=c("CoxSnell","Nagelkerke","McFadden"))
print(gratchrsquared)
