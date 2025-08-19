"""
--------------------------
Path: week1_project/day7_project/day7_project.py
Date: 2025-08-19
Author: Semyon Kolosov
--------------------------
Day 7 — Mini-project in the portfolio
Project: ETL from CSV to DB
--------------------------
CSV source: Titanic or other dataset.
--------------------------
Python script:
    Reads CSV via Pandas.
    Cleans data (for example, replaces empty values).
    Loads into a table in the database (PostgreSQL or SQL Server).
--------------------------
Upload to GitHub:
    Folder with code.
    README with instructions.
    Screenshots of work.
--------------------------
"""

import pyodbc as cnn
import pandas as pd
from pathlib import Path

# Load the CSV file
csv_file_path = Path(__file__).parent / 'retail_product_dataset_with_missing_values.csv'
df = pd.read_csv(csv_file_path, sep=',', encoding='utf-8')

# Connect to the SQL Server database
conn = cnn.connect(
    "Driver={SQL Server};"
    "Server=Issetra\\Onenja;"  # My server name
    "Database=MyTestBase;"      # My database name
)

# Create a cursor object to execute SQL commands
crs = conn.cursor()

df.fillna({
    'Price': df['Price'].mean(),
    'Discount': df['Discount'].mean(),
    'Rating': df['Rating'].mean(),
    'Stock': 'Unknown',
    'Category': 'Unknown'
}, inplace=True)

# Create the RetailProducts table if it does not exist
crs.execute("""
     IF OBJECT_ID('dbo.RetailProducts', 'U') IS NULL
        CREATE TABLE RetailProducts (
            ProductID INT IDENTITY(1,1) PRIMARY KEY,
            Price FLOAT,
            Discount FLOAT,
            Rating FLOAT,
            Stock NVARCHAR(50),
            Category NVARCHAR(50)
    )
""")

# Clear the table before inserting new data
crs.execute("TRUNCATE TABLE RetailProducts")

# Insert data from the DataFrame into the RetailProducts table
for index, row in df.iterrows():
    crs.execute("""
        INSERT INTO RetailProducts (Price, Discount, Rating, Stock, Category)
        VALUES (?, ?, ?, ?, ?)
    """, row['Price'], row['Discount'], row['Rating'], row['Stock'], row['Category'])

# Commit the transaction
conn.commit()

# Select all rows from the RetailProducts table
crs.execute("SELECT * FROM RetailProducts")

# Print the results using a pyodbc cursor
for row in crs.fetchall():
    print(row)

# Close the cursor and connection
crs.close()
conn.close()

