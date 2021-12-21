import random
from hangman_art import stages, logo
from hangman_words import word_list

# Select a random word
word_answer = word_list[random.randint(0, len(word_list) - 1)]
obscurial = ""
print(word_answer)

for word in word_answer:
    obscurial += '_'

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