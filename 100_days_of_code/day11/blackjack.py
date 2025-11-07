import random
from blackjack_title import blackjack_title

print("Welcome to the game of Blackjack!!!")
print(blackjack_title)


def draw_another():
    """This Function will append random card at the end of the list"""

    player_hand.append(random.choice(deck))
    print(f"Your new deck after drawing one card: {player_hand}")
    if(sum(player_hand) > 21):
        if 11 in player_hand:
            player_hand[player_hand.index(11)] = 1
        if sum(player_hand)>21:
            print("You lose because your total exceeded 21 !!!")
        else:
            print(f"Your final hand {player_hand} and new total: {sum(player_hand)}")
    else:
        print(f"Your final hand {player_hand} and new total: {sum(player_hand)}")


def check_win():
    if sum(dealers_hand)>21 and sum(player_hand)<21:
        print("You win as Dealer's hand exceeds 21 !!!!!")
    elif sum(player_hand)>21 and 17<sum(dealers_hand)<21:
        print("You lose as your hand is higher than 21 !!!")
    elif sum(player_hand)>sum(dealers_hand):
        print("You win !!!!")
    elif sum(player_hand)<sum(dealers_hand):
        print("You lose !!!")
    else:
        print("Draw !!!")

def reveal_hands():
    print(f"Dealer's hand {dealers_hand}")
    print(f"Your final hand {player_hand}")

    if(sum(dealers_hand)<17) and (len(dealers_hand)<3):
        print("Dealer's total is lower than 17, drawing another card!!!")
        dealers_hand.append(random.choice(deck))
        print(f"Dealer's final hand {dealers_hand} against your hand {player_hand}")
    
    check_win()



#deck of cards where every card with painting is 10 and Ace can be 11 or 1 depending on situation
deck = [11, 2,3,4,5,6,7,8,9,10,10,10,10]
continue_playing = True

while continue_playing:
    dealers_hand = [random.choice(deck), random.choice(deck)]
    player_hand = [random.choice(deck), random.choice(deck)]

    print(f"Dealers hand: [{dealers_hand[0]}, ?]")
    print(f"Your hand: {player_hand}")

    player_draw_another = input("Do you want to draw another card?type 'y' or 'n': ").lower()
    if player_draw_another == "y":
        draw_another()
    reveal_hands()

    user_choice = input("Press 'y' to start a new game, or 'n' to exit: ").lower()
    if(user_choice == "n"):
        continue_playing = False
        print("Thanks for playing black jack with us!!!!")
    else:
        print("\n"*10)
        print(blackjack_title)
        print("Welcome to another game, Cards have been dealt")
    

