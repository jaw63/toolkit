import matplotlib.pyplot as plt
import pandas as pd
import os  

# change to correct directory
absolute_path = 'Queries'
os.chdir(absolute_path)

# get data 
df = pd.read_csv('right3name.csv') 

x=df['digit']
y=df['count']

plt.figure()

# plot data
plt.bar(x, y, color="pink", width=0.9) 

# tweak
plt.yscale('log')

# labels
plt.xlabel("###")
plt.ylabel("Count of occurrences")
plt.title("Distribution, last three digits") 

plt.show()
