import sqlite3
import locale

class DbInit:
    def __init__(self):
        self.con = sqlite3.connect('inventory.db')
        self.cur = self.con.cursor()
        self.sqlite = self.cur.execute('select * from inventory')
        locale.setlocale(locale.LC_ALL, '')


class DbReport(DbInit):
    def __init__(self, Supplied_name, Supplied_order, Supplied_limit):
        super().__init__()
        self.Supplied_name = Supplied_name
        self.Supplied_order = Supplied_order
        self.Supplied_limit = Supplied_limit
        print(f"{Supplied_name : <10}{Supplied_order : ^25}{Supplied_limit : >10}")
        for i in self.cur.execute(f'select * from inventory where Supplier = "{Supplied_name}" order by "{Supplied_order}" DESC limit {Supplied_limit}'):
            ProdNo = i[0]
            Inventory = i[1]
            Price = i[2]
            Supplier = i[3]
            TotalCost = i[4]
            print(f"{ProdNo : <10}{Inventory : ^25}{TotalCost : >10}")
            #print(f'{Supplier} has spent a total {(locale.currency(TotalCost, grouping = True))} buying Product #: {ProdNo}')
        Accumulate = 0.0
        for i in self.cur.execute(f'select * from inventory where Supplier = "{Supplied_name}" order by "{Supplied_order}" DESC limit {Supplied_limit}'):
            Accumulate = Accumulate + float(i[4])
        print(f"{'That is a total of '} {(locale.currency(Accumulate, grouping = True)) : >25}")



#DbInit(ByCompany('Company AAA'))
DbReport('Company AAA', 'Inventory', '5')
#DbInit(ByCompany('CC Company CC'))
#DbInit('BBB Company')
#DbInit('CC Company CC')



