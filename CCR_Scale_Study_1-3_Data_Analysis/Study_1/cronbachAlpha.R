library(ltm)

# Put file path to Study1Data.csv below
data <- read.csv("~/CCR_Scale/CCR_Scale_Study_1-3_Data_Analysis/Study_1/Study1Data.csv")

data_19_items <- data[,c("warmth",
                         "empathy",
                         "friendliness",
                         "sympathy",
                         "closeness",
                         "positivity",
                         "liking.each.other",
                         "enthusiasm",
                         "deep.conversation",
                         "respect",
                         "getting.along",
                         "excitement",
                         "connection",
                         "coordination",
                         "focus",
                         "attentiveness",
                         "smooth.flow",
                         "equal.participation",
                         "engagement")]

cronbach.alpha(data_19_items, CI=TRUE, standardized=TRUE)


