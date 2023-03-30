'''
     
'''

media = float(input("Enter your media: "))
frequency = float(input("Enter your frequency: "))

if frequency < 75:
    print("Reproved")
else:
    if media < 6:
        print("Reproved by note")
    else:
        print("Aproved")