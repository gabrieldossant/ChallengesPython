import re

binaryValue = input("Type a binary number: ")
listCaracteres = list(binaryValue)
listCaracteres.reverse()
pattern = r'^[01]+$'

if re.match(pattern, binaryValue):
    print()
else:
    print("Invalid binary number! ")



