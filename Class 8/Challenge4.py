n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
escolha = int(input('''Escolha a operação
[ 1 ] Soma
[ 2 ] Subtração
[ 3 ] Multiplicação
[ 4 ] Divisão'''))

def calculator(esc, x, y):
    if esc == 1:
        return summ(x, y)
    elif esc == 2:
        return sub(x, y)
    elif esc == 3:
        return mult(x, y)
    elif esc == 4:
        return div(x, y)
    else:
        return print("Erro! Número digitado incorreto!")

def summ(x, y):
    r = x + y
    return r

def sub(x, y):
    r = x - y
    return r

def mult(x, y):
    r = x * y
    return r

def div(x, y):
    r = x / y
    return r

print(calculator(escolha, n1, n2))