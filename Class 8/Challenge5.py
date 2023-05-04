weight = float(input("Type your weight: "))
height = float(input("Type your height: "))

def calculatorIMC(x, y):
    i = (x/(y*y))
    if i < 20:
        print(f"Underweight, IMC: {i}")
    elif i >= 20 and i < 25:
        print(f"Normal weight, IMC: {i}")
    elif i >= 25 and i < 30:
        print(f"overweight, IMC: {i}")
    elif i >= 30 and i < 40:
        print(f"Obese, IMC: {i}")
    else:
        print(f"Morbidly obese, IMC: {i}")

calculatorIMC(weight, height)