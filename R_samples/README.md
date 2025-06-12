# Installation
- Run the following R code: `install.packages("duckdb")`

# DUCKDB ways to work
- In memory: when you don't load a duckdb file
- From a duckdb file: when you have a duckdb file or you are creating one

# SQL statements
- Duckdb work with sql statements. If you have a 500 MB csv file and you only want a specify part of the data. You will reduce memory consumption. `select id, name from my_data.csv where city = 'New York';`

# Disadvantage of using many parquet files with partitioning
= Hundreds of small files can slow down when loading files. Consider migration to duckdb
- You can create a master metadata file (in DuckDB or CSV format) because it is a powerful way to track, organize, and query your distributed DuckDB files. It acts like a catalog or index, helping you manage and access your data efficiently. See metadata.csv
