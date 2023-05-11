import soma
import subtracao
import mult
import div

n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
escolha = int(input('''Escolha a operação
[ 1 ] Soma
[ 2 ] Subtração
[ 3 ] Multiplicação
[ 4 ] Divisão'''))

if escolha == 1:
    print(f"O resultado é {soma.soma(escolha, n1, n2)}")
elif escolha == 2:
    subtracao.sub(escolha, n1, n2)
elif escolha == 3:
    mult.multiplica(escolha, n1, n2)
elif escolha == 4:
    div.divisao(escolha, n1, n2)