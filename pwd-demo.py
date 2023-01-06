# Change the current working directory with os.chdir()
import os
cwd = os.getcwd()
print('Current Working Directory is: ', cwd)

absolute_path = 'Queries'
os.chdir(absolute_path)

print('New working directory is: ', os.getcwd())

# Returns:
# Current Working Directory is:  /Users/datagy
# New working directory is:  /Users/datagy/Documents