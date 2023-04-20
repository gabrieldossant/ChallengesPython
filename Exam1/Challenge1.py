'''
    Nome: Gabriel dos Santos Silva
    RGM: 33210268
    Noturno
'''
somaPar = 0
qtdPar = 0
somaImpar = 0
qtdImpar = 0
qtd = 0
somaTotal = 0

valor = int(input("Digite uma quantidade de números: "))
for i in range(valor):
    numero = float(input(f"Digite {i+1} número: "))
    num = numero % 2
    c = +i
    qtd = +i
    if num == 0:
        somaPar += numero
        qtdPar += 1
        somaTotal = somaPar + somaImpar
    else:
        somaImpar += numero
        qtdImpar += 1
        somaTotal = somaPar + somaImpar

    if qtdImpar == 3:
        if qtd < i:
            qtd = +i
        print(f"A soma dos números pares: {somaPar}")
        print(f"Quantidade de números pares {qtdPar}")
        print(f"A soma dos números impares: {somaImpar}")
        print(f"Quantidade de números impares: {qtdImpar}")
        print(f"A soma dos números pares e impares: {somaTotal}")
        print(f"Quantidade de números digitados pelo usuário: {qtd}")
        exit()


if qtd < i:
    qtd = +i
somaTotal = somaPar + somaImpar
print(f"A soma dos números pares: {somaPar}")
print(f"Quantidade de números pares {qtdPar}")
print(f"A soma dos números impares: {somaImpar}")
print(f"Quantidade de números impares: {qtdImpar}")
print(f"A soma dos números pares e impares: {somaTotal}")
print(f"Quantidade de números digitados pelo usuário: {qtd}")

