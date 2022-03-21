import random
names_string = input("Enter the names of the people at the dinner table separated by comma and space")
names_list = names_string.split(", ")

print(names_list)
print("the bill will be paid by...drumroll")
random_num_in_list = random.randint(0, len(names_list) - 1)
# print(len(names_list))
# print(random_num_in_list)
print(f"{names_list[random_num_in_list]} is going to pay for the meal")
print(f"{random.choice(names_list)} is the choice to pay")