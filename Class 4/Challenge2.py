'''
    Write a program in Python that asks the user for an integer
    number from the user and display it if it is even
'''

n1 = int(input("Type a number: "))
n2 = n1 % 2
if n2 == 0:
    print("Your number is par!")
else:
    print("Your number is impar")
