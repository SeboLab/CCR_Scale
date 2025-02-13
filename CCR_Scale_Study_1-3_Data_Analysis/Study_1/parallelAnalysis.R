install.packages("paran")

library(paran)

# Put file path to Study1Data.csv below
data <- read.csv("~/CCR_Scale/CCR_Scale_Study_1-3_Data_Analysis/Study_1/Study1Data.csv")


paran(data, cfa=TRUE, graph=TRUE, color=TRUE, col=c("black","orange","blue"))
