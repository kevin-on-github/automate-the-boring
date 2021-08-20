import sqlite3
import locale


def dblookup(Supplied_name):
    con = sqlite3.connect('inventory.db')
    cur = con.cursor()
    sqlite = cur.execute('select * from inventory')
    locale.setlocale(locale.LC_ALL, '')
    for i in cur.execute(f'select * from inventory where Supplier = "{Supplied_name}"'):
        ProdNo = i[0]
        Inventory = i[1]
        Price = i[2]
        Supplier = i[3]
        TotalCost = i[4]
        print(f'{Supplier} has spent a total {(locale.currency(TotalCost, grouping = True))} buying Product #: {ProdNo}')
    Accumulate = 0.0
    for i in cur.execute(f'select * from inventory where Supplier = "{Supplied_name}"'):
        Accumulate = Accumulate + float(i[4])
    print(f"{'That is a total of '} {(locale.currency(Accumulate, grouping = True)) : >25}")

dblookup('Company AAA')
dblookup('BBB Company')
dblookup('CC Company CC')



