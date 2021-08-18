print("Enter 2 numbers:")
a=float(input())
b=float(input())

print("What would you like to perform?")
print("Choose among the following options:")
print("Enter 1 for Addition, 2 for Subtraction, 3 for Multiplication, 4 for Division")
c=int(input())
if c==1:
    output=a+b
elif c==2:
    output=a-b
elif c==3:
    output=a*b
elif c==4:
    output=a/b   
print(output) 
