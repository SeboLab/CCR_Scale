library(psych)

library(paran)

# Put file path to Study1Data.csv below
data <- read.csv("~/CCR_Scale/Data_Analysis/Data/Study1Data.csv")

fa(data, nfactors = 2, rotate="promax", fm="pa")
