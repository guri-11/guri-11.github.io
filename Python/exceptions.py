import sys
try:
    x=int(input("x: "))
    y=int(input("y: "))
except ValueError:
    print("Error: Invalid input.")
    sys.exit(1)

try:
    result =x/y
except ZeroDivisionError:
    print("Error: Cannot Divide by 0.")
    sys.exit(1)

result =x/y
print ("%d/%d= %f" %(x,y,result))