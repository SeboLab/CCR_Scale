# In-person study (Study 3)

# Put file path to Study3_CorrelationCoefficient.csv below
df <- read.csv("~/CCR_Scale/CCR_Scale_Study_1-3_Data_Analysis/Study_3/Study3_CorrelationCoefficient.csv")

Score <- df$rapportscore
Rating <- df$perceived_robot_responsiveness

# Calculate correlation coefficient and p-value
result <- cor.test(Score, Rating)

# Print correlation coefficient and p-value
cat("Correlation coefficient:", result$estimate, "\n")
cat("P-value:", result$p.value, "\n")