import random
from hangman_art import stages, logo
from hangman_words import word_list

chosen_word = random.choice(word_list)
lives = 6
print(f"Psst the word is {chosen_word}")

display = []
word_length = len(chosen_word)
end_of_game = False
for _ in chosen_word:
    display += "_"
print(display)
while not end_of_game:
    guess = input("Guess a letter \n").lower()

    for position in range(word_length):
        letter = chosen_word[position]
        print(f"Current position: {position}\n Current Letter: {letter}\n Guess-letter: {guess}")
        if letter == guess:
            display[position] = letter


    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose.")
    print(display)

    if "_" not in display:
        end_of_game = True
        print("You win")

    print(stages[lives])
# for letter in chosen_word:
#     if letter == guess:
#         print("Right")
#     else:
#         print("Wrong")

