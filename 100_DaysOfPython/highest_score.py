#!/usr/bin/python3
# We can use the max function instead
students_score = input("Enter a list of student score separated by space: ").split(' ')
largest_score = int(students_score[0])
for i in students_score:
    i = int(i)
    if i > largest_score:
        largest_score = i
print(f"The highest score in the class is: {largest_score}")