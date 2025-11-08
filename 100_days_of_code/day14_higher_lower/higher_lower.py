import random
from game_data import data
import art

player_score = 0
is_game_on = True
#Display game logo

def display_comparision(celeb1, celeb2):
    """This function takes list items and accesses dictionary data of those items to display"""
    global player_score
    if(player_score>0):
        print(f"Your Score is {player_score} !")
    print(f"Option A {celeb1["name"]}, {celeb1["description"]} from {celeb1["country"]}")
    print(art.vs)
    print(f"Option B: {celeb2["name"]}, {celeb2["description"]} from {celeb2["country"]}")

def compare_followers(celeb1, celeb2):
    if celeb1["follower_count"] > celeb2["follower_count"]:
        return celeb1
    else:
        return celeb2

def ask_and_verify(celeb1, celeb2, correct_answer):
    global is_game_on
    global player_score
    selection = input("Who has more followers, 'A' or 'B' ?: ").lower()
    if (selection=='a' and correct_answer==celeb1) or (selection=='b' and correct_answer==celeb2):
        player_score += 1
        celeb1=celeb2
        return celeb1
    else:
        print(f"\nSorry, That was wrong you failed with final score of {player_score}!!!")
        print(f"{celeb1["name"]} has {celeb1["follower_count"]} followers AND {celeb2["name"]} has {celeb2["follower_count"]} followers \n")
        is_game_on = False
        return

#randomly select 2 entries from data and display
def game():
    global is_game_on
    celeb1 = random.choice(data)
    while is_game_on:
        celeb2 = random.choice(data)
        display_comparision(celeb1=celeb1, celeb2=celeb2)
        correct_answer = compare_followers(celeb1, celeb2)
        celeb1 = ask_and_verify(celeb1, celeb2, correct_answer=correct_answer)
      
game()

