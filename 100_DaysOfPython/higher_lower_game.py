from game_data import logo, vs, data
import random
                                                  
is_game_over = True
user_score = 0
random_celebrityB = random.choice(data)

while is_game_over:
    # Variables
    random_celebrityA = random_celebrityB
    random_celebrityB = random.choice(data)
    celeb_A_followers, celeb_B_followers = random_celebrityA['follower_count'], random_celebrityB['follower_count']
    while celeb_A_followers == celeb_B_followers:
        random_celebrityB = random.choice(data)
        celeb_A_followers, celeb_B_followers = random_celebrityA['follower_count'], random_celebrityB['follower_count']

    celebrity_detailsA = f"Compare A: {random_celebrityA['name']}, a {random_celebrityA['description']}, from {random_celebrityA['country']}."
    celebrity_detailsB = f"Against B: {random_celebrityB['name']}, a {random_celebrityB['description']}, from {random_celebrityB['country']}."

    # Print the ArtWork
    print(logo, '\n', celebrity_detailsA)
    print(vs, '\n',celebrity_detailsB)
    print(celeb_A_followers, celeb_B_followers)
    # Check if user is correct.

    user_choice = input("Who has more followers? Type 'A' or 'B': " ).upper()
    if celeb_A_followers > celeb_B_followers:
        if user_choice == 'A':
            user_score += 1
            print(f"You're right! Current score: {user_score}")
        else:
            print(f"Sorry you're Wrong. Final score is {user_score}")
            is_game_over = False
    else:
        if user_choice == 'B':
            user_score += 1
            print(f"You're right! Current score: {user_score}")
        else:
            print(f"Sorry you're Wrong. Final score is {user_score}")
            is_game_over = False