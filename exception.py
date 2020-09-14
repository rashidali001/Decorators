import sys
try:
    x=int(input("x:"))
    y=int(input("y:"))

except ValueError:
    print("Error!Didnt enter a number")
    sys.exit(1)

try:
    result=x/y
except ZeroDivisionError:
    print("Error!cant divide by zero")
    sys.exit(1)

print(f"{x}/{y} is {result}")