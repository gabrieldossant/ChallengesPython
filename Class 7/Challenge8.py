n1 = float(input("Type the first number: "))
n2 = float(input("Type the second number: "))
print(" 1 - Average among the numbers entered\n 2 - Difference from highest to lowest\n 3 - Product of the two numbers entered\n 4 - First divided by second")
choose = int(input("Choose the [1/4] operator: "))

def verifyChoose(number, x, y):
    if number == 1:
        total = (x + y)/2
        return print(f"The result of the average is {total}.")
    elif number == 2:
        if x > y:
            return print(f"The first number typed {x} is biggest than second number typed {y}.")
        elif x < y:
            return print(f"The second number typed {y} is biggest than first number typed {x}.")
        else:
            return print(f"The two numbers typed is are equal.")
    elif number == 3:
        total = x * y
        return print(f"The first product typed is {x} \n The second product typed is {y} \n The total = {total}")
    elif number == 4:
        total = x / y
        return print(f"The result of the division of the first by the second is {total}.")
    else:
        print(f"Invalid number!")
        

result = verifyChoose(choose, n1, n2)