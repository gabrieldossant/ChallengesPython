n1 = float(input("Type the first number: "))
n2 = float(input("Type the second number: "))
choose = int(input("Choose the operator: [1/4]"))

def verifyChoose(number, x, y):
    if number == 1:
        total = (x + y)/2
        return total
    elif number == 2:
        if x > y:
            return print(f"The first number typed {x} is biggest than second number typed {y}.")
        elif x < y:
            return print(f"The second number typed {y} is biggest than first number typed {x}.")
        else:
            return print(f"The two numbers typed is are equal.")
    elif number == 3:
        total = x * y
        

result = verifyChoose(choose, n1, n2)