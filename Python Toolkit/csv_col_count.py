import csv

with open('filename.csv', 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    
    # Count the number of rows
    row_count = sum(1 for row in csvreader)
    
    # Reset the file pointer to the beginning of the file
    csvfile.seek(0)
    
    # Count the number of columns in the first row
    col_count = len(next(csvreader))
    
    # Print the row and column counts
    print(f"Number of rows: {row_count}")
    print(f"Number of columns: {col_count}")
