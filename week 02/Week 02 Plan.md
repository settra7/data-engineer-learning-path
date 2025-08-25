# 📅 Week 2 — Advanced SQL, Pandas, and Relational Modeling

## 🎯 Weekly Goal:

- Reinforce SQL (including window functions, CTE, PIVOT/UNPIVOT).
- Master advanced Pandas techniques.
- Understand the basics of relational modeling (star/snowflake).
- Create a portfolio project: Kaggle dataset analytics + data model diagram.

## Day 1 — Basic SQL Review

Theory:
- ```SELECT, WHERE, GROUP BY, HAVING.```
- ```JOIN (INNER, LEFT, RIGHT, FULL).```

Practice:
- Take a database (PostgreSQL or SQL Server).
- Create Customers, Orders, Products tables.

Try these queries:
- Find all customers with orders > 3.
- Calculate the total amount of orders for each customer.

## Day 2 — Window functions

Theory:
- ```ROW_NUMBER(), RANK(), DENSE_RANK()```.
- ```LAG(), LEAD(), OVER(PARTITION BY ... ORDER BY ...)```.

Practice:
- Take a table of orders.
- For each customer, number the orders by date.
- Find orders made on two consecutive days (```LAG()```).

## Day 3 — CTE and PIVOT/UNPIVOT

Theory:
- CTE (Common Table Expressions) — timed results.
- PIVOT/UNPIVOT (reverse rows into columns and back).

Practice:
- Use CTE to find customers with an average order value > 100.
- Make a PIVOT: count the number of orders by month in a table.

## Day 4 — Pandas: Deepening

Theory:
- ```merge```, ```join```, ```groupby``` with multiple columns.
- ```pivot_table```, ```melt```.

Practice:
- Download the Titanic or Netflix Movies dataset from Kaggle.
- Build a pivot_table: average age of passengers by class and gender.
- Use ```melt``` to reverse the table.

## Day 5 — Relational Modeling

Theory:
- Normalization (1NF, 2NF, 3NF).
- Star Schema.
- Snowflake Schema.

Practice:
- Build a schema for a mini Data Warehouse:
- Fact: sales.
- Dimensions: customers, products, time.
- Use dbdiagram.io or draw.io.

## Day 6 — Mini-Project (Part 1)

### 📂 Project 2: Kaggle Dataset Analytics

- Take a dataset (e.g. Titanic, Netflix, or Sales Data).
- In SQL, make some analytical queries:
- TOP-10 by some metric.
- Use window functions.
- Use CTE.
- Save SQL scripts in the week2_sql_analysis folder.

## Day 7 — Mini-project (part 2)

### 📂 Project 2 (continued)
- Do a similar analysis in Pandas.
- Build a pivot table (pivot_table).
- Draw a star model diagram (Star Schema) in dbdiagram.io.

Upload to GitHub in the week2_project folder:
- Jupyter Notebook (analysis.ipynb).
- SQL file (queries.sql).
- Model diagram (model.png).
- README with a description of the project.

## 📦 Summary of the second week
- A week2_project folder will appear in GitHub.
- Inside: SQL queries, Jupyter Notebook, data model diagram.
- At the interview at Vega IT you will be able to show: “I did the relational model, SQL analytics and Pandas processing.”