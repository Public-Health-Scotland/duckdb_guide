## Python examples
This folder contains some basic Python examples using duckdb package.

### Requirements
These are the minimun required packages to run these scripts
```python
duckdb==1.5.5
pandas==3.0.5
python-dotenv=1.2.3
```

### Scripts

01_duckdb_creation/import_data_to_encrypted_duckdb.py: This script has two parts. The first one creates an encrypted duckdb file and creates 2 tables. The second part reads a table, prints the data type columns and prints the dataframe result. You have to create a .env file and type a password using this line `DUCKDB_KEY=type_here_a_long_password`

