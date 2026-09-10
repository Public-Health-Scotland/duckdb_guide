import polars as pl
import duckdb

df_pl = pl.read_csv("data/beds.csv")

result = duckdb.query("SELECT COUNT(*) FROM df_pl WHERE Quarter = '2019Q2'").df()

print(result)