import csv
with open('sales.csv','r') as f:
    reader = csv.reader(f)
    header = next(reader)
    row_idx = 0
    col_idx = 0
    max_table = -1# float('-inf')
    r = 1
    for row in reader:
        for i in range(1,len(row)-1):
            if float(row[i])>max_table:
                col_idx = i
                row_idx = r
                max_table = float(row[i])

        r += 1
    print('Maximum sale:',max_table,'Quarter:',row_idx,'Product:',header[col_idx])