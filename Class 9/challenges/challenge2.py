frase = []
frase = "Nesta direção; disse o Gato, girando a pata direita, mora um Chapeleiro. E nesta direção, apontando com a pata esquerda, mora uma Lebre de Março. Visite quem você quiser: são ambos loucos!"
pontuacoes = ".,;:?!()[]{}-–—\"'"
fraseSemPontuacao = ""

for c in frase:
    if c not in pontuacoes:
        fraseSemPontuacao += c

print(fraseSemPontuacao)