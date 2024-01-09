#!/usr/bin/python3
import random
#Variables
word_list = input("Enter atleast 3 words to play with: ").split(' ')
choosen_word = random.choice(word_list)
display = []
end_of_game = False
word_length = len(choosen_word)
lives  = len(choosen_word)
for i in range(word_length):
    display += ['_']
print(display)
while not end_of_game:
    guess = input("Enter a letter: ").lower()
    for i in range(word_length):
        if choosen_word[i] == guess:
            display[i] = guess
    if guess not in choosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You Lose")
    if guess not in choosen_word:
        print(f"{guess} is not in {choosen_word}")
    if '_' not in display:
        end_of_game = True
        print("You Win")
print(f"The Chosen word is {choosen_word}")