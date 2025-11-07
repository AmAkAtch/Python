print("Welcome to Ciesar cipher")
print("************************")

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
    'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
    'u', 'v', 'w', 'x', 'y', 'z'
]


def encode():
    plain_text = input("Enter the String to Encode: ")
    shift_number = int(input("Enter the shift Number: "))
    ciphered_text = ""

    for char in plain_text.lower():
        if char not in alphabet:
            ciphered_text += char
        else:
            shifted_index = alphabet.index(char) + shift_number
            shifted_index %= len(alphabet)
            ciphered_text += alphabet[shifted_index]

    print(f'Ciphered text : {ciphered_text}')

def decode():
    cipher_text = input("Enter the String to Decode: ")
    shift_number = int(input("Enter the shift Number: "))
    plain_text = ""

    for char in cipher_text.lower():
        if char not in alphabet:
            plain_text += char
        else:
            shifted_index = alphabet.index(char) - shift_number
            shifted_index %= len(alphabet)
            plain_text += alphabet[shifted_index]
    
    print(f'Plain text : {plain_text}')

continue_choice = 0

while continue_choice == 0:
    user_choice = input("Enter 'encode' to encrypt the message and 'decode' to Decrypt the message: ")

    if user_choice.lower() == "encode":
        print("Welcome to encoding")
        encode()
    elif user_choice.lower() == "decode":
        print("Welcomet to decoding")
        decode()
    else:
        print("Dumfak try again")
    
    continue_choice = int(input("\n To continue using this feature press 0 and to exit press 1: "))
