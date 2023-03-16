'''
    Create a program in python that asks the user for the value in hours, 
    calculates and displays the value in minutes, knowing that 1 hour is 60 minutes.
'''
num = int(input(print(f'Type a time slot: ')))
addMinutes = 0
calculator = 1
while calculator <= num:
    calculator += 1
    addMinutes += 60
print(f"The value entered: {num} hours \nThe result in minutes: {addMinutes} minutes")