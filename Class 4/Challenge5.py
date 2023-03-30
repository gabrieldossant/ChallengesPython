'''
    Create a program in Python that asks for the gender of the user
    and tell it whether the user is male or female.
'''

sex = input("Type your sex:")
if sex.upper()[0] == "M":
    print("Your sex is Male.")
if sex.upper()[0] == "F":
    print("Your sex is Female.")
else:
    print("Unclassified")