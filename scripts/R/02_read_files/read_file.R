library(duckdb)
library(glue)

my_file_path <- "data/beds.csv"
con <- dbConnect(duckdb::duckdb())

result <- dbGetQuery(
  con,
  glue("
  SELECT COUNT(*)
  FROM read_csv_auto('{my_file_path}')
  WHERE Quarter = '2019Q2'
  ")
)

dbDisconnect(con, shutdown = TRUE)

print(result)
