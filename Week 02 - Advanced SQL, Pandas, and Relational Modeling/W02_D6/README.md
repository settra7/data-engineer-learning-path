# 📂 Day 6 — Mini-project: Kaggle dataset analytics
## 🔹 Preparation

Choose a dataset (preferably a small one, so as not to waste time cleaning):

- Titanic ([from Kaggle](https://www.kaggle.com/c/titanic/data))
- Netflix Movies ([from Kaggle](https://www.kaggle.com/datasets/shivamb/netflix-shows))
- Superstore Sales ([from Kaggle](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final))

Create a table in the database (Titanic, Netflix, Sales — depending on your choice).

Load the data (via CSV import or INSERT).

## 🔹 Tasks

### 1. TOP-10 by metric

Examples:
- Titanic → TOP-10 oldest passengers.
- Netflix → TOP-10 countries with the largest number of films.
- Sales → TOP-10 products by total revenue.

👉 Save the result in the query 01_top10.sql.

### 2. Use window functions
Examples:
- Titanic → add a seat number for each passenger in order of age.
- Netflix → number the movies by year of release.
- Sales → for each customer, calculate the cumulative sum of orders.

👉 Save as 02_window_functions.sql.

### 3. Use CTE (Common Table Expressions)

Examples:
- Titanic → first select passengers over 30 in the CTE, then calculate the average age from this set.
- Netflix → make a CTE with a filter of "only Movies", then calculate the TOP-5 genres inside it.
- Sales → make a CTE with revenue calculation by category, then select only those with > 10000.

👉 Save as 03_cte.sql.

### 4. Extra (if you have time)
- Use LAG()/LEAD() - for example, compare the release date of the current and next movie.
- Use nested CTEs (one on top of the other).

👉 Save as 04_extra.sql.

# 📂 My comments on the implementation

I found it difficult to import ```CSV``` files using SQL Server's built-in tools (especially when it came to choosing the right data types for the columns), so I wrote a universal Python loading script: ```W02_D6_import_to_sql_server.py```

With this script, I was able to load all three datasets at once and get the right data types in each column.

Here are the types of data I was able to obtain using this script:

```sql
/****** Object:  Table [dbo].[Netflix_Movies_and_TV_Shows]    Script Date: 29.08.2025 10:29:13 ******/

CREATE TABLE [dbo].[Netflix_Movies_and_TV_Shows](
	[show_id] [nvarchar](10) NULL,
	[type] [nvarchar](10) NULL,
	[title] [nvarchar](110) NULL,
	[director] [nvarchar](210) NULL,
	[cast] [nvarchar](780) NULL,
	[country] [nvarchar](130) NULL,
	[date_added] [date] NULL,
	[release_year] [int] NULL,
	[rating] [nvarchar](10) NULL,
	[duration] [nvarchar](10) NULL,
	[listed_in] [nvarchar](80) NULL,
	[description] [nvarchar](250) NULL
) ON [PRIMARY]
GO

/****** Object:  Table [dbo].[Superstore_Dataset]    Script Date: 29.08.2025 10:29:20 ******/

CREATE TABLE [dbo].[Superstore_Dataset](
	[Row ID] [int] NULL,
	[Order ID] [nvarchar](20) NULL,
	[Order Date] [date] NULL,
	[Ship Date] [nvarchar](10) NULL,
	[Ship Mode] [nvarchar](20) NULL,
	[Customer ID] [nvarchar](10) NULL,
	[Customer Name] [nvarchar](30) NULL,
	[Segment] [nvarchar](20) NULL,
	[Country] [nvarchar](20) NULL,
	[City] [nvarchar](20) NULL,
	[State] [nvarchar](20) NULL,
	[Postal Code] [int] NULL,
	[Region] [nvarchar](10) NULL,
	[Product ID] [nvarchar](20) NULL,
	[Category] [nvarchar](20) NULL,
	[Sub-Category] [nvarchar](20) NULL,
	[Product Name] [nvarchar](130) NULL,
	[Sales] [float] NULL,
	[Quantity] [int] NULL,
	[Discount] [float] NULL,
	[Profit] [float] NULL
) ON [PRIMARY]
GO

/****** Object:  Table [dbo].[Titanic]    Script Date: 29.08.2025 10:29:28 ******/

CREATE TABLE [dbo].[Titanic](
	[PassengerId] [int] NULL,
	[Survived] [int] NULL,
	[Pclass] [int] NULL,
	[Name] [nvarchar](90) NULL,
	[Sex] [nvarchar](10) NULL,
	[Age] [float] NULL,
	[SibSp] [int] NULL,
	[Parch] [int] NULL,
	[Ticket] [nvarchar](20) NULL,
	[Fare] [float] NULL,
	[Cabin] [nvarchar](20) NULL,
	[Embarked] [nvarchar](10) NULL
) ON [PRIMARY]
GO
```

I also needed some manipulation to process the loaded data. To convert string fields containing non-standard date formats to date format (e.g. '```6/14/2014```' and '```September 22, 2021```'), I used the following construction:

```sql
UPDATE
	[dbo].[Netflix_Movies_and_TV_Shows]
SET
	[date_added] = PARSE([date_added] AS DATE USING 'en-US')

ALTER TABLE [dbo].[Netflix_Movies_and_TV_Shows]
ALTER COLUMN [date_added] date;
```

Only after that, these fields could be processed as dates.