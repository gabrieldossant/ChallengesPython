print(f"ESCOLHA O CÁLCULO QUE DESEJA FAZER")
print(f"1 - QUADRADO\n2 - TRIÂNGULO\n3 - RETÂNGULO\n4 - TRAPÉZIO\n5 - PENTÁGONO\n6 - HEXÁGONO")
escolha = int(input("Digite um número de [1/6]:"))

if escolha == 1:
    lado = float(input("Digite o valor do lado do quadrado: "))
    area = lado ** 2
    print(f"A área do quadrado é {area}.")
elif escolha == 2:
    base = float(input("Digite o valor da base do triângulo: "))
    altura = float(input("Digite o valor da altura do triângulo: "))
    area = (base * altura)/2
    print(f"A área do triângulo é {area}")
elif escolha == 3:
    comprimento = float(input("Digite o valor do comprimento do retângulo: "))
    largura = float(input("Digite o valor da largura do retângulo: "))
    area = comprimento * largura
    print(f"A área do retângulo é {area}.")
elif escolha == 4:
    baseMaior = float(input("Digite o valor da base maior do Trapézio: "))
    baseMenor = float(input("Digite o valor da base menor do Trapézio: "))
    altura = float(input("Digite o valor da altura do Trapézio: "))
    area = ((baseMaior + baseMenor) * altura)/2
    print(f"A área do trapézio é {area}.")
elif escolha == 5:
    lado = float(input("Digite o valor do lado do pentágono: "))
    area = (5 / 4) * (lado ** 2) * (1 / ((5 ** 0.5 + 1) / 2))
    print(f"A área do pentagono é {area}")
elif escolha == 6:
    lado = float(input("Digite o valor do lado do hexágono: "))
    area = (3 * (3 ** 0.5) * lado ** 2) / 2
    print(f"A área do hexágono é {area}")
else:    
    print("Numéro inválido! Digite os números dentro do limite.")