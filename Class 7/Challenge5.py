'''
    Lucas is taking the subject of Programming Language and will make an 
    algorithm (flowchart) that will calculate the final grade of the subject 
    and verify the final condition, according to the table. Also, considering 
    that there will be five activities that make up 50% of the grade and the 
    other 50% will be a (single) Assessment. How will this algorithm work? 
    Use your knowledge of abstraction, algorithms, and problem decomposition
'''
def verifyActivityNote(x):
    gradeActivity = float(input(f"Enter your {x} activity grade: [0/2]"))
    if(gradeActivity >= 0 and gradeActivity <= 2):
        return gradeActivity
    else: 
        print("Invalid number. Try again inside the dedault.")
        return verifyActivityNote(x)

def pushGrade():
    for i in range(1, 6):
        grade.append(verifyActivityNote(i))

def verifyExamGrade():
    exam = float(input(f"Enter your Exam grade: [0/10]"))
    if exam >= 0 and exam <= 10:
        return exam
    else:
        print("Invalid number. Try Again inside the default.")
        return verifyExamGrade()

def sumGradesActivity(list):
    sumAct = 0
    for i in range(len(list)):
        sumAct += list[i]
    return sumAct

def sumGrades(x, y):
    total = x + y
    return total

def mediaGrade(x):
    division = x/2
    return division

def verifyResult(x):
    if x >= 0 and x < 4:
        print(f"REPROVED! \n Your media result is {x.__round__(2)}")
    elif x >= 4 and x < 7:
        print(f"EXAM! \n Your media result is {x.__round__(2)}")
    else:
        print(f"APROVED! \n Your media result is {x.__round__(2)}")

def show():
    pushGrade()
    examGrade = verifyExamGrade()
    sumActivity = sumGradesActivity(grade)
    sumTotal = sumGrades(examGrade, sumActivity)
    result = mediaGrade(sumTotal)
    verifyResult(result)

grade = []
show()
