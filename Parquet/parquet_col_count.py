import pyarrow.parquet as pq

# Get filename
filename = input("parquet filename? ")
filename  = "{}{}".format(filename, ".parquet")

# Open the Parquet file
parquet_file = pq.ParquetFile(filename)

# Get the number of rows and columns
num_rows = parquet_file.metadata.num_rows
num_cols = len(parquet_file.schema)

# Print the dimensions
print(f"Number of rows: {num_rows}")
print(f"Number of columns: {num_cols}")

# Print the first few lines
table = pq.read_table(filename)
first_four_rows = table.slice(0, 4)
df = first_four_rows.to_pandas()
print(df)
