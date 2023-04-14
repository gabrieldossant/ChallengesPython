'''
    Lucas is taking the subject of Programming Language and will make an 
    algorithm (flowchart) that will calculate the final grade of the subject 
    and verify the final condition, according to the table. Also, considering 
    that there will be five activities that make up 50% of the grade and the 
    other 50% will be a (single) Assessment. How will this algorithm work? 
    Use your knowledge of abstraction, algorithms, and problem decomposition
'''
activityNote = float(input("Type the activity note: "))
examGrade = float(input("Type the exam grade: "))
sum = 0
average = 0

if activityNote >= 0 and activityNote <= 10:
    sum += activityNote
elif examGrade >= 0 and examGrade <= 10:
    sum += examGrade
else:
    print("Invalid grade!")

average = sum/2

if average >= 0 and average < 4:
    print(f"The average students is {average} \n REPROVED")
elif average >= 4 and average < 7:
    print(f"The average students is {average} \n EXAM")
elif average >= 7 and average <= 10:
    print(f"The average students is {average} \n APROVED")