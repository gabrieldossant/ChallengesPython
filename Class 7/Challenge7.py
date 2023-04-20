import math

'''
    Maria estava fazendo a sua lição de casa queprecisava calcular o valor 
    da hipotenusa de umtriângulo e teve a ideia de montar um algoritmo
    (fluxograma) que faça isso mediante o valor doscatetos do triângulo. 
    Como será esse algoritmo?Utilize o seu conhecimento em abstração, 
    algoritmo edecomposição de problemas
'''

catet1 = float(input("Enter the value of the first catet: "))
catet2 = float(input("Enter the value of the second catet: "))

hipotenusa = math.sqrt(catet1**2 + catet2**2)

print(f"The result of the hipotenusa is {hipotenusa}")