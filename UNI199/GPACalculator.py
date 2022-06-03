total_credit = 0
total_grade = 0
total_Gpa = 0
GPA_list = []
Gpa = 0

number = int(input("Enter the number of students: "))
for i in range(1,number+1):
    total_credit = 0
    total_grade = 0
    print("\nStudent ", i, ":")
    course = int(input("Enter the number of courses taken: "))
    for j in range(1,course+1):
        print("Course ", j, ":")
        grade = int(input("Enter grade out of 4 :"))
        credit = int(input("Enter the course credit: "))
        total_credit += credit
        total_grade += grade*credit
    Gpa = total_grade/total_credit
    total_Gpa += Gpa
    print("Gpa for the student",i,"is ", Gpa)
    GPA_list.append(Gpa)
print("Highest GPA: ", max(GPA_list))
print("Average GPA of the students:", total_Gpa/number)
