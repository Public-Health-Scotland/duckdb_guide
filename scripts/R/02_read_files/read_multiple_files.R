library(duckdb)
library(data.table)

# memory DuckDB connection
duckcon <- dbConnect(duckdb::duckdb())

# Query all Parquet files in subfolders like main/sub/names.parquet
files <- glue::glue("main/**/*.parquet")

# Use where clause to load only needed data
query <- glue::glue("SELECT code, user FROM '{files}' where code = 100")

# Generate a data.table from the query result
my_data <- DBI::dbGetQuery(duckcon, query) |> as.data.table()

# close the connection
dbDisconnect(duckcon, shutdown = TRUE)
# print value of my_data
print(my_data)
