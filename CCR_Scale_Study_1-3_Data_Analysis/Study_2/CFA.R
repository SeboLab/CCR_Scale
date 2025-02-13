library(lavaan)

# Put file path to Study2Data.csv
data <- read.csv("~/CCR_Scale/CCR_Scale_Study_1-3_Data_Analysis/Study_2/Study2Data.csv")

# Specify the CFA model (excluding deep conversation)
model <- '
    first =~ sympathy+empathy+warmth+excitement+enthusiasm+positivity+friendliness+connection+respect+liking+closeness+getting
    second =~ attentiveness+coordination+focus+equal+smooth+engagement
    '

# Run CFA
cfa_result <- cfa(model, data = data, ordered=TRUE)

# Obtain fit indices
fit_indices <- fitMeasures(cfa_result, c("cfi", "tli", "rmsea", "srmr"))
fit_indices
