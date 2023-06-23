import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

# Path to the input Parquet file
input_file = 'filename.parquet'

# Path to the output Parquet file
output_file = 'output.parquet'

# Read the input Parquet file
table = pq.read_table(input_file)

# Convert Parquet table to pandas DataFrame
df = table.to_pandas()

# Add a new column with the company value
df['column'] = 'value'

# Convert pandas DataFrame back to Parquet table
table = pa.Table.from_pandas(df)

# Write the updated table to a new Parquet file
pq.write_table(table, output_file)
