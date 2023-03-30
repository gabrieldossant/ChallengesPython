'''
    Create an algorithm that reads the age of a person and tells his electoral class:
    * non-voter (under 16).
    * compulsory voter (between the ages of 18 and 65)
    * optional voter (between 16 and 18 years old and over 65 years old)
'''
age = int(input("Enter your age to find out your electoral class: "))

if age < 16:
    print("Non-elector")
elif age > 18 and age <= 65:
    print("Required-elector")
elif age >= 16 and age <= 18 and age > 65:
    print("Facultative-elector")
    