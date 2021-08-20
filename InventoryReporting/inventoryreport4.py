import sqlite3
import locale



class DbInit:
    def __init__(self):
        self.con = sqlite3.connect('inventory.db')
        self.cur = self.con.cursor()
        locale.setlocale(locale.LC_ALL, '')


class DbTotalCost(DbInit):
    def __init__(self, Supplied_order, Supplied_dir, Supplied_limit):
        super().__init__()
        print(f"{'Supplier' : <20}{'Inventory' : ^20}{'TotalCost' : >10}{'SerialNo' : >10}")
        print(f'---------------------------------------------------------------')
        Accumulate = 0.0
        for i in self.cur.execute("SELECT * FROM Inventory ORDER BY "+Supplied_order+" "+Supplied_dir+" LIMIT "+Supplied_limit+""):
            Inventory = i[1]
            Price = i[2]
            Supplier = i[3]
            TotalCost = i[4]
            SerialNo = i[5]
            print(f'{Supplier : <20} {Inventory : ^20} {(locale.currency(TotalCost, grouping = True)) : >10} {SerialNo : >10}')
            Accumulate = Accumulate + float(i[4])
        print(f"{'That is a total of '} {(locale.currency(Accumulate, grouping = True)) : >25}")
        print(f'--------------------------------------------------------------')

class DbInventory(DbInit):
    def __init__(self, Supplied_order, Supplied_dir, Supplied_limit):
        super().__init__()
        print(f"{'Supplier' : <20}{'Inventory' : ^20}{'Price' : ^15}{'SerialNo' : >10}")
        print(f'---------------------------------------------------------------')
        for i in self.cur.execute("SELECT * FROM Inventory ORDER BY "+Supplied_order+" "+Supplied_dir+" LIMIT "+Supplied_limit+""):
            Inventory = i[1]
            Price = i[2]
            Supplier = i[3]
            TotalCost = i[4]
            SerialNo = i[5]
            print(f'{Supplier : <20} {Inventory : ^20} {(locale.currency(Price, grouping = True)) : >10} {SerialNo : >10}')
        print(f'---------------------------------------------------------------')
        
        
class DbPrice(DbInit):
    def __init__(self, Supplied_order, Supplied_dir, Supplied_limit):
        super().__init__()
        print(f"{'Supplier' : <20}{'Inventory' : ^20}{'Price' : >10}{'SerialNo' : >10}")
        print(f'---------------------------------------------------------------')
        for i in self.cur.execute("SELECT * FROM Inventory ORDER BY "+Supplied_order+" "+Supplied_dir+" LIMIT "+Supplied_limit+""):
            Inventory = i[1]
            Price = i[2]
            Supplier = i[3]
            TotalCost = i[4]
            SerialNo = i[5]
            print(f'{Supplier : <20} {Inventory : ^20} {(locale.currency(Price, grouping = True)) : >10} {SerialNo : >10}')
        print(f'---------------------------------------------------------------')


DbInventory('Inventory', 'ASC', '10')
DbPrice('Price', 'DESC', '15')
DbInventory('SerialNo', 'DESC', '10')
DbTotalCost('TotalCost', 'DESC', '10')


