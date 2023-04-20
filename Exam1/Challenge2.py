clientes = 5
faturamento = 54000
somaVenda = 0

for i in range(clientes):
    vendaCliente = int(input(f"Digite o {i+1} cliente: "))
    somaVenda = somaVenda + vendaCliente

if somaVenda > faturamento:
    resto = (somaVenda - faturamento)
    divisao = resto/faturamento
    resultado = divisao * 100
    print(f"O valor ultrapassou o limite do faturamento! \n Faturamento: {faturamento} Soma de vendas: {somaVenda}")
    print(f"A porcentagem ultrapassada da matriz é %{resultado.__round__(2)}")
else:
    print("Não ultrapassou a matriz")