print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, L")
add_pepperoni = input("Do you want pepperoni?, Y or N?")
extra_cheese = input("Do you want extra cheese?, Y or N")

small_pizza = 15
medium_pizza = 20
large_pizza = 25

cheese = 1
pepperoni_for_small = 2
pepperoni_for_medium_or_large = 3

total_cost = 0

if (size == "L"):
    total_cost += large_pizza

    if (add_pepperoni == "Y"):
        total_cost += pepperoni_for_medium_or_large

    if(extra_cheese == "Y"):
        total_cost += cheese

if (size == "M"):
    total_cost += medium_pizza

    if(add_pepperoni == "Y"):
        total_cost += pepperoni_for_medium_or_large

    if(extra_cheese == "N"):
        total_cost += cheese

if (size == "S"):
    total_cost += small_pizza

    if (add_pepperoni == "Y"):
        total_cost += pepperoni_for_small

    if (extra_cheese == "Y"):
        total_cost += cheese

print(f"Total cost for your order is ${total_cost}")