# Comparing CCR Scale to Gratch study (Study 2)

# Put file path to Study2DataForOrdinalRegression.csv below
df <- read.csv("~/CCR_Scale/CCR_Scale_Study_1-3_Data_Analysis/Study_2/Study2DataForOrdinalRegression.csv")

Gratch <- df$Gratch
CCR <- df$CCR

# Calculate correlation coefficient and p-value
result <- cor.test(Gratch, CCR)

# Print correlation coefficient and p-value
cat("Correlation coefficient:", result$estimate, "\n")
cat("P-value:", result$p.value, "\n")



