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
