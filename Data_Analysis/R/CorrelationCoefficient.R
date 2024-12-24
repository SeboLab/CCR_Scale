# Comparing CCR Scale to Gratch study (study 2)

# Put file path to ordinalRegression_Study2_excludingDeepConversation.csv below
df <- read.csv("~/CCR_Scale/Data_Analysis/Data/Study2Data/ordinalRegression_Study2_excludingDeepConversation.csv")

Gratch <- df$Gratch
CCR <- df$CCR

# Calculate correlation coefficient and p-value
result <- cor.test(Gratch, CCR)

# Print correlation coefficient and p-value
cat("Correlation coefficient:", result$estimate, "\n")
cat("P-value:", result$p.value, "\n")



# In-person study (study 3)

# Put file path to Study3_CorrelationCoefficient.csv below
df <- read.csv("~/CCR_Scale/Data_Analysis/Data/Study3_CorrelationCoefficient.csv")

Score <- df$rapportscore
Rating <- df$participantrating

# Calculate correlation coefficient and p-value
result <- cor.test(Score, Rating)

# Print correlation coefficient and p-value
cat("Correlation coefficient:", result$estimate, "\n")
cat("P-value:", result$p.value, "\n")



