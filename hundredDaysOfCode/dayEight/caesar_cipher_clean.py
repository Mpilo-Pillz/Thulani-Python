alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")



# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text, shift):
    encrypted_word = ""

    # TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
    for letter in range(len(text)):
        if text[letter] in alphabet and text[letter].isalpha():
            indexOfWordInAlphabet = alphabet.index(text[letter])
            print(alphabet.index(text[letter]))
            if (indexOfWordInAlphabet + shift) <= (len(alphabet) - 1):
                encrypted_word += alphabet[alphabet.index(text[letter]) + shift]
            else:
                encrypted_word += alphabet[(alphabet.index(text[letter]) + shift) - (len(alphabet))]
        else:
            encrypted_word += text[letter]
    print(f"{text} encrypted by shift number {shift} is {encrypted_word}")


def decrypt(text, shift):
    decrypted_word = ""

    # for word in text_list():
    for letter in range(len(text)):
        if text[letter] not in alphabet:
            decrypted_word += text[letter]
        else:
            indexOfWordInAlphabet = alphabet.index(text[letter])
            if text[letter] in alphabet and text[letter].isalpha():
                if indexOfWordInAlphabet - shift >= 0:
                    decrypted_word += alphabet[(indexOfWordInAlphabet - shift) - (len(alphabet))]
                else:
                    decrypted_word += alphabet[(alphabet.index(text[letter]) - shift) + (len(alphabet))]

    print(f"{text} decrypted by shift number {shift} is {decrypted_word}")


if direction == "encode":
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    encrypt(text, shift)
elif direction == "decode":
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    decrypt(text, shift)
else:
    print("INVALID INPUT")
# djwjmjabujpo