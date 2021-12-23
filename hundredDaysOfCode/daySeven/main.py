import random
from hangman_art import stages, logo
from hangman_words import word_list

isGameActive = True
word_answer = word_list[random.randint(0, len(word_list) - 1)]
obscurial = ""
obscurialArray = []

for word in word_answer:
    obscurialArray.append('_')
    obscurial += '_'

while isGameActive:
    # Select a random word
    print(word_answer)
    print(obscurial)
    print(obscurialArray)
    user_guess = input("Guess a letter in the word\n")

    for word in word_answer:
        if (user_guess == word):
            obscurial += user_guess
            print(obscurial)
            obscurialArray.append(word)
            break
        else:
            print(stages[0])
            obscurial += '_'
            print(obscurial)
            obscurialArray.append('_')
            break

print(obscurialArray)
print(obscurial)

# declare number of wrongs
# while number of wrongs is less than stages.lenth
#     input guess the letter
#     check letter is in word
#  if word is not in letter
#   number of plus1
#   print stages length - number of wrond
#  else
#     replace _ with word
#   print _ with words