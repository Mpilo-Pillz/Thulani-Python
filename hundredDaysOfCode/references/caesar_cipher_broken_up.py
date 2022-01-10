alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
word_array = ["mpilo", "fikasentech"]
decrypted_word_array = []
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
    decrypted_word_array.append(decrypted_word)

for word in word_array:
    decrypt(word, 2)

print(decrypted_word_array)