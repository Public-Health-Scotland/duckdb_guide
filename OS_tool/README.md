## Windows installation (DuckDB Desktop tooling)

-   You will have a powerfull tool in your CMD/powershell. No need to run R or Python.
-   We will use winget which is an official Microsoft tool (Windows Package Manager). It is **safe** since it pulls packages from the Microsoft Community Package Manifest Repository. This Microsoft resource has a review process to ensure packages are safe and legitimate.
-   Open a cmd or Powershell (windows) and run the following command: `winget install DuckDB.cli --version 1.4.4`
-   If you already have another DuckDb version you should uninstall it using this command: `winget uninstall DuckDB.cli`. You may need to reinstall the extensions after upgrading.
-   There is a file .duckdbrc in this repository which you need to copy in your user folder (C:\Users\your_user_name). This file contains the proxy configuration for duckdb. If you don't copy this file, you won't be able to install extensions and use the user interface.
![.duckdbrc file in Windows 11 file explorer](./img/image.png)

-   Then, you can start using duckdb, you need to run the command in a cmd/porwershell: `duckdb`
-   You can use the following command to check your installed extension: `SELECT extension_name, installed, description FROM duckdb_extensions();`

-   You can exit duckdb using .exit or simply closing the window

### Extensions

-   If you only read csv files, it is not mandatory to install the other extensions. So, you can skip these extensions installation.
-   If you already executed duckdb in your terminal/PowerShell you won't need to do it again.
-   If you cannot install extensions, go back an make sure if you copied the file .duckdbrc in your user folder (C:\Users\your_user_name).

| Extension  | Command                                       | Description                                                           |
|------------|-----------------------------------------------|------------------------|
| Excel      | `INSTALL excel;LOAD excel;`                   | enables you to read and write Excel (.xlsx) files              |
| Spatial    | `INSTALL spatial;LOAD spatial;`               | provides support for geospatial data processing                |
| Sqlite     | `INSTALL sqlite_scanner;LOAD sqlite_scanner;` | allows DuckDB to read and write data from SQLite database file |
| Httpfs     | `INSTALL httpfs;LOAD httpfs;`                 | allows you to read and write remote files over HTTP(S) and S3  |
| UI         | `INSTALL ui;LOAD ui;`                         | enables web bassed user interface                              |

### How to use duckdb

-   If you already executed duckdb in your terminal/PowerShell you won't need to do it again.
-   There is a folder called **data** in this repository. You can use the files in this folder to practice with duckdb.
-   If you want to read files from your network and you don't want to deal with absolute/relative long paths. You can use this Windows workaround. Open your file explorer, go to your network folder, keep pressed shift key and right click in an empty space. You will see **Open PowerShell window here** ![DuckDB as part of right click options menu](./img/image-8.png)

-   You can write SQL in multiline way. Press enter for multiple lines. A colon (;) means the end of a query.

-   There are 2 very useful commands to check datasets. They are “describe” and “summarize”. In this example, I am using beds.csv `describe from file_name.csv` or `summarize from file_name.csv`

![a summarise and describe SQL command example](./img/image-3.png)

-   It’s time to read an excel file using the function read_xlsx('file_name.xlsx', sheet='sheet_name')

![how to read an Excel file](./img/image-4.png)

-   If you have a parquet file, it is simple as a csv file

-   If you have a duckdb.file you can easily start duckdb with the name of the file.

![how to open a duckdb file](./img/image-5.png)

-   If you already started duckdb with no duck file. You can run "attach" and "use" commands

![how to attach a DuckDb file after starting duckdb with no files attached](./img/image-7.png)

-   It is the same process if you want to work with a sqlite file:

![how to open a sqlite file](./img/image-6.png)

-   If you want to export one table from a duckdb or sqlite database, you can use the command COPY `COPY table_name to ‘file_name.csv’ (format ‘csv’);` `COPY table_name to ‘file_name.parquet’ (format ‘parquet’);` `COPY (select field_name, mean(value) as mean_value from admissions_day group by field_name) to ‘grouped_field_mean.csv’ (format ‘csv’);`

## intermediate SQL commands

-   You can join 2 tables (same file or different files and formats)

```         
select a.*, b.country
from read_xlsx('demo.xlsx', sheet='sales') a left join read_xlsx('demo.xlsx', sheet='countries') b
on a.id_country=b.id;
```

![a left join between 2 sheets in the same Excel file](img/image-9.png)

```         
select a.*, b.country
from read_xlsx('demo.xlsx', sheet='sales') a full join read_xlsx('demo.xlsx', sheet='countries') b
on a.id_country=b.id;
```

![a full join between 2 sheets in the same Excel file](img/image-11.png)

-   You can have multiple subqueries like this:

```         
WITH cleaned AS (
  SELECT * FROM read_xlsx('demo.xlsx', sheet='sales')
  WHERE amount IS NOT NULL
),
aggregated AS (
  SELECT id_country, AVG(amount) as avg_amount
  FROM cleaned
  GROUP BY id_country
)
select b.country, round(a.avg_amount, 2) as avg_amnt
from aggregated a join read_xlsx('demo.xlsx', sheet='countries') b
on a.id_country=b.id
order by avg_amount desc;
```

![multiple subqueries to calculate an average value per country](img/image-10.png)

## Advance SQL commands

-   Regular expressions for column names using columns function `select HB, columns('Average.*') from beds.csv;`
-   We can create the pivot of a table `PIVOT beds.csv ON Quarter USING MEAN(PercentageOccupancy) GROUP BY HB;`
-   It is possible to do the unpivot too `UNPIVOT pivoted.csv ON COLUMNS(* EXCLUDE HB) INTO NAME Quarter VALUE sales;`
