import sys
import traceback


try:
    raise Exception('This is an error message.')
except:
    errorFile = open('error_log.txt', 'a')
    errorFile.write(traceback.format_exc())
    errorFile.close()
    print(f'Traceback info written to {errorFile}')

def boxPrint(symbol, width, height):
    if len(symbol) != 1:
        raise Exception('Change the symbol to a string of length 1.')
    if (width <2) or (height < 2):
        raise Exception('Width and Height must be greater than or equal to 2')
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)

if len(sys.argv) != 4:
    print(f'You entered {sys.argv[1:]} as paramaters.\n Inter a single character, a width, and a height.\n You entered {len(sys.argv) - 1} paramaters.')
else:
    boxPrint(str(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
