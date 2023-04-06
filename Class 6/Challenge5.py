valor_binario = "1111"

# Converte a string em uma lista de caracteres e inverte a ordem dos caracteres
lista_caracteres = list(valor_binario)
lista_caracteres.reverse()

# Converte cada caractere em um número inteiro
lista_numeros = [int(caractere) for caractere in lista_caracteres]

print(lista_numeros)
