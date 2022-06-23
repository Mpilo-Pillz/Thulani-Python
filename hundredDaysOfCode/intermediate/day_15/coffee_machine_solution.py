MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0

resources = {
    "water": 10300,
    "milk": 1200,
    "coffee": 1100,
}

coins = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01,
}


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made and False if ingredients are insufficient"""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True


def process_coins():
    """Returns the total calculated form coins inserted"""
    print("Pelase insert coins")
    total = input("how many quarters") * 0.25
    total += input("how many Dimes") * 0.10
    total += input("how many nickles") * 0.05
    total += input("how many pennis") * 0.01
    return total


is_on = True

while is_on:
    choice = input("What would you like? (latte, espresso, cappuccino): ")

    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink):
            payment = process_coins()
