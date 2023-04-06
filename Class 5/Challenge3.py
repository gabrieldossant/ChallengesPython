'''
    Make a program in Python that asks the user for three distinct integers and
    and outputs the largest of them (disregarding the possibility that they are
    equal)
'''

n1 = int(input("Type a first number:"))
n2 = int(input("Type a second number:"))
n3 = int(input("Type a third number:"))

if n1 > n2 and n1 > n3:
    print(f"The first number typed is: {n1} ")
elif n2 > n1 and n2 > n3:
    print(f"The second number typed is: {n2}")
else:
    print(f"The third number typed is: {n3}")