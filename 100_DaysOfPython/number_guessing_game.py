#!/usr/bin/python3
from random import randint
print("Welcome to Number Guessing Game!\nI'm thinking of a number between 1 and 100.")
game_level = input("Choose a difficulty: Type 'easy' or 'hard': ")
if game_level == 'easy':
    number_of_attempts = 10
    random_number = randint(0, 100)
    print(f"{random_number}")
    while number_of_attempts > 0:
        print(f"You have {number_of_attempts} attempts remaining to guess the number.")
        number_guessed = int(input("Make a guess: "))
        if number_guessed > random_number:
            print("Too high.\nGuess again")
            if number_of_attempts == 1:
                print("You have run out of guesses, you lose.")
        elif number_guessed < random_number:
            print("Too low.\nGuess again")
            if number_of_attempts == 1:
                print("You have run out of guesses, you lose.")
        else:
            print(f"You got it! The answer is {random_number}")
            break
        number_of_attempts -= 1
elif game_level == 'hard':
    number_of_attempts = 5
    random_number = randint(0, 100)
    while number_of_attempts > 0:
        print(f"You have {number_of_attempts} attempts remaining to guess the number.")
        number_guessed = int(input("Make a guess: "))
        if number_guessed > random_number:
            print("Too high.\nGuess again")
            if number_of_attempts == 1:
                print("You have run out of guesses, you lose.")
        elif number_guessed < random_number:
            print("Too low.\nGuess again")
            if number_of_attempts == 1:
                print("You have run out of guesses, you lose.")
        else:
            print(f"You got it! The answer is {random_number}")
            break
        number_of_attempts -= 1