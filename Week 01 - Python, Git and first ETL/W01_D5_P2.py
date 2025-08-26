# 📌 Task:
# Find any small CSV file with data (you can use Kaggle, data.gov, or simply export it to CSV from Excel/Google Sheets).
# Open it with pd.read_csv().
# Do:
#   Print the total number of rows and columns.
#   Determine if there are gaps (NaN) in the data and in which columns they occur.
#   Fill the gaps in the numeric columns with the average value, and in the text columns with the string "Unknown".
#   Sort the data by one numeric column (ascending).
#   Print the 5 largest values in another numeric column.
#   Save the processed data to a new CSV file processed.csv.

import pandas as pd
from pathlib import Path

csv_file_path = Path(__file__).parent / 'W01_D5_P2_retail_product_dataset_with_missing_values.csv'

df = pd.read_csv(csv_file_path, sep=',', encoding='utf-8')

# Print the total number of rows and columns
date_info = {
    'count_rows': df.shape[0], 
    'count_columns': df.shape[1],
}
print(f"\nTotal number of rows: {date_info['count_rows']}")
print(f"Total number of columns: {date_info['count_columns']}")

print()

# Determine if there are gaps (NaN) in the data and in which columns they occur
for column in df.columns:
    if df[column].isnull().any():
        null_count = df[column].isnull().sum()
        print(f"Column '{column}' has {null_count} NaN values.")
    else:
        print(f"Column '{column}' has no NaN values.")

# Fill the gaps in the numeric columns with the average value,
# and in the text columns with the string "Unknown"
if df.isnull().values.any():
    df.fillna({
        'Price': df['Price'].mean(),
        'Discount': df['Discount'].mean(),
        'Rating': df['Rating'].mean(),
        'Stock': 'Unknown',
        'Category': 'Unknown'
    }, inplace=True)

print()

# Print the 5 largest values in another numeric column
for column in df.select_dtypes(include=['float64', 'int64']).columns:
    print(f"5 largest values in column '{column}':")
    print(df[column].nlargest(5))

print()

# Sort the data by one numeric column (ascending)
df.sort_values(by='Price', ascending=True, inplace=True)

print(df.head())

# Save the processed data to a new CSV file processed.csv
output_file_path = Path(__file__).parent / 'W01_D5_P2_processed.csv'
df.to_csv(output_file_path, index=False)
