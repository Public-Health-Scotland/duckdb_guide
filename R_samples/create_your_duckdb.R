library(duckdb)
library(data.table)
# Duckdb has the capability to create tables in one file

dfusers <- data.table(id = c(1, 2, 3),
                    name = c("John", "David", "Joe"))

dfteams <- data.table(team = c("red", "blue"))

dftask <- data.table(task = c("clean", "wipe"))

# If you have a list of dataframe/data.table objects in R
list_imputs <- list(users = dfusers, teams = dfteams, tasks = dftask)

# you will create a duckdb file in your own current directory
conduck <- duckdb::dbConnect(duckdb::duckdb(), dbdir = "sample.duckdb")

sapply(names(list_imputs), function(name) {
  dbWriteTable(conduck, name, list_imputs[[name]])
})

dbDisconnect(conduck, shutdown = TRUE)