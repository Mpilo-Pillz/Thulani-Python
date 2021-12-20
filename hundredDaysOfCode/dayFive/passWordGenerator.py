#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
password = ""

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
for num in range(0, nr_letters):
    random_num_in_letters = random.randint(0, len(letters) - 1)
    password += letters[random_num_in_letters]

for num in range(0, nr_numbers):
    password += numbers[random.randint(0, 9)]

for num in range(0, nr_symbols):
    random_symbol_in_symbols = random.randint(0, len(symbols) - 1)
    password += symbols[random_symbol_in_symbols]

print(password)
# convert_password_to_array = list(password)
# print('-->',convert_password_to_array)
# shuffle_password_array = random.shuffle(convert_password_to_array)
# random.shuffle(random.shuffle(convert_password_to_array))
print(list(password))
print('-->',random.shuffle(list(password)))
shuffled = random.sample(password, len(password))
print("shuf-->", shuffled)

# print(shuffle_password_array)
# shuffle_password = ''.join(shuffle_password_array)
# print(f"Shuffled word is {shuffle_password}")
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# TODO: shuffle the words
shuffledPAssword = ""

for word in shuffled:
    shuffledPAssword += word

print(f"your shuffled password is {shuffledPAssword}")