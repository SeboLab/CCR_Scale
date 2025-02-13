library(psych)

# Put file name Study2Data.csv and Study2GratchAlreadyReversed.csv below

data <- read.csv("~/CCR_Scale/CCR_Scale_Study_1-3_Data_Analysis/Study_2/Study2Data.csv")
data <- subset(data, select = -deep) #exclude deep conversation

omega(data)

data <- read.csv("~/CCR_Scale/CCR_Scale_Study_1-3_Data_Analysis/Study_2/Study2GratchAlreadyReversed.csv")
omega(data)
