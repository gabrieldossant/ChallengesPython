import re
# Done with the ( FOR )

binaryNumber = input("Type a binary number: ")
binaryNumber = binaryNumber[::-1]
pattern = r'^[01]+$'
decimal = 0

if re.match(pattern, binaryNumber):
    for i in range(len(binaryNumber)):
        decimal += int(binaryNumber[i]) * (2 ** i)       
    print(f"The decimal result is {decimal}")
else:
    print("Invalid binary number!")
