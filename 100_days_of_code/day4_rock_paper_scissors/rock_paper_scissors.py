import random

rock = """
Rock
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

paper = """
Paper
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissors = """
Scissors
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""

hand_sign = [rock, paper, scissors]

print("Welcome to the game of Rock, Paper, Scissors....")

computer_choice = random.randint(0,2);

user_choice = int(input("""
Please Enter your choice...
- For Rock Enter 0
- For Paper Enter 1
- For Scissors Enter 2\n\n"""))

if 0<=user_choice<=2:
    print("You have selected")
    print(hand_sign[user_choice])
    print("Computer Selected")
    print(hand_sign[computer_choice])

    if (computer_choice==user_choice-1) or (computer_choice==2 and user_choice==0):
        print("You win Boy!!")
    elif computer_choice==user_choice:
        print("Thats a draw")
    else:
        print("You lose!")

else:
    print("You have failed as intelligent human being, for not being able to enter Number.")


