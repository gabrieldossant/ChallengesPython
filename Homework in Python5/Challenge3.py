# Done without the ( FOR )
import re

binaryValue = input("Type a binary number: ")
pattern = r'^[01]+$'

if re.match(pattern, binaryValue):
    decimal = int(binaryValue, 2)
    print(decimal)
else:
    print("Invalid binary number! ")