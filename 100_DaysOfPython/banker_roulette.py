#!usr/bin/python3
import random
names_input = input("Enter everybody's name, separeted by commas: ")
names = names_input.split(", ")
names_len = random.randint(0, (len(names) - 1))
print(f"{names[names_len]} is paying the bill")
