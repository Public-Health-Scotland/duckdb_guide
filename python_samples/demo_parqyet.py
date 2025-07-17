import pandas as pd
import duckdb

result = duckdb.query("SELECT * FROM './data/admissions.parquet'").df()
print(result)