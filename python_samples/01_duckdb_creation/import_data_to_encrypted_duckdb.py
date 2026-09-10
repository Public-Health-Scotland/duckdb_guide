import duckdb
import os
from dotenv import load_dotenv

load_dotenv()

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

# Open DuckDB read-only
con = duckdb.connect()

con.execute(f"""
    INSTALL httpfs;
    LOAD httpfs;
    ATTACH '{db_path}' AS enc (
        ENCRYPTION_KEY '{encryption_key}',
        ENCRYPTION_CIPHER 'GCM'
    );
    USE enc;
""")

df = con.execute("""
    SELECT
        QuarterQF,
        HB,
        HBQF,
        Location,
        LocationQF
    FROM beds
""").fetchdf()

con.close()

print(df)
