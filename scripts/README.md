## Scripts folder
This folder contains two subfolders focused on R and Python script examples.

| Section         | Location                                       |
|-----------------|---------------------------------------------------|
| R examples      | [View R examples README](./R/README.md)           |
| Python examples | [View Python examples README](./Python/README.md) |

### General knowledge

#### DuckDB ways of working
- In memory: when you do not load a DuckDB file, but you can attach one later.
- From a DuckDB file: when you have a DuckDB file or want to create one.

#### SQL statements
- DuckDB works with SQL statements. If you have a 500 MB CSV file and only want to read a specific part of the data, you can reduce memory consumption. For example, you can run this statement: `select id, name from my_data.csv where city = 'New York';`

#### DuckDB can perform better than Parquet files with partitioning
- Hundreds of small Parquet files (less than 5 MB each) can slow down reads. Consider migrating to DuckDB.
- You can store more than one table in a DuckDB file.
- You can add a password to encrypt your DuckDB file.
- If you have very large files (10 GB each), you can create a master metadata file (in DuckDB or CSV format). This is a powerful way to track, organise, and query distributed DuckDB files. It acts like a catalog or index, helping you manage and access your data efficiently. See `metadata.csv`.
