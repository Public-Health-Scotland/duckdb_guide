## Python examples
This folder contains some basic R examples using duckdb package.

### Requirements
These are the minimun required packages to run these scripts
```r
install.packages("duckdb")
install.packages("glue")
install.packages("dotenv")
```

### Scripts

01_duckdb_creation/import_data_to_encrypted_duckdb.R: This script has two parts. The first one creates an encrypted duckdb file and creates 2 tables. The second part reads a table, prints the data type columns and prints the dataframe result. You have to create a .env file and type a password using this line `DUCKDB_KEY=type_here_a_long_password` and press enter to have an empty line at the end.
