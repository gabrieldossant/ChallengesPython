'''
    Create a program in python that asks the user for his age expressed in years, 
    months and days (separate variables). Calculate and display the age expressed 
    in days. For this consider 1 year = 365 days, 1 month = 30 days.
'''

yearBirth = int(input(print("Type your year of birth: ")))
mouthBirth = int(input(print("Type your mouth of birth: ")))
dayBirth = int(input(print("Type your day of birth: ")))
currentYear = 2023
age = currentYear - yearBirth
totaldays = (age * 365)

print(f"Your date of birth is {dayBirth}/{mouthBirth}/{yearBirth}\nYour current age is {age}\nYour total days added together is {totaldays}")