#!/bin/usr/python3
basic_salary = 1500
camera_sold = input("Enter number of cameras sold: ")
camera_price = input("Enter price of  a camera: ")
commission = float(camera_price) * 0.02 * float(camera_sold)
bonus = float(camera_sold) * 200
total_salary =  round(basic_salary, 2) + round(commission, 2) + round(bonus, 2)
print(f"Bonus gained = {bonus}\nCommission gained = {commission}\nTotal Salary = {total_salary}")
