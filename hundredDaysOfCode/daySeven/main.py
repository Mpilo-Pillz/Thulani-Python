import random
from hangman_art import stages, logo
from hangman_words import word_list

# Select a random word
word_answer = word_list[random.randint(0, len(word_list) - 1)]

obscurial = ""
obscurialArray = []
print(word_answer)
user_guess = input("Guess a letter in the word\n")
for word in word_answer:
    print(word)
    if (user_guess == word):
        obscurial += user_guess
        obscurialArray.append(word)
    else:
        obscurial += '_'
        obscurialArray.append('_')

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