import pyarrow.parquet as pq
import pandas as pd

# Specify the path to the Parquet file
parquet_file = 'file.parquet'

# Read the Parquet file into a PyArrow Table
table = pq.read_table(parquet_file)

# Convert the PyArrow Table to a Pandas DataFrame
df = table.to_pandas()

# Specify the path and filename for the CSV file
csv_file = 'file.csv'

# Write the Pandas DataFrame to a CSV file
df.to_csv(csv_file, index=False)
