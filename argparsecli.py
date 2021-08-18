import sys

print(type(sys.argv))
print('The CLI args are: ')
for i in sys.argv:
    print(i)