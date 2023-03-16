'''day1 = input("João trabalhou 1 dia?")
day2 = input("João trabalhou 2 dias?")
day3 = input("João trabalhou 3 dias?")

tvDeTubo = day1 or day2 or day3
print(f"João pode comprar uma tv de tubo? {tvDeTubo}")
tvDe32polegadas = day2 or day3
print(f"João pode comprar uma tv de 32 polegadas? {tvDe32polegadas}")
tvDe55polegadas = day3
print(f"João pode comprar uma tv de 55 polegadas? {tvDe55polegadas}")'''

segunda = input("João trabalhou segunda?")
quarta = input("João trabalhou quarta?")
sexta = input("João trabalhou sexta?")

tvDeTubo = eval(segunda) or eval(quarta) or eval(sexta)
print(f"João pode comprar uma tv de tubo? {tvDeTubo}")
tvDe32polegadas = eval(quarta) or eval(sexta)
print(f"João pode comprar uma tv de 32 polegadas? {tvDe32polegadas}")
tvDe55polegadas = eval(sexta)
print(f"João pode comprar uma tv de 55 polegadas? {tvDe55polegadas}")




