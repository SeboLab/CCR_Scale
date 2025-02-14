library(ltm)

# Put file name Study3Data.csv below
data <- read.csv("~/CCR_Scale/CCR_Scale_Study_1-3_Data_Analysis/Study_3/Study3Data.csv", header=T)
#select the 18 scale item columns
data <- data[, c("Attentiveness","Sympathy","Empathy","Warmth","Excitement","Enthusiasm","Positivity","Friendliness","Connection",
                 "Coordination","Focus","Engagement","Respect","Liking_each_other","Closeness","Equal_participation","Getting_along","Smooth_flow")]

cronbach.alpha(data, CI=TRUE, standardized=TRUE)
