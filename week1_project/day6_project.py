# Practice:
# Install PostgreSQL (or SQL Server Express).
# Create a table called passengers.
# From Python, write 5 rows of data there.

import pandas as pd
import pyodbc as cnn

# Connect to the SQL Server database
conn = cnn.connect(
    "Driver={SQL Server};"
    "Server=Issetra\Onenja;" # My server name
    "Database=MyTestBase;" # My database name
    )

# Create a cursor object to execute SQL commands
crs = conn.cursor()

# Create the passengers table, dropping it if it already exists
crs.execute(
    """
    DROP TABLE IF EXISTS passengers; 
    CREATE TABLE passengers (
            [PassengerID] [int] IDENTITY(1,1) NOT NULL,
	        [Passenger] [nvarchar](50) NOT NULL,
	        [DateRegistered] [date] NOT NULL,
        CONSTRAINT [PK_PassengerID] PRIMARY KEY CLUSTERED ([PassengerID] ASC)
    );
    """
    )

# Insert 5 rows of data into the passengers table
crs.execute("""
    INSERT INTO passengers (Passenger, DateRegistered)
    VALUES
        ('John Doe', '2023-10-01'),
        ('Jane Smith', '2023-10-02'),
        ('Alice Johnson', '2023-10-03'),
        ('Bob Brown', '2023-10-04'),
        ('Charlie White', '2023-10-05');
    """
    )
# Select all rows from the passengers table
crs.execute("""
    SELECT * FROM passengers;
    """
    )
# Print the results using a pyodbc cursor
for row in crs.fetchall():
    print (row)

# Print the table result using pandas
tableResult = pd.read_sql("""
    SELECT * FROM passengers;
    """, conn)
print(tableResult)