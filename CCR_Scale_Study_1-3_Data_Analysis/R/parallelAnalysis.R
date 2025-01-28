install.packages("paran")

library(paran)

# Put file path to Study1Data.csv below
data <- read.csv("~/CCR_Scale/Data_Analysis/Data/Study1Data.csv")
  
paran(data, cfa=TRUE, graph=TRUE, color=TRUE, col=c("black","red","blue"))
