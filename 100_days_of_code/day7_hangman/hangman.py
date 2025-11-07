import random
from lists import words, stages

print("Welcome to the Game of Hangman")

current_word = random.choice(words)
current_word = current_word.lower()

remaining_attempts = 6
right_words = 0
guessed_word = ["_"]*len(current_word)

while remaining_attempts>0 and right_words<len(current_word):
    guessed_character = str(input("Guess the Character in the word: \n"))

    if (guessed_character in current_word) and not (guessed_character in guessed_word):
        positions = [i for i, ch in enumerate(current_word) if ch==guessed_character]

        for position in positions:
            guessed_word[position] = guessed_character

        print(stages[-remaining_attempts-1])
        print(f'Solved Word: {"".join(guessed_word)}')

        right_words += len(positions)

    else:
        print(stages[-remaining_attempts])
        print(f'Solved Word: {"".join(guessed_word)}')

        remaining_attempts -= 1

if remaining_attempts==0:
    print("You failed !!")
else:
    print("Good Job Boii !!!")
    

    
