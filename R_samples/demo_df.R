library(duckdb)
library(data.table)

dt = fread("data/beds.csv")

# Connect to DuckDB
con <- dbConnect(duckdb::duckdb())
# Register the data.table
duckdb::duckdb_register(con, "dt_table", dt)

# Query it
result = dbGetQuery(con, "SELECT COUNT(*) FROM dt_table WHERE Quarter = '2019Q2'") |> as.data.table()
print(class(result))
print(result)
