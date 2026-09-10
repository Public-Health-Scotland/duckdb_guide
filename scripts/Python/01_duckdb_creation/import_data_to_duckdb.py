import duckdb
import pandas as pd

list_inputs = {
    "users": pd.DataFrame({
        "id": [1, 2, 3],
        "name": ["John", "David", "Joe"]
    }),
    "teams": pd.DataFrame({
        "team": ["red", "blue"]
    }),
    "tasks": pd.DataFrame({
        "task": ["clean", "wipe"]
    })
}

# When we use "with" we don't need to worry about closing connection. It closes for us
with duckdb.connect("data/sample.duckdb") as con:
    for table_name, df in list_inputs.items():
        con.sql(f"CREATE OR REPLACE TABLE {table_name} AS SELECT * FROM df")
