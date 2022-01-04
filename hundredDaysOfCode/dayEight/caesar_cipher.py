alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def encrypt(text, shift):
    encrypted_word = ""

    # TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
    for letter in range(len(text)):
        indexOfWordInAlphabet = alphabet.index(text[letter])
        if text[letter] in alphabet:
            print(alphabet.index(text[letter]))
            if (indexOfWordInAlphabet + shift) <= (len(alphabet) - 1):
                encrypted_word += alphabet[alphabet.index(text[letter]) + shift]
            else:
                encrypted_word += alphabet[(alphabet.index(text[letter]) + shift) - (len(alphabet))]
    print(f"{text} encrypted by shift number {shift} is {encrypted_word}")
    #e.g.
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛
    # i get an index out of range

def decrypt(text, shift):
    decrypted_word = ""

    for letter in range(len(text)):
        indexOfWordInAlphabet = alphabet.index(text[letter])

        if text[letter] in alphabet:
            if indexOfWordInAlphabet - shift >= 0:
                decrypted_word += alphabet[(indexOfWordInAlphabet - shift) - (len(alphabet))]
            else:
                decrypted_word += alphabet[(alphabet.index(text[letter]) - shift) + (len(alphabet))]
    print(f"{text} decrypted by shift number {shift} is {decrypted_word}")

# encrypt(text, shift)
decrypt(text, shift)
# djwjmjabujpo