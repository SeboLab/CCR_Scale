library(ltm)

# Put file name Study2Data.csv and Study2GratchAlreadyReversed.csv below

data <- read.csv("~/CCR_Scale/CCR_Scale_Study_1-3_Data_Analysis/Study_2/Study2Data.csv")
data <- subset(data, select = -deep) #exclude deep conversation
cronbach.alpha(data, CI=TRUE, standardized=TRUE)

data <- read.csv("~/CCR_Scale/CCR_Scale_Study_1-3_Data_Analysis/Study_2/Study2GratchAlreadyReversed.csv")

cronbach.alpha(data, CI=TRUE, standardized=TRUE)

