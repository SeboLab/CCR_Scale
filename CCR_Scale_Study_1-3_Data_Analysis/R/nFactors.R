library(nFactors)
library(psych)
library(psycho)

# Put file path to Study1Data.csv below
data <- read.csv("~/CCR_Scale/Data_Analysis/Data/Study1Data.csv")

nfactors(data)
