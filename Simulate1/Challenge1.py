valueA = int(input("Digite o primeiro número: "))
valueB = int(input("Digite o segundo número: "))
valueC = int(input("Digite o terceiro número: "))

print("Os números digitados foram ", valueA, valueB, valueC)

if (valueA > valueB and valueA > valueC):
    if (valueB > valueC):
        print("Os números na ordem decrescente são", valueA, valueB, valueC)
if (valueA > valueB and valueA > valueC):
    if (valueC > valueB):
        print("Os números na ordem decrescente são", valueA, valueC, valueB)
if (valueB > valueA and valueB > valueC):
    if (valueA > valueC):
        print("Os números na ordem decrescente são", valueB, valueA, valueC)
if (valueB > valueA and valueB > valueC):
    if (valueC > valueA):
        print("Os números na ordem decrescente são", valueB, valueC, valueA)
if (valueC > valueA and valueC > valueB):
    if (valueA > valueB):
        print("Os números na ordem decrescente são", valueC, valueA, valueB)
if (valueC > valueA and valueC > valueB):
    if (valueB > valueA):
        print("Os números na ordem decrescente são", valueC, valueB, valueA)


if (valueA < valueB and valueA < valueC):
    if (valueB < valueC):
        print("Os números na ordem crescente são", valueA, valueB, valueC)
if (valueA > valueB and valueA < valueC):
    if (valueC < valueB):
        print("Os números na ordem crescente são", valueA, valueC, valueB)
if (valueB < valueA and valueB < valueC):
    if (valueA < valueC):
        print("Os números na ordem crescente são", valueB, valueA, valueC)
if (valueB < valueA and valueB < valueC):
    if (valueC < valueA):
        print("Os números na ordem crescente são", valueB, valueC, valueA)
if (valueC < valueA and valueC < valueB):
    if (valueA < valueB):
        print("Os números na ordem crescente são", valueC, valueA, valueB)
if (valueC < valueA and valueC < valueB):
    if (valueB < valueA):
        print("Os números na ordem crescente são", valueC, valueB, valueA)


