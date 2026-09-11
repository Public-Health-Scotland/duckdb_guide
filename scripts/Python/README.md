## Python examples
This folder contains basic Python examples using the DuckDB package.

### Requirements
These are the minimum required packages to run the scripts:
```python
duckdb==1.5.5
pandas==3.0.5
python-dotenv==1.2.3
```

### Scripts

1. 01_duckdb_creation/import_data_to_encrypted_duckdb.py: This script has two parts. The first one creates an encrypted duckdb file and creates 2 tables. The second part reads a table, prints the data type columns and prints the dataframe result. You have to create a .env file and type a password using this line `DUCKDB_KEY=type_here_a_long_password` and press enter to have an empty line at the end.

2. 01_duckdb_creation/import_data_to_duckdb.py: This script creates a non encrupted DuckDB file based on 3 data.table objects.

3. 02_read_files/read_file.py: This script reads a CSV file directly, allowing you to avoid creating a DuckDB file. It efficiently loads only the required data rather than processing the entire file.

4. 02_read_files/read_multiple_files.py: This script reads multiple Parquet files. Each file must have an identical schema (matching column names).

5. 03_advanced/read_many_duckdb_files.py: This script reads multiple DuckDB files. If a DuckDB file exceeds 5 GB, it may be advisable to create a second one to prevent performance degradation.
