#!/bin/usr/python3
height = float(input("Enter your height: "))
weight = float(input("Enter your weight: "))
bmi = weight / (height ** 2)
print("Your BMI is {:.2f}".format(bmi))
