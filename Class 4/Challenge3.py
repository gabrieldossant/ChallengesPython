'''
    Create a program in Python that prompts the user for three
    values (A, B, and C) and checks whether the value stored in
    B is the smallest.
'''

n1 = int(input("Type your first number: "))
n2 = int(input("Type your second number: "))
n3 = int(input("Type your third number:"))

if n2 < n1 and n2 < n3:
    print(f"The number {n2} is the smallest typed")
else:
    print(f"The second number {n2} typed is not the least ")


