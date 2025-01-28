library(psych)

# Put file path below (Study1Data_noSpaces.csv, CCR_Study2_allData.csv, or Gratch_alreadyReversed_noItemNames.csv)
data <- read.csv("~/CCR_Scale/Data_Analysis/Data/Study2Data/CCR_Study2_allData.csv")

omega(data)

omega(data, nfactors=2)

study1factors <- c(
  "sympathy",
  "empathy",
  "warmth",
  "excitement",
  "enthusiasm",
  "positivity",
  "friendliness",
  "connection",
  "respect",
  "liking",
  "closeness",
  "getting",
  "coordination",
  "focus",
  "attentiveness",
  "smooth",
  "equal",
  "engagement",
  "deep"
)

# Excluding deep conversation
factor1 <- c(
"sympathy",
"empathy",
"warmth",
"excitement",
"enthusiasm",
"positivity",
"friendliness",
"connection",
"respect",
"liking",
"closeness",
"getting"
)

factor2 <- c(
  "coordination",
  "focus",
  "attentiveness",
  "smooth",
  "equal",
  "engagement"
)

# Combined factor 1 and 2 excluding deep conversation
factors <- c(
  "sympathy",
  "empathy",
  "warmth",
  "excitement",
  "enthusiasm",
  "positivity",
  "friendliness",
  "connection",
  "respect",
  "liking",
  "closeness",
  "getting",
  "coordination",
  "focus",
  "attentiveness",
  "smooth",
  "equal",
  "engagement"
)

gratch <- c("q1","q2","q3","q4","q5","q6","q7","q8","q9","q10","q11")

run = data[factors]
omega(run)
