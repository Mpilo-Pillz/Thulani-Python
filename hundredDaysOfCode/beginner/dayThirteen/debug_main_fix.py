def my_function():
    for i in range(1, 21):
        if i == 20:
            print("GOT IT!")
my_function()

# def my_function():
#     for i in range(1, 20 + 1):
#         if i == 20:
#             print("GOT IT!")
# my_function()
# def my_function():
#     for i in range(1, 20):
#         if i == 20:
#             print("GOT IT!")
# my_function()

# BUG 2
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5)
# # dice_num = 6 out of range
# # dice_num = 1 misses the 1 at index 0
# print(dice_imgs[dice_num])
#
# # BUG 3
# year = int(input("What's your year of birth?"))
# if year >= 1980 and year <= 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")
#
# # BUG 4
# age = int(input("How old are you?"))
# if age > 18:
#     print(f"You can drive at age {age}.")

# BUG 5
#Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(f"total words is {total_words}: words per page is {pages}")
# print(total_words)

# #Use a Debugger
def mutate(a_list):
  b_list = []
  for item in a_list:
    new_item = item * 2
    b_list.append(new_item)
  print(b_list)

mutate([1,2,3,5,8,13])