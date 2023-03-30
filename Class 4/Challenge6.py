'''
    Make a program that prompts the user for an integer
    and calculate and display the square root of that number. O
    should first check if the number entered is
    positive, displaying a warning message if it is negative.
'''

import math

value = float(input("Type a number: "))

if value < 0:
    print("The result is negative ")
else:
    print("The result is positive: ", math.sqrt(value))