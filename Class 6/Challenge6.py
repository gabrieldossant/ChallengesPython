c = 1
media = 0

while c <= 10:
    grade1 = float(input("Type the first students grade: "))
    grade2 = float(input("Type the second students grade: "))

    media = (grade1 + grade2)/2

    print("The student's average is %.2f" %media)
    c += 1
