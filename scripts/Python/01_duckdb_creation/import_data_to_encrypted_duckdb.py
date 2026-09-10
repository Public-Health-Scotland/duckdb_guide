import os
from dotenv import load_dotenv
import duckdb
import pandas as pd

csv_path = "data/beds.csv"
parquet_path = "data/admissions.parquet"
db_path = "data/encrypted_data.duckdb"
encryption_key = os.getenv("DUCKDB_KEY")

# Start in-memory DuckDB
con = duckdb.connect()

# Attach encrypted database
con.execute(f"""
    INSTALL httpfs;
    LOAD httpfs;
    ATTACH '{db_path}' AS enc (
        ENCRYPTION_KEY '{encryption_key}',
        ENCRYPTION_CIPHER 'GCM'
    );
    USE enc;
""")

# Import CSV
con.execute(f"""
    CREATE TABLE beds AS
    SELECT *
    FROM read_csv_auto('{csv_path}');
""")

# Import Parquet
con.execute(f"""
    CREATE TABLE admissions AS
    SELECT *
    FROM read_parquet('{parquet_path}');
""")

print("Successfully created encrypted DuckDB file and imported data.")

con.close()

# Open DuckDB connection
con = duckdb.connect()

# attach file in Read only mode
con.execute(f"""
    INSTALL httpfs;
    LOAD httpfs;
    ATTACH '{db_path}' AS enc (
        READ_ONLY,
        ENCRYPTION_KEY '{encryption_key}',
        ENCRYPTION_CIPHER 'GCM'
    );
    USE enc;
""")

df = con.execute("""
SELECT
    Quarter,
    HB,
    HBQF,
    Location,
    SpecialtyName
FROM beds""").fetchdf()

con.close()

print(df.dtypes)
print(df)
