
'''
    Make a program in Python that asks for a code referring to the type of
    and also the number of nights that a customer wants.
    desired by a customer. Calculate and show, using nested conditional structure, the total amount
    pay by the customer, according to the table below:
'''

typeOfDaily = input("Enter a type daily of hosting: ")
quantyOfDaily = float(input("Enter quanty of daily: "))

if typeOfDaily.upper()[0] == "S":
    print(f"Your value of daily is : {255,50 * quantyOfDaily}")
elif typeOfDaily.upper()[0] == "D":
    print(f"Your value of daily is : {305,50 * quantyOfDaily}")
elif typeOfDaily.upper()[0] == "T":
    print(f"Your value of daily is {360,50}")
else:
    print("Type of hosting is invalid!")