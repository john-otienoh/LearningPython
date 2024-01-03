#!/usr/bin/python3
print("WElcome to my love calculator")
name_one = input("Enter your name: ")
name_two = input("Enter patners name: ")
patners_name = name_one + name_two
patners_name_lower = patners_name.lower()
t = patners_name_lower.count('t')
r = patners_name_lower.count('r')
u = patners_name_lower.count('u')
e = patners_name_lower.count('e')
true = t + r + u + e

l = patners_name_lower.count('l')
o = patners_name_lower.count('o')
v = patners_name_lower.count('v')
e = patners_name_lower.count('e')
love = l + o + v + e
total_score = int(str(true) + str(love))
if total_score < 10 or total_score > 90:
    print(f"Your score is {total_score}, you go together like coke and mentos")
elif total_score >= 10 or total_score <= 90:
    print(f"Your score is {total_score}, you are alright together")
else:
    print(f"Your score is {total_score}")
