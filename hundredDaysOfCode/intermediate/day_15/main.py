money = 0
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coins = {
    "quarters": 0.25,
    "dimes": 0.10,
    "nickles": 0.05,
    "pennies": 0.01,
}


def calculate_total_based_on_coins_added( coin_type, number_of_coins):
    global coins
    return number_of_coins * coins[coin_type]

def deduct_resources(resources, drink):
    print(f"Menu- {resources}, DRINK - {drink}")
    for resource in resources:
        print("PABZZZ-->", resource)
    resources["water"] = resources["water"] - drink["ingredients"]["water"]
    resources["milk"] = resources["milk"] - drink["ingredients"]["milk"]
    resources["coffee"] = resources["coffee"] - drink["ingredients"]["coffee"]
    print("------------------------")
    print(resources)
    return {}



    # for ingredient in menu:
# def runMachine():

# if(resources[])
# TODO: 1 - Input prompt "What would you like?"
drink_choice = input("What would you like? (latte, espresso, cappuccino: ")
drink_selected = MENU[drink_choice]
total_cash = 0

# TODO: 2 - Print "Please insert coins"
print("Please insert coins. ")

for coin in coins:
    # TODO: 3 - Prompt "How many quarters"
    # TODO: 4 - Prompt "How many dimes"
    # TODO: 5 - Prompt "How many nickles"
    # TODO: 6 - Prompt "How many pennies"
    total_coins = int(input(f"How many {coin}? "))
    total_cash += calculate_total_based_on_coins_added(coin, total_coins)
print(total_cash)
change = total_cash
if MENU[drink_choice]["cost"] <= total_cash:
    change = total_cash - MENU[drink_choice]["cost"]
else:
    print("Not enough money. Money returned.")
print("change", change)
print("price latter", MENU[drink_choice])
# TODO: 7 - Print "Here is your change {change}"
# TODO: 8 - Print "Here is your {drink}☕"

# TODO: 9 - Turn off coffee machine"
# TODO: 10 - Print report"
def printReport(resources, money):
    unit = "ml"
    for key in resources:
        if key == "coffee":
            unit = 'g'
        print(f"{key}: {resources[key]}{unit}")
    print(f"Money: ${money}")

printReport(resources, money)
deduct_resources(resources, drink_selected)
