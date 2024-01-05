#!/usr/bin/python3
import random
choice = int(input("What do you choose? Press\n0-Rock\n1-Paper\n2-Scissor\n"))
option = ['Rock', 'Paper', 'Scissors']
computer = random.randint(0, 2)
print(f"You selected {option[choice]}\nComputer selected {option[computer]}")
if choice > 2 or choice < 0:
    print("Invalid Number")
elif choice == 0 and computer == 2:
    print("User wins")
elif choice < computer:
    print("Computer Wins")
elif choice == computer:
    print("You Both Draw")
elif computer == 0 and choice == 2:
    print("Computer Wins")
elif choice > computer:
    print("User wins")