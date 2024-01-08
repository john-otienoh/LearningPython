#!/usr/bin/python3
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 
           'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 
           'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 
           'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '+', '?']
full_password, full_password_in_string = [], ''
print("Welcome to the PyPassword Generator!")
user_letters = random.randint(1, 5)
user_numbers = random.randint(1, 5)
user_symbols = random.randint(1, 5)
for i in range(0, user_letters):
    full_password.append(random.choice(letters))
for i in range(0, user_numbers):
    full_password.append(random.choice(numbers))
for i in range(0, user_symbols):
    full_password.append(random.choice(symbols))
random.shuffle(full_password)
for i in full_password:
    full_password_in_string  += i
print(f"Here is your password {full_password_in_string}")