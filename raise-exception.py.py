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
        raise Exception('Change the symbol to a strength of length 1.')
    if (width <2) or (height < 2):
        raise Exception('Width and Height must be greater than or equal to 2')
    print(symbol * width)
    for i in range(height - 2):
        print(symbol + (' ' * (width - 2)) + symbol)
    print(symbol * width)


boxPrint('O', 10, 10)
