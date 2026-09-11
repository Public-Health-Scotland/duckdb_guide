This README file helps to understand how views work in duckdb and how to use them. Views are virtual tables that are defined by a SQL query. They do not store data themselves but provide a way to simplify complex queries and improve readability.

# Pre requirements
-   You need to have duckdb installed. Please, follow the instructions in the main README.md file.
-   You need to have a duckdb file with some tables to practice with views. You can use the files in the **data** folder of this repository or create your own duckdb file.
-   You can use the duckdb CLI or the duckdb UI to create and query views.

# Create a view
To create a view, you can use the following syntax:

```sql
BEGIN;
CREATE VIEW view_name AS
SELECT column1, column2
FROM table_name
WHERE condition;
COMMIT;
```

# Query a view
Once you have created a view, you can query it just like a regular table:

```sql
SELECT column1, column2 FROM view_name;
```

## example
- Download sample.duckdb file from the data folder and open it in the duckdb UI using this command `duckdb sample.duckdb -ui`
- Run this SQL to see your tables in the duckdb file (You will see tasks, teams and users tables):

```sql
show tables;
```


- Run this SQL to create a view called "v_user_details" that selects the "admissions_day" table:

```sql
BEGIN;
CREATE VIEW v_user_details AS
select 
  t.team_name, u.user_fname,u.user_lname 
from teams t inner join users u on t.team_id=u.team_id;
COMMIT;
```

-   Run this SQL to query the view (it will return 3 rows from the original DuckDB file):

```sql
select 
    team_name,user_fname,user_lname 
from v_user_details
```

Note: 
-   Views can support join operations, but they do not support insert, update, or delete operations since they are virtual tables.
-   Views can be used to simplify complex queries by encapsulating them in a single view definition, making it easier to reuse and maintain the logic.
-   SQL BEGIN and COMMIT block is important when you are creating a new object (e.g. tables, views) in your DuckDB file.