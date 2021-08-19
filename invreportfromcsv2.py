import csv
from os import read


class doWork:
    def __init__(self, inputfile, outputfile):
        self.inputfile = inputfile
        self.outputfile = outputfile
        print(f'Input file is {self.inputfile}, and output file is {self.outputfile}.')
    
    def combine(self):
        with open(self.inputfile, newline='') as inv_file:
            f = csv.reader(inv_file)
            output = list(f)
            
        with open(self.outputfile, 'w') as out_file:
            w = csv.writer(out_file, delimiter=',')
            w.writerow(['ProdNo', 'Inventory', 'Price', 'Supplier', 'TotalCost'])
            for i in range(1, len(output)):
                total_cost = round(float(output[i][1]) * float(output[i][2]), 2)
                w.writerow([output[i][0], output[i][1], output[i][2], output[i][3], total_cost])

p = doWork("inventoryreport.csv", "testreport.csv")
p.combine()
