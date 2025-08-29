# This script imports a CSV file into a SQL Server database table using pandas and pyodbc.
# I will import three datasets:
#   • W02_D6_netflix_movies_and _tv_shows.csv
#   • W02_D6_superstore_dataset.csv
#   • W02_D6_titanic.csv

import pandas as pd # For data manipulation
import pyodbc as cnn # For connecting to SQL Server
from pathlib import Path # For handling file paths
import math # For rounding up string lengths
import chardet # For detecting file encoding

# Dictionary of csv files and their corresponding table names
datasets = {
    "W02_D6_netflix_movies_and _tv_shows.csv": "Netflix_Movies_and_TV_Shows",   
    "W02_D6_superstore_dataset.csv": "Superstore_Dataset",
    "W02_D6_titanic.csv": "Titanic"
}

# Define dunction to read CSV file into a pandas DataFrame
def read_csv_to_df(file_path, csv_code_page):
    df = pd.read_csv(file_path, encoding=csv_code_page)
    return df

# Define function to map pandas dtypes to SQL Server data types
def map_dtype(col, dtype, df):
    if pd.api.types.is_integer_dtype(dtype):
        return "INT"
    elif pd.api.types.is_float_dtype(dtype):
        return "FLOAT"
    elif pd.api.types.is_bool_dtype(dtype):
        return "BIT"
    elif pd.api.types.is_datetime64_any_dtype(dtype):
        return "DATETIME"
    elif pd.api.types.is_object_dtype(dtype) or pd.api.types.is_string_dtype(dtype):
        max_len = df[col].astype(str).map(len).max()
        rounded_len = int(math.ceil(max_len / 10.0)) * 10
        return f"NVARCHAR({rounded_len})"
    else:
        return "NVARCHAR(MAX)"

# Connect to the SQL Server database
conn = cnn.connect(
    "Driver={SQL Server};"
    "Server=Issetra\Onenja;" # My server name
    "Database=MyTestBase;" # My database name
)

# Create a cursor object to execute SQL commands
crs = conn.cursor()

# Iterate over the datasets and import each one
for csv_file, table_name in datasets.items():
    print(f"\nImporting \"{csv_file}\" into table \"{table_name}\"...")

    # Define the path to the CSV file
    file_path = Path(__file__).parent / csv_file

    with open(file_path, "rb") as f:
        csv_code_page = chardet.detect(f.read(5000))  # Detect the file encoding

    # Read the CSV file into a DataFrame
    df = read_csv_to_df(file_path, csv_code_page["encoding"])

    # Drop the table if it already exists
    crs.execute(f"IF OBJECT_ID('{table_name}', 'U') IS NOT NULL DROP TABLE {table_name};")
    conn.commit()

    # Generate and execute the CREATE TABLE statement based on the DataFrame's columns and dtypes
    columns_with_types = ", ".join(
        [f"[{col}] {map_dtype(col, dtype, df)}" for col, dtype in zip(df.columns, df.dtypes)]
    )
    print(f"\tCreating table {table_name} with columns: {columns_with_types}")
    create_table_query = f"CREATE TABLE {table_name} ({columns_with_types});"
    crs.execute(create_table_query)
    print("\t...done.")

    print("\tFilling NaN values with None for SQL Server compatibility...")

    # Fill NaN values with None for SQL Server compatibility
    df = df.where(pd.notnull(df), None)

    # Replacing NaN values in integer columns with 0
    for col, dtype in zip(df.columns, df.dtypes): 
        if pd.api.types.is_integer_dtype(dtype):
            df[col] = df[col].fillna(0)
        elif pd.api.types.is_float_dtype(dtype):
            df[col] = df[col].fillna(0.0)
        else:
            df[col] = df[col].where(pd.notnull(df[col]), None)

    # Replacing NaN values in string columns with NULL
    for col, dtype in zip(df.columns, df.dtypes):
        if pd.api.types.is_object_dtype(dtype) or pd.api.types.is_string_dtype(dtype):
            df[col] = df[col].where(pd.notnull(df[col]), None)

    print("\t...done.")

    print("\tInserting data into the SQL Server table...")

    # Insert data into the SQL Server table
    for index, row in df.iterrows():
        placeholders = ", ".join(["?"] * len(row))
        insert_query = f"INSERT INTO {table_name} VALUES ({placeholders})"
        crs.execute(insert_query, tuple(row))
        if index % 100 == 0:
            conn.commit()  # Commit every 100 rows for efficiency

    conn.commit()  # Final commit
    print("\t...done.")
    print(f"\tImported {len(df)} rows into \"{table_name}\".")

print("\nAll datasets have been imported successfully.")
# Close the cursor and connection
crs.close()
conn.close()
