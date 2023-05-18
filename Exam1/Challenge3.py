somaPar = 0
qtdPar = 0
somaImpar = 0
qtdImpar = 0
qtd = 0
somaTotal = 0

for i in range(200):
    numero = float(input(f"Digite {i+1} número: "))
    num = numero % 2
    if num == 0:
        somaPar += numero
        qtdPar += 1
        somaTotal = somaPar + somaImpar
        qtd = qtd + 1
    else:
        somaImpar += numero
        qtdImpar += 1
        somaTotal = somaPar + somaImpar
        qtd = qtd + 1

    if qtdImpar == 3:
        print(f"A soma dos números pares: {somaPar}")
        print(f"Quantidade de números pares {qtdPar}")
        print(f"A soma dos números impares: {somaImpar}")
        print(f"Quantidade de números impares: {qtdImpar}")
        print(f"A soma dos números pares e impares: {somaTotal}")
        print(f"Quantidade de números digitados pelo usuário: {qtd}")
        exit()
