grade = 0
sum = 0
qntGrade = 0
choose = "y"

while choose.upper()[0] == "y" or choose == "Y":
    grade = float(input("Type the students grade: "))
    sum += grade
    qntGrade += 1
    choose = input("Do you want to continue? [Y/N]")

media = sum/qntGrade

print(f"The total average is {media}")