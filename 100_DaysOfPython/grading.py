student_score = {
    'john': 81,
    'jane': 78,
    'jack': 99,
    'joe': 74,
    'doe': 62,
}
student_grade = {}
for student in student_score:
    if student_score[student] > 90 and student_score[student] < 100:
        student_grade[student] = 'Outstanding.'
    elif student_score[student] > 80:
        student_grade[student] = 'Exceeds Expectation.'
    elif student_score[student] > 70:
        student_grade[student] = 'Acceptable.'
    elif student_score[student] < 70:
        student_grade[student] = 'Fail.'
print(student_grade)
print(student_score)