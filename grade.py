def gradingStudents(grades):
    temp=0
    new_grade=[]
    for i in range(len(grades)):
        temp=grades[i]
        if (temp<38):
            new_grade.append(temp)
        else:
            if (temp%5 >= 3):
                a=5*((int(temp/5))+1)
                new_grade.append(a)
            else :
                new_grade.append(temp)
    return new_grade

grades_count = int(input().strip())

grades = []

for _ in range(grades_count):
    grades_item = int(input().strip())
    grades.append(grades_item)

result = gradingStudents(grades)
print(result)
