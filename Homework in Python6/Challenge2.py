valorCompra = float(input("Digite o valor da compra: "))
parcelas = int(input("Digite a quantidade de parcelas: "))

def verifica(x, y):
    if y == 0: 
        return print(f"Valor da compra a VISTA: {valorCompra}")
    elif y > 0:
        juros = x * 0.05
        total = x + juros
        return print(f'''
        Valor da compra é: {x}
        Parcelas: {y}
        Valor da compra com juros: {total}
        Valor da compra parcelada com juros: {total/y}''')
    
resultado = verifica(valorCompra, parcelas)