#!usr/bin/python3
print("Welcome to python pizza delivery")
size = input("What size of pizza do you want? S, M or L ")
pepperoni = input("Do you want pepperoni? Y or N ")
cheese = input("Do you want extra cheese? Y or N ")
price = 0
if size == 'S' or size == 's':
    price += 15
    if pepperoni == 'Y' or pepperoni == 'y':
        price += 2
        if cheese == 'y' or cheese == 'Y':
            price += 1
            print(f"Your total bill is: {price}")
        else:
            print(f"Your total bill is: {price}")
    elif pepperoni == 'N' or pepperoni == 'n':
        if cheese == 'y' or cheese == 'Y':
            price += 1
            print(f"Your total bill is: {price}")
        else:
            print(f"Your total bill is: {price}")
elif size == 'M' or size == 'm':
    price += 20
    if pepperoni == 'Y' or pepperoni == 'y':
        price += 3
        if cheese == 'y' or cheese == 'Y':
            price += 1
            print(f"Your total bill is: {price}")
        else:
            print(f"Your total bill is: {price}")
    elif pepperoni == 'N' or pepperoni == 'n':
        if cheese == 'y' or cheese == 'Y':
            price += 1
            print(f"Your total bill is: {price}")
        else:
            print(f"Your total bill is: {price}")
elif size == 'L' or size == 'l':
    price += 25
    if pepperoni == 'Y' or pepperoni == 'y':
        price += 3
        if cheese == 'y' or cheese == 'Y':
            price += 1
            print(f"Your total bill is: {price}")
        else:
            print(f"Your total bill is: {price}")
    elif pepperoni == 'N' or pepperoni == 'n':
        if cheese == 'y' or cheese == 'Y':
            price += 1
            print(f"Your total bill is: {price}")
        else:
            print(f"Your total bill is: {price}")
else:
    print("You haven't place your order")
