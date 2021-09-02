import openpyxl

def main():

    wb = openpyxl.Workbook()
    ws1 = wb.create_sheet('MySheet', 0)

    ws1['A1'] = 42
    ws1['A2'] = 'Hello World'
    ws1['B1'] = 12
    ws1['C1'] = '=(A1 + B1)'

    wb.save('myworkbook2.xlsx')
    wb.close()

if __name__ == '__main__':
    main()
