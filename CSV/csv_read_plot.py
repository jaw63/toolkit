import matplotlib.pyplot as plt
import pandas as pd

filename = 'file.csv'

# get data 
df = pd.read_csv(filename) 

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
