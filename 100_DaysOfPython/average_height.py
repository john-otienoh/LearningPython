students_height = input("Enter a list of student heights separated by space: ").split(' ')
sum, average_height= 0, 0
for n in students_height:
    sum += int(n)
average_height = round(sum / len(students_height), 2)
print(f"""
      Student height entered is {students_height}\n
      Total sum of heights entered is {sum}\n
      Average height is {average_height}""")