import duckdb
import pandas as pd

my_file_path = "data/beds.csv"

# Connect to DuckDB
con = duckdb.connect()

# Run the query
result = con.execute(f"""
    SELECT COUNT(*)
    FROM read_csv_auto('{my_file_path}')
    WHERE Quarter = '2019Q2'
""").fetch_df()

# Close connection
con.close()

print(result)
