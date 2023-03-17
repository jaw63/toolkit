import csv

filename = 'file.csv'

# open CSV file
with open(filename, newline='') as csvfile:
    # create CSV reader object
    reader = csv.reader(csvfile)

    # count number of rows and columns
    num_rows = sum(1 for row in reader)
    csvfile.seek(0)
    num_cols = len(next(reader))

    # print number of rows and columns
    print("Number of rows: ", num_rows)
    print("Number of columns: ", num_cols)

    # print header row
    csvfile.seek(0)
    header = next(reader)
    print("Header: ", header)

    # print first few lines
    for i, row in enumerate(reader):
        if i < 5: # adjust the number of rows to print as needed
            print(row)
        else:
            break
