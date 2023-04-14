activityNote = float(input("Type the activity note: "))
examGrade = float(input("Type the exam grade: "))
sum = 0
average = 0

if activityNote >= 0 and activityNote <= 10:
    sum += activityNote
elif examGrade >= 0 and examGrade <= 10:
    sum += examGrade

average = sum/2

if average >= 0 and average < 4:
    print(f"The average students is {average} \n REPROVED")
elif average >= 4 and average < 7:
    print(f"The average students is {average} \n EXAM")
elif average >= 7 and average <= 10:
    print(f"The average students is {average} \n APROVED")