# Practice:
#   • Download the Titanic or Netflix Movies dataset from Kaggle.
#   • Build a pivot_table: average age of passengers by class and gender.
#   • Use melt to reverse the table.

import pandas as pd
from pathlib import Path

# Load Titanic dataset
csv_file_path = Path(__file__).parent / 'W02_D4_P1_titanic_dataset.csv'

# Read the CSV file into a DataFrame
df = pd.read_csv(csv_file_path, sep=',', encoding='utf-8')

# Build a pivot_table: average age of passengers by class
print('\nPivot Table: Average Age of Passengers by Class:')
pivot_table = pd.pivot_table(df, index='Pclass', columns='Sex', values='Age', aggfunc='mean')
print(pivot_table.head())

# Use melt to reverse the table
print('\nReversed Table using Melt:')
unpivoted = pivot_table.reset_index().melt(id_vars=['Pclass'], value_vars=['male', 'female'])
print(unpivoted.head())