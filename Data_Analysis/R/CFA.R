library(lavaan)

# Put file path to CCR_Study2_allData.csv below:
data <- read.csv("~/CCR_Scale/Data_Analysis/Data/Study2Data/CCR_Study2_allData.csv")

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
