import pyarrow as pa
import pyarrow.parquet as pq


# Set the file paths for the two Parquet files you want to merge and what to create
file_path_1 = 'abc.parquet'
file_path_2 = 'def.parquet'

merged_file_path = 'abcdef.parquet'

# Read the two parquet files using pyarrow
table_1 = pq.read_table(file_path_1)
table_2 = pq.read_table(file_path_2)

# Combine the two tables using the concat_tables() method
merged_table = pa.concat_tables([table_1, table_2])

# Write the merged table to a new parquet file
pq.write_table(merged_table, merged_file_path)
