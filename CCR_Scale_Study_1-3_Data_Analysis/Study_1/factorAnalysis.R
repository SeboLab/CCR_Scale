library(psych)
library(paran)
library(GPArotation)

# Put file path to Study1Data.csv below
data <- read.csv("~/CCR_Scale/CCR_Scale_Study_1-3_Data_Analysis/Study_1/Study1Data.csv")

fa(data, nfactors = 2, rotate="promax", fm="pa")
