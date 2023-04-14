qtdNum = int(input("Digite uma quantidade de valores desejados para soma da equação: "))
i = 0
somaPositivo = 0
somaNegativo = 0

while i < qtdNum:
    numero = int(input(f"Digite {i} número: "))
    if(numero >= 0):
        somaPositivo += numero
    if(numero < 0):
        somaNegativo += numero
    i = i + 1

print(f"A soma dos valores positivos é igual a: {somaPositivo}")
print(f"A soma dos valores negativos é igual a: {somaNegativo}")
print("A soma dos valores positivos e negativos é igual a:", (somaNegativo + somaPositivo))