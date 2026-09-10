library(duckdb)
library(data.table)

# use dbdir = ":memory:" when you don't have a duckdb file and you will read data from other file extensions
duckcon <- duckdb::dbConnect(duckdb::duckdb(), dbdir = ":memory:")

# Query all Parquet files in subfolders like main/sub/names.parquet
files <- glue::glue("main/**/*.parquet")

# Use where clause to load only needed data
query <- glue::glue("SELECT code, user FROM '{files}' where code = 100")

my_data <- DBI::dbGetQuery(duckcon, query) |> as.data.table()
