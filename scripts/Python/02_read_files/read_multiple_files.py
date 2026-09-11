import duckdb
import pandas as pd

# all parquet files
files = "main/**/*.parquet"
# open an in-memory DuckDB connection
con = duckdb.connect()

# Prepare your query to read multiple parquet files
# Use where clause to load only needed data
my_data = con.execute(f"""
    SELECT code, user
    FROM '{files}'
    WHERE code = 100
""").fetchdf()

# close the connection
con.close()
# print value of my_data
print(my_data)
