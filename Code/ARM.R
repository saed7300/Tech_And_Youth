###ARM

library(arules)
library(arulesViz)


full_data = 'C:\\Users\\sneaz\\Documents\\Text Mining\\Data\\Transaction Data\\transaction_data_label.csv'
#education_data = 'https://raw.githubusercontent.com/saed7300/Tech_And_Youth/main/Data/Transaction%20Data/transaction_data_education.csv'
transaction_data <- read.transactions(full_data,
                                     rm.duplicates=FALSE,
                                     format="basket",
                                     sep=","
                                     )
#inspect(transaction_data)
education_rules = arules::apriori(transaction_data,
                               parameter = list(support=.0001, confidence=.0001,
                                                minlen=2, maxlen=5),
                               appearance = list(rhs = c("education")))
parenting_rules = arules::apriori(transaction_data,
                                  parameter = list(support=.01, confidence=.01,
                                                   minlen=2, maxlen=5),
                                  appearance = list(rhs = c("parenting")))
mh_rules = arules::apriori(transaction_data,
                                  parameter = list(support=.0001, confidence=.0001,
                                                   minlen=2, maxlen=5),
                                  appearance = list(rhs = c("mental health")))
society_rules = arules::apriori(transaction_data,
                                  parameter = list(support=.0001, confidence=.0001,
                                                   minlen=2, maxlen=5),
                                  appearance = list(rhs = c("in society")))
inspect(education_rules[1:20])
sort_rules_sup <- sort(education_rules, by="support", decreasing = TRUE)
sort_rules_con <- sort(education_rules, by="confidence", decreasing = TRUE)
sort_rules_lift <- sort(education_rules, by="lift", decreasing = TRUE)
inspect(sort_rules_sup[1:15])
inspect(sort_rules_con[1:15])
inspect(sort_rules_lift[1:15])

plot(sort_rules_sup[1:15], method="graph", engine = "interactive",
     shading="support")



sort_rules_sup <- sort(parenting_rules, by="support", decreasing = TRUE)
sort_rules_con <- sort(parenting_rules, by="confidence", decreasing = TRUE)
sort_rules_lift <- sort(parenting_rules, by="lift", decreasing = TRUE)
inspect(sort_rules_sup[1:15])
inspect(sort_rules_con[1:15])
inspect(sort_rules_lift[1:15])

plot(sort_rules_sup[1:15], method="graph", engine = "interactive", shading="support")


sort_rules_sup <- sort(mh_rules, by="support", decreasing = TRUE)
sort_rules_con <- sort(mh_rules, by="confidence", decreasing = TRUE)
sort_rules_lift <- sort(mh_rules, by="lift", decreasing = TRUE)
inspect(sort_rules_sup[1:15])
inspect(sort_rules_con[1:15])
inspect(sort_rules_lift[1:15])

plot(sort_rules_sup[1:15], method="graph", engine = "interactive", shading="support")



sort_rules_sup <- sort(society_rules, by="support", decreasing = TRUE)
sort_rules_con <- sort(society_rules, by="confidence", decreasing = TRUE)
sort_rules_lift <- sort(society_rules, by="lift", decreasing = TRUE)
inspect(sort_rules_sup[1:15])
inspect(sort_rules_con[1:15])
inspect(sort_rules_lift[1:15])

plot(sort_rules_sup[1:15], method="graph", engine = "interactive", shading="support")
