def final_grade(dicti, weights):
    final_grade = {}
    failed_students = []
    count = 0
    for name, grade in dicti.items():
        total = grade['Attendance'] * weights['Attendance'] + grade['HW'] * weights['HW'] + grade['Quiz'] * weights[
            'Quiz'] + grade['Lab'] * weights['Lab'] + grade['Exam'] * weights['Exam']
        if total >= 60:
            final_grade[name] = 'Pass'
        else:
            final_grade[name] = 'Fail'
            failed_students.append(name)
            count += 1
    return final_grade, failed_students, count


gradebook = {'Ross': {'Attendance': 100, 'HW': 100, 'Quiz': 100, 'Lab': 100, 'Exam': 100},
             'Rachel': {'Attendance': 40, 'HW': 45, 'Quiz': 50, 'Lab': 50, 'Exam': 50},
             'Monica': {'Attendance': 100, 'HW': 100, 'Quiz': 90, 'Lab': 90, 'Exam': 100},
             'Chandler': {'Attendance': 80, 'HW': 90, 'Quiz': 90, 'Lab': 80, 'Exam': 90},
             'Phoebe': {'Attendance': 20, 'HW': 55, 'Quiz': 30, 'Lab': 30, 'Exam': 35},
             'Joey': {'Attendance': 10, 'HW': 30, 'Quiz': 25, 'Lab': 15, 'Exam': 20}}

weights = {'Attendance': 0.05,
           'HW': 0.3,
           'Quiz': 0.3,
           'Lab': 0.1,
           'Exam': 0.25}

print(final_grade(gradebook, weights))