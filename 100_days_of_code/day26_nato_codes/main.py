import pandas as pd

#TODO 1. Create a dictionary in this format:
with open("nato_phonetic_alphabet.csv") as file:
    phonetic_alphabets = {line.split(",")[0].strip():line.split(",")[1].strip() for i, line in enumerate(file) if i != 0}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
user_input = input("Enter the word: ").upper()
df = pd.read_csv("nato_phonetic_alphabet.csv")
print([phonetic_alphabets[char] for char in user_input])
print([df[df.letter == char]["code"].values[0] for char in user_input])


