import pyarrow as pa
import pyarrow.parquet as pq
import pandas as pd

# Specify the path to the CSV file
csv_file = 'file.csv'

# Read the CSV file into a Pandas DataFrame
df = pd.read_csv(csv_file)

# Convert the Pandas DataFrame to a PyArrow Table
table = pa.Table.from_pandas(df)

# Specify the path and filename for the Parquet file
parquet_file = 'file.parquet'

# Write the PyArrow Table to a Parquet file
pq.write_table(table, parquet_file)
