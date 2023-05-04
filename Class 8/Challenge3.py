n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
escolha = input("Escolha a operação (+) (-) (*) (/)")

def calculator(esc, x, y):
    if esc == "+":
        return print(f"O resultado da soma é {x+y}")
    elif esc == "-":
        return print(f"O resultado da subtração é {x-y}")
    elif esc == "*":
        return print(f"O resultado da multiplicação é {x*y}")
    elif esc == "/":
        return print(f"O resultado da divisão é {x/y}")
    else:
        return print("ERRO! Operação digitada incorreta!")

calculator(escolha, n1, n2)
