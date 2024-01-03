#!/bin/usr/python3
height = float(input("Enter your height: "))
weight = float(input("Enter your weight: "))
bmi = weight / (height ** 2)
print("Your BMI is {:.2f}".format(bmi))
if bmi < 18.5:
    print("You are underweight")
elif bmi > 18.5 and bmi < 25:
    print("You are of normal  weight")
elif bmi > 18.5 and bmi < 25:
    print("You are overweight")
elif bmi > 30 and bmi < 35:
    print("You are obese")
else:
    print("You are clinically Obese")
