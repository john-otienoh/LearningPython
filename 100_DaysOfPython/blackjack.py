############### Our Blackjack House Rules #####################
## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
play_game = input("Do you want to play a game of blackjack? Type 'y' or 'n'")
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
import random
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
is_game_over = False
user_cards = []
computer_cards = []

def deal_card():
    '''deal_card() function that uses the List below to *return* a random card.'''

    random_card = random.choice(cards)
    return random_card
def play_game():
    for _ in range(0, 2):
        '''Deal the user and computer 2 cards each using deal_card() and append().'''

        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    def calculate_score(list_of_cards):
        '''calculate_score() that takes a List of cards as input and returns the score.
        Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) 
        and return 0 instead of the actual score. 0 will represent a blackjack in our game.'''

        if 11 in list_of_cards and 10 in list_of_cards and len(list_of_cards) == 2:
            return 0
        if 11 in list_of_cards and sum(list_of_cards) > 21:
            list_of_cards.remove(11)
            list_of_cards.append(1)

        return sum(list_of_cards)

    def compare(computer_result, user_result):
        if computer_result == user_result:
            return "It's a draw"
        elif computer_result == 0 or user_result > 21:
            return "Coputer Wins User Loses"
        elif computer_result > 21 or user_result == 0:
            return "User Wins Computer loses"
        else:
            return "User Wins" if user_result > computer_result else "Computer wins"

    while not is_game_over:
        user_result = calculate_score(user_cards)
        computer_result = calculate_score(computer_cards)
        if user_result == 0 or user_result > 21 or computer_result == 0 or computer_result > 21:
            is_game_over = True 
        else:
            should_user_deal = input("Type 'y' to get another card, type 'n' to pass")
            if should_user_deal == 'y' or should_user_deal == 'Y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while  computer_result < 17 and computer_result != 0:
        computer_cards.append(deal_card())
        computer_result = calculate_score(computer_result)
while input("Type 'y' to play another game of blackjack, type 'n' to quit") == 'y':
    play_game()