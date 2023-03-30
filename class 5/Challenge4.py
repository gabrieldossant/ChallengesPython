'''
    Create a program in Python that asks the user for his weight and height and
    calculate the Body Mass Index: BMI= weight/height²
'''

weight = float(input("Type your weight: "))
height = float(input("Type your height: "))
imc = (weight/(height*height))

if imc < 20:
    print(f"Underweight, IMC: {imc}")
elif imc >= 20 and imc < 25:
    print(f"Normal weight, IMC: {imc}")
elif imc >= 25 and imc < 30:
    print(f"overweight, IMC: {imc}")
elif imc >= 30 and imc < 40:
    print(f"Obese, IMC: {imc}")
else:
    print(f"Morbidly obese, IMC: {imc}")