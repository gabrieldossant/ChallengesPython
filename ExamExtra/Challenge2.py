i = 1
contAnoAnterior = 0
somaAnoAnterior = 0
somaAnoPosterior = 0
qtdPosterior = 0
qtdAnterior = 0
qtdCarros = 0
mediaAnterior = 0
mediaPosterior = 0

while i < 100:
    modelo = input("Qual é o modelo do carro?")
    ano = int(input("Qual é o ano do carro? "))
    print("--------------------------")
    if ano < 1990:
        somaAnoAnterior = somaAnoAnterior + ano
        qtdAnterior = qtdAnterior + 1
        i = i + 1
        qtdCarros = qtdCarros + 1
        if qtdCarros == 5:
            mediaAnterior = somaAnoAnterior/qtdAnterior
            mediaPosterior = somaAnoPosterior/qtdPosterior
            totalMedia = (mediaPosterior + mediaAnterior)/ i
            print(f"A média dos anos dos carros anteriores a 1990 é {mediaAnterior}")
            print(f"A média dos anos dos carros posteriores a 1990 é {mediaPosterior}")
            print(f"A média dos anos de todos os carros inserido é {totalMedia}")
            exit()
    if ano > 1995:
        somaAnoPosterior = somaAnoPosterior + ano
        qtdPosterior = qtdPosterior + ano
        i = i + 1
    if ano == 1995:
        mediaAnterior = somaAnoAnterior/qtdAnterior
        mediaPosterior = somaAnoPosterior/qtdPosterior
        totalMedia = (mediaPosterior + mediaAnterior)/ i
        print(f"A média dos anos dos carros anteriores a 1990 é {mediaAnterior}")
        print(f"A média dos anos dos carros posteriores a 1990 é {mediaPosterior}")
        print(f"A média dos anos de todos os carros inserido é {totalMedia}")
        exit()

