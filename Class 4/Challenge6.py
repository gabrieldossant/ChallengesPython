import math

value = float(input("Type a number: "))

if value < 0:
    print("The result is negative ")
else:
    print("The result is positive: ", math.sqrt(value))