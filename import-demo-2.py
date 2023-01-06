import os 

print('Original working directory is: ', os.getcwd())

absolute_path = 'Queries'
os.chdir(absolute_path)

print('New working directory is: ', os.getcwd())

import csv
 
# opening the CSV file
with open('transactions.csv', mode ='r')as file:
   
  # reading the CSV file
  csvFile = csv.reader(file)
 
  # displaying the contents of the CSV file
  for lines in csvFile:
        print(lines)