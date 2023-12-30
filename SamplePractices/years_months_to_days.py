#!/bin/usr/python3
year = input("Enter number of Years: ")
month = input("Enter number of Months: ")
day = 0
if int(month) % 2 == 0:
    day = (int(year) * 365) + (int(month) * 30)
else:
    day = (int(year) * 365) + (int(month) * 31)
print(f"{year} years(s) and {month} month(s) is equal to {day} days")