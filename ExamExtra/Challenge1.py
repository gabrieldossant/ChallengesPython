# Nome: Gabriel dos Santos Silva
# RGM: 33210268
# Período: Noturno

contM = 0
contF = 0
somaMasc = 0
somaFem = 0
i = 1

while i < 100:
    nome = input(f"{i} - Digite o seu nome: ")
    sexo = input(f"{i} - Qual o seu genêro [M/F]: ")
    idade = int(input(f"{i} - Digite sua idade: "))

    if sexo.upper()[0] == "F":
        somaFem = somaFem + idade
        contF = contF + 1
        i = i + 1
    
    if sexo.upper()[0] == "M":
        somaMasc = somaMasc + idade
        contM = contM + 1
        i = i + 1

    if contM == 5:
        mediaM = somaMasc/contF
        mediaF = somaFem/contM
        print(f"A média das idades do sexo masculino é {mediaM}")
        print(f"A média das idades do sexo feminino é {mediaF}")
        print(f"A soma das idades do sexo masculino e feminino é {somaMasc + somaFem}")
        exit()

