students_number = int(input("Enter number of students: "))

student_details = {}
for i in range(students_number):
    name = input("Enter your name: ")
    physics_marks = int(input("Enter your physics marks: "))
    maths_marks = int(input("Enter your maths marks: "))
    history_marks = int(input("Enter your history marks: "))
    total_marks = physics_marks + maths_marks + history_marks
    print(f"{name} has {physics_marks} in physics, {maths_marks} inn maths and {history_marks} in history")
    if total_marks < 120:
        print("You failed.")
    else:
        print("You have passed.")
    student_details[name] = total_marks
print(student_details)