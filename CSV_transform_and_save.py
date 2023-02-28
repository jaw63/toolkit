import pandas as pd 

# read the CSV file into a pandas DataFrame
filename = 'file.csv'
df = pd.read_csv(filename)

# truncate date
df['ts'] = df['ts'].str[:10]

# truncate description
df['descr_trunc'] = df['descr'].str[:23]

# create a pivot table with counts of descr
pivot_table = pd.pivot_table(df, index='descr_trunc', values='person_id', aggfunc='count')

# sort the pivot table by counts in descending order
sorted_pivot_table = pivot_table.sort_values(by=['person_id'], ascending=False)

# print part of the sorted pivot table
print(sorted_pivot_table.head()) 
#print(sorted_pivot_table[:20]) 

# save the modified DataFrame as a new CSV file
df.to_csv('asstfin_v2.csv', index=False)

# save the pivot table as a new CSV file
sorted_pivot_table[:15].to_csv('asstfind_pivot.txt')
