library(duckdb)

# Create a connection without a duckdb file
con <- dbConnect(duckdb::duckdb())

# Attach multiple databases wuth the same table structure
# If you have many files, you can dynamically attach only the relevant ones
dbExecute(con, "ATTACH 'data_2023.duckdb' AS db2023")
dbExecute(con, "ATTACH 'data_2024.duckdb' AS db2024")

# Query across them
result <- dbGetQuery(con, "
  SELECT col1, col2 FROM db2023.my_table
  UNION ALL
  SELECT col1, col2 FROM db2024.my_table
  WHERE some_column = 'value'
")
