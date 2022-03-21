# GUESS THE NUMBER
- print logo
- print Welcome to the Guessing Game
- Print I'm thinking of a number between 1 and 100.
- Generate a random number between 1 and 100
  - store number in variable called number_to_guess
- Input Choose a difficulty. Type 'easy' or hard
  - store in a variable called difficulty
  - hard has 5 attempts
  - easy has 10 attempts
- print "your have {hard or easy} attempts remaining"
- Input Make a guess
  - convert to an Int
  - store in var called user_guess

## KEEPING THE GAME ALIVE
loop while game_is_not_over
    game_is_not_over = True
    
while game_is_not_over
## YOU WIN
if number is == user_guess
    - print you win
    - end the game -game_is_not_over to false

## Wrong Guess
store in cunction caalled compare
if number > user_guess
   print Too high
    deduct 1 from hard | easy
    print number of attempts remaining
if number < user_guess
    print Too low
    deduct 1 from hard | easy
    print number of attempts remaining

if tries left == 0
 Game over


