#Password Generator Project
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

charcter_list = [letters, numbers, symbols]
total_pass_legnth = nr_letters+nr_symbols+nr_numbers

letters_count=0
symbols_count=0
numbers_count=0
password = ""

for character in range(total_pass_legnth * 2):
    current_list_index = random.randint(0,2);
    if letters == charcter_list[current_list_index] and letters_count < nr_letters:
        password += random.choice(letters)
        letters_count = letters_count+ 1
    elif symbols == charcter_list[current_list_index] and symbols_count < nr_symbols:
        password += random.choice(symbols)
        symbols_count += 1
    elif numbers == charcter_list[current_list_index] and numbers_count < nr_numbers:
        password += random.choice(numbers)
        numbers_count += 1

print(f'{password} of length {len(password)}')


# Or another way to tackle the same problem would be
password=""
password_list = []

for letter in range(0, nr_letters):
    password_list.append(random.choice(letters))
for number in range(0, nr_numbers):
    password_list.append(random.choice(numbers))
for symbol in range(0, nr_symbols):
    password_list.append(random.choice(symbols))

random.shuffle(password_list)

for char in password_list:
    password += char

print(f'{password} is {len(password)} long')