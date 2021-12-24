import random
from hangman_art import stages, logo
from hangman_words import word_list

word_answer = word_list[random.randint(0, len(word_list) - 1)]
obscurial = ""
obscurialArray = []
chances = len(stages)
isGameActive = chances > -1

for word in word_answer:
    obscurialArray.append('_')
    obscurial += '_'

while chances > -1:
    if ''.join(obscurialArray) == word_answer:
        print("AWESOME!!! YOU GUESSED THEM ALL")
        break
    # Select a random word
    print(word_answer)
    print(obscurialArray)
    print("mind-->", ''.join(obscurialArray))
    user_guess = input("Guess a letter in the word\n")
    print(word_answer.find(user_guess))
    if (word_answer.find(user_guess) > -1):
        occurrences = [i for i in range(len(word_answer)) if list(word_answer)[i] == user_guess]
        print(occurrences)
        for occurrence in occurrences:
            obscurialArray[occurrence] = user_guess
        # obscurialArray[word_answer.find(user_guess)] = user_guess
        print(word_answer.find(user_guess))
    else:
        chances = chances - 1
        print(stages[chances])

print("GAME OVER SON!!!")
print(obscurialArray)
print(f"The word was {word_answer}")

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