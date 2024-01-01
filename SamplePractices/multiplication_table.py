#!/usr/bin/python3
num = input("Enter a digit you want to see it's multiplication table:  ")
for i in range(1, int(num) + 1):
    for j in range(1, int(num) + 1):
        print(i * j, end=" ")
    print('\n')
else:
    print("Here is your table")
