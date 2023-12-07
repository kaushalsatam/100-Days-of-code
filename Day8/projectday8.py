# Caeser cipher - Encryption algorighm

import art
print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# def encrypt(e_text, e_shift):
#     cipher_text = ""
#     for letter in range(0, len(e_text)):    # you can use e_text instead of range function
#         # cipher_text += alphabet[alphabet.index(e_text[letter]) + e_shift]
#         letter_index = alphabet.index(e_text[letter])
#         final_shift = letter_index + e_shift
#         if final_shift > len(alphabet) - 1:
#             final_shift = final_shift - len(alphabet)
#         cipher_text += alphabet[final_shift]
#     print(f"The encoded text is: {cipher_text}")

# def decrypt(d_text, d_shift):
#     plain_text = ""
#     for letter in range(0, len(d_text)):
#         plain_text += alphabet[alphabet.index(d_text[letter]) - d_shift]
#     print(f"The decoded text is: {plain_text}")

def caesar(text, shift, direction):
    changed_text = ""
    for char in range(0, len(text)):
        if direction == 'encode':
            if text[char] in alphabet:
                char_index = alphabet.index(text[char])
                final_shift = char_index + shift
                # if final_shift > len(alphabet) - 1:
                #     final_shift = final_shift - len(alphabet)
                while final_shift > len(alphabet) - 1:
                    final_shift = final_shift % len(alphabet)
                changed_text += alphabet[final_shift]
            else:
                changed_text += text[char]
        if direction == 'decode':
            if text[char] in alphabet:
                changed_text += alphabet[alphabet.index(text[char]) - shift]
            else:
                changed_text += text[char]

    print(f"The {direction}d text is: {changed_text}")
    

# code for repetition of the Caeser Cipher
result = True
while result == True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(text = text, shift = shift, direction = direction)
    
    should_continue = input("Type 'yes' if you want to go again. Otherwise type 'no'. \n" )
    if should_continue == "no":
        result = False
        print("Goodbye!")