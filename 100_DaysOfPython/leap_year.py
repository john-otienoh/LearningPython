#!usr/bin/python3
year = int(input("Which year do you want to check: "))
test_one = year / 4
test_two = year / 100
test_three = year / 400
if year % 4 == 0:
    if year % 100 != 0:
        print("This is a leap year")
    else:
        if year % 400 == 0:
            print("This is leap year")
        else:
            print("This is not a leap year")
else:
    print("This is not a leap  year")