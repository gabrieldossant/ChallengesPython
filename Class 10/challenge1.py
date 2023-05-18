sala1 = 10
sala2 = 5
sala3 = 6 
sala4 = 8
sala5 = 0

vagas = [sala1, sala2, sala3, sala4, sala5]

escolhaUsuario = int(input("Digite o número da sala que deseja [1] [2] [3] [4] [5]: "))
if escolhaUsuario == 0:
    print("Você digitou ZERO. Fim do programa!")
    exit()

ingresso = int(input("Digite a quantidade de ingressos para ver o filme: "))

def verifica(sala, qtd_ingressos, vagas):
    if sala < 1 or sala > len(vagas):
        print("Sala inválida!")
        exit()
        
    indice_sala = sala - 1
    vagas_disponiveis = vagas[indice_sala]
    
    if qtd_ingressos > vagas_disponiveis:
        print(f"Esgotado! O número de vagas disponíveis é de {vagas_disponiveis}.")
    else:
        vagas_restantes = vagas_disponiveis - qtd_ingressos
        print("Perfeito! Aproveite o filme!")
        print(f"Lugares disponíveis: {vagas_restantes}")

verifica(escolhaUsuario, ingresso, vagas)

        
