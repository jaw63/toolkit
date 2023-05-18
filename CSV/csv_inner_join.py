import pandas as pd
import csv

# inputs
file1 = 'file1.csv'
file2 = 'file2.csv'
common_column = '[column_name]'

# define column count function
def col_count(file):
    with open(file, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        
        # Count the number of rows
        row_count = sum(1 for row in csvreader)
        
        # Reset the file pointer to the beginning of the file
        csvfile.seek(0)
        
        # Count the number of columns in the first row
        col_count = len(next(csvreader))
        
        # Print the row and column counts
        print(f"For {file}....")
        print(f"Number of rows: {row_count}")
        print(f"Number of columns: {col_count}")

# Load the CSV files into pandas DataFrames
df1 = pd.read_csv(file1)
df2 = pd.read_csv(file2)

col_count(file1)
col_count(file2)

# Convert the column data types just in case (can likely be deleted)
df2[common_column] = df2[common_column].astype(str)
df1[common_column] = df1[common_column].astype(str)

# Perform inner join on common columns
result = pd.merge(df1, df2, on=common_column, how='inner')

# Save the result to a new CSV file
result.to_csv('joined.csv', index=False)

col_count(f'joined.csv')
    
