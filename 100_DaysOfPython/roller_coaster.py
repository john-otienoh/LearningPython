#!usr/bin/python3
height = int(input("Enter your height: "))
amount = 0
if height >  120:
    print("You can ride")
    age = int(input("Enter your age: "))
    if age > 18:
        amount = 12
        photos = int(input("Do you want photos\n1 - Yes\n2 - No\n"))
        if photos == 1:
            amount += 3
            print(f"You'll pay a total of ${amount}")
        else:
            print(f"You'll pay ${amount}")
    elif age < 12:
        amount =  5
        photos = int(input("Do you want photos\n1 - Yes\n2 - No\n"))
        if photos == 1:
            amount += 3
            print(f"You'll pay a total of ${amount}")
        else:
            print(f"You'll pay ${amount}")
    else:
        photos = int(input("Do you want photos\n1 - Yes\n2 - No\n"))
        if photos == 1:
            amount += 3
            print(f"You'll pay a total of ${amount}")
        else:
            print(f"You'll pay ${amount}")
else:
    print("Can't ride")
