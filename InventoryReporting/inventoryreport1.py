import csv

with open('inventoryreport.csv') as inv_file:
    with open('testreport.csv', 'w') as out_file:
        f = csv.reader(inv_file, delimiter=',')
        w = csv.writer(out_file, delimiter=',')
        output = list(f)
        w.writerow(['ProdNo', 'Inventory', 'Price', 'Supplier', 'TotalCost'])

        for i in range(1, len(output)):
            total_cost = round(float(output[i][1]) * float(output[i][2]), 2)
            w.writerow([output[i][0], output[i][1], output[i]
                       [2], output[i][3], total_cost])
