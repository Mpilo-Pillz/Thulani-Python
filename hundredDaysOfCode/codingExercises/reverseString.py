def reverseString(word):
    reversedWord = ""
    for char in reversed(range(len(word))):
        print(char)
        reversedWord += word[char]
    return reversedWord

print(reverseString("print"))

# Reverse String Fancy
str = "race"
print("".join(reversed(str)))

# Reverse super fancy
string = "racecar"
print(string[::-1])


