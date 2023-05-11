num = int(input("Digite um número inteiro: "))
inversor = ""
soma = 0

for i in str(num):
    inversor = i + str(inversor)

soma_numeros = int(num) + int(inversor)

print(num)
print(inversor)
print(soma_numeros)
