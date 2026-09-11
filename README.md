# DuckDB guide

DuckDB is an in-process SQL OLAP database management system. It is simple, feature-rich, fast, and open source. The recommended version is 1.4.4 (February 2026). If you only want to code in R, check the `R_samples` folder.

## DuckDB ecosystem
1. DuckDB programming language package: This software allows users to easily integrate DuckDB in R/Python projects.
2. DuckDB OS tooling: This software can be installed at the operating-system level (e.g. Windows, Linux). It has extensions to read Excel files, PostgreSQL, a web-based user interface, and other interesting features.

Note: The DuckDB packages for R and Python can be installed directly from CRAN and PyPI, respectively. Installation of the DuckDB command-line (OS) tooling is optional and is only required if you intend to use DuckDB outside Posit Workbench.

## More sections

| Topic            | More info                            |
|------------------|--------------------------------------|
| R/Python package | [View script examples README](./scripts/README.md) |
| OS tool          | [View OS tool README](./OS_tool/README.md)          |
| UI (OS tool)     | [View UI README](./ui/README.md)                    |
| Common queries   | [View common queries README](./common_queries/)     |
| DuckDB views     | [View views README](./view/README.md)                |

## Resources

-   [Official website](https://duckdb.org/)
-   [R functions and DuckDB performance](https://gsandrof66.github.io/Rperformance/Basic_perf.html)
