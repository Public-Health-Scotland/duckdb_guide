# duckdb_guide
DuckDB is an in-process SQL OLAP database management system. Simple, feature-rich, fast & open source. If you only want to code in R you have to check R_samples folder.

## Windows installation
- You will have a powerfull tool in your CMD/powershell. No need to run R or Python.
- We will use winget which is an official Microsoft tool (Windows Package Manager). It is **safe** since It pulls packages from the Microsoft Community Package Manifest Repository, which has a review process to ensure packages are safe and legitimate.
- Open a cmd or Powershell (windows) and run the following command: `winget install DuckDB.cli`
- Then, you can start using duckdb, you need to run the command in a cmd/porwershell: `duckdb`
- You can use the following command to check your installed extension: `SELECT extension_name, installed, description FROM duckdb_extensions();`
![alt text](./img/image-1.png)
- You can exit duckdb using .exit or simply closing the window

### Extensions
- If you only read csv files, it is not mandatory to install the other extensions. So, you can skip these extensions installation.
- The httpfs extension allows you to read and write remote files over HTTP(S) and S3
`INSTALL httpfs;`
`LOAD httpfs;`
- The excel extension enables you to read and write Excel (.xlsx) files
`INSTALL excel;`
`LOAD excel;`
- The spatial extension provides support for geospatial data processing
`INSTALL spatial;`
`LOAD spatial;`
- The sqlite_scanner extension allows DuckDB to directly read and write data from SQLite database file
`INSTALL sqlite_scanner;`
`LOAD sqlite_scanner;`
![alt text](./img/image-2.png)
- If you cannot install the extensions, it may be your firewall/VPN permissions.

### How to use duckdb
- If you already executed duckdb in your PowerShell you won't need to do it again.
- If you want to read files from your network and you don't want to deal with absolute/relative long paths. You can use this Windows workaround. Open your file explorer, go to your network folder, keep pressed shift key and right click in an empty space. You will see **Open PowerShell window here**
![alt text](./img/image-8.png)
- There are 2 very useful commands to check datasets. They are “describe” and “summarize”. In this example, I am using beds.csv
`describe from file_name.csv`
`summarize from file_name.csv`
![alt text](./img/image-3.png)
- It’s time to read an excel file using the function read_xlsx('file_name.xlsx', sheet='sheet_name')
![alt text](./img/image-4.png)
- If you have a parquet file, it is simple as a csv file
- If you have a duckdb.file you can easily start duckdb with the name of the file.
![alt text](./img/image-5.png)
- If you already started duckdb with no duck file. You can run "attach" and "use" commands
![alt text](./img/image-7.png)
- It is the same process if you want to work with a sqlite file:
![alt text](./img/image-6.png)
- If you want to export one table from a duckdb or sqlite database, you can use the command COPY
`COPY table_name to ‘file_name.csv’ (format ‘csv’);`
`COPY table_name to ‘file_name.parquet’ (format ‘parquet’);`
`COPY (select field_name, mean(value) as mean_value from admissions_day group by field_name) to ‘grouped_field_mean.csv’ (format ‘csv’);`

## Advance SQL commands
- Regular expressions for column names using columns function
`select HB, columns('Average.*') from beds.csv;`
- We can create the pivot of a table
`PIVOT beds.csv ON Quarter USING MEAN(PercentageOccupancy) GROUP BY HB;`
- It is possible to do the unpivot too
`UNPIVOT pivoted.csv ON COLUMNS(* EXCLUDE HB) INTO NAME Quarter VALUE sales;`
