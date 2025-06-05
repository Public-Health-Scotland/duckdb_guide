# Installation
- Run the following R code: `install.packages("duckdb")`

# DUCKDB ways to work
- In memory: when you don't load a duckdb file
- From a duckdb file: when you have a duckdb file or you are creating one

# SQL statements
- Duckdb work with sql statements. If you have a 500 MB csv file and you only want a specify part of the data. You will reduce memory consumption. `select id, name from my_data.csv where city = 'New York';`