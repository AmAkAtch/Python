import random

print("Welcome to Nubmer guessing Game")
print("You have to guess the Number I am thinking between 1 to 100..")

original_num = random.randint(1,100)
guesses = 0
isSearching = True

difficulty = input("Please Select difficulty 'hard', 'medium', 'easy': ").lower()
if difficulty == "hard":
    guesses = 3
elif difficulty == "medium":
    guesses = 5
else:
    guesses = 10

while guesses>0 and isSearching:
    guess = int(input("Guess the number: "))
    if guess < original_num:
        print("You are lower")
        guesses -= 1
    elif guess > original_num:
        print("You are Higher")
        guesses -= 1
    else:
        print("Dang it!! You win")
        isSearching = False
    print(f'You have {guesses} guesses left')

print("Thanks for playing")
