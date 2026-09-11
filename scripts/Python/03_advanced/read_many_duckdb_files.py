import duckdb
import pandas as pd

# Create an in-memory DuckDB connection
con = duckdb.connect()

# Attach multiple DuckDB databases
con.execute("ATTACH 'data_2023.duckdb' AS db2023")
con.execute("ATTACH 'data_2024.duckdb' AS db2024")

# Query across them
result = con.execute("""
    SELECT col1, col2 FROM db2023.my_table
    UNION ALL
    SELECT col1, col2 FROM db2024.my_table
    WHERE some_column = 'value'
""").fetchdf()

# Close the connection
con.close()

print(result)
