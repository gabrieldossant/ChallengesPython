reply = int(input(f'Type 1 to calculate the perimeter \nType 2 to calculate the area'))

def checkAwnser():
    if reply == 1:
        calculatePerimeter()
    elif reply == 2:
        calculateArea()

def calculatePerimeter():
    first_Side = int(input(print(f'Inform the value of the first side:')))
    second_Side = int(input(print(f'Inform the value of the second side: ')))
    third_Side = int(input(print(f'Inform the value of the third side: ')))
    perimeter = (first_Side + second_Side + third_Side)
    print(f'The value of the perimeter is {perimeter}')
def calculateArea():
    base = int(input(print(f'Enter the base value: ')))
    height = int(input(print(f'Enter the height value: ')))
    area = (base * height)/2
    print(f'The value of the area is {area}')

checkAwnser()


