# Faça um método que receba como parâmetros o Km inicial, Km
# final, quantidade de litros gastos e preço do litro. Calcule e mostre:
# - Distância percorrida;
# - Consumo médio;
# - Valor gasto;
# Faça um programa principal que solicite para o usuário o valor da
# quilometragem inicial, final, a quantidade de litros gastos e o preço
# do litro e mostre a distância percorrida, o consumo médio e o valor
# gasto, para isso utilize o método definido acima.

kmInicial = float(input("Digite a quilometragem inicial: "))
kmFinal = float(input("Digite a quilometragem final: "))
qtdLitros = float(input("Digite a quantidade de litros: "))
precoLitro = float(input("Digite o preço do litro: "))

def calculo(x, y, a, b):
    distancia = x - y
    consumoMedio = distancia / a
    valorGasto = a * b
    
    return print(f'''
    Distância percorrida: {distancia} Km
    Consumo médio: {consumoMedio} Km/L
    Valor gasto: {valorGasto} $
    ''')

resultado = calculo(kmInicial, kmFinal, qtdLitros, precoLitro)

