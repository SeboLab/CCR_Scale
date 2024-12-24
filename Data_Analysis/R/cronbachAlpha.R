library(ltm)

# Put file name (Study1Data.csv, CCR_Study2_excludingDeepConversation.csv, or Gratch_alreadyReversed.csv) below:
data <- read.csv("~/CCR_Scale/Data_Analysis/Data/Study2Data/Gratch_alreadyReversed.csv")

cronbach.alpha(data, CI=TRUE, standardized=TRUE)
