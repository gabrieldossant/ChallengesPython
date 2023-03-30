'''
    Make a program that receives the integer number of the license plate of a
    verify and print which day of the week the day of the week the vehicle cannot
    circulate in the "Expanded Center".
'''

plateDigit = int(input("Enter a number: [ 0 / 9]"))

if plateDigit == 1 or plateDigit == 2:
    print("You cannot circulate on (MONDAY)")
elif plateDigit == 3 or plateDigit == 4:
    print("You cannot circulate on (TUESDAY)")
elif plateDigit == 5 or plateDigit == 6:
    print("You cannot circulate on (WEDNESDAY)")
elif plateDigit == 7 or plateDigit == 8:
    print("You cannot circulate on (THURSDAY)")
elif plateDigit == 9 or plateDigit == 0: 
    print("You cannot circulate on (FRIDAY)")
else:
    print("Invalid typed number!")