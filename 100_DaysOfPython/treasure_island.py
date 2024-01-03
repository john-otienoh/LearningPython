#!usr/bin/python3
print("Welcome to the Treasure Island\nYour mission is to find the treasure")
path = int(input("Go to left or right:\n0-Right\n1-Left\n"))
if path == 1:
    navigation_method = int(input("Do you want to swim or wait\n0-wait\n1-swim\n"))
    if navigation_method == 0:
        door = int(input("Select the door to enter in\n0-blue\n1-red\n2-yellow\n"))
        if door == 0 or door == 1:
            print("Game Over")
        elif door == 2:
            print("You win")
        else:
            print("Invalid choice")
    else:
        print("Game Over")
else:
    print("Game Over")
