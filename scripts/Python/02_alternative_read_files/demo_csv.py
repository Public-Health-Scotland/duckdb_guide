import pandas as pd
import duckdb

df = pd.read_csv("data/beds.csv")
result = duckdb.query("SELECT COUNT(*) FROM df WHERE Quarter = '2019Q2'").df()
print(result)