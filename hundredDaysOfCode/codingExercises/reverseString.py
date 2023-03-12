def reverseString(word):
    reversedWord = ""
    for char in reversed(range(len(word))):
        print(char)
        reversedWord += word[char]
    return reversedWord

print(reverseString("print"))
