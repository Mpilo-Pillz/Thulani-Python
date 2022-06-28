money = 0
machine_on = True
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

def has_no_empty_resource(resources):
    for resource in resources:
        # print("CHECK-->", resource)
        # print(resources[resource])
        if resources[resource] <= 0:
            print("CHECK-->", resource)
            print(resources[resource])
            return False
        # else:
        #     return True

def calculate_total_based_on_coins_added( coin_type, number_of_coins):
    global coins
    return number_of_coins * coins[coin_type]

def deduct_resources(resources, drink):

    for ingredient in drink["ingredients"]:
        resources[ingredient] = resources[ingredient] - drink["ingredients"][ingredient]

def check_resource_sufficiency(resources, drink):
    for ingredient in drink["ingredients"]:
        if(resources[ingredient] >= drink["ingredients"][ingredient] ):
            print("We GOOD")
            return True
        else:
            print(f"We OUT of {ingredient}, pick another drink")
            return False



    # for ingredient in menu:
# def makeCoffee():

# TODO: 1 - Input prompt "What would you like?"
# drink_choice = input("What would you like? (latte, espresso, cappuccino: ")
# drink_selected = MENU[drink_choice]
# total_cash = 0
# drink_choice = input("What would you like? (latte, espresso, cappuccino: ")
# drink_selected = MENU[drink_choice]


def ask_for_coins(drink_choice):
    total_cash = 0
    print("Please insert coins. ")
    for coin in coins:
        total_coins = int(input(f"How many {coin}? "))
        total_cash += calculate_total_based_on_coins_added(coin, total_coins)
    print(total_cash)
    change = total_cash
    if MENU[drink_choice]["cost"] <= total_cash:
        change = total_cash - MENU[drink_choice]["cost"]
        print(f"Here is your {drink_choice} ☕")
    else:
        print("Not enough money. Money returned.")
    print(f"Here is your change {change}")


# TODO: 9 - Turn off coffee machine"

def printReport(resources, money):
    unit = "ml"
    for key in resources:
        if key == "coffee":
            unit = 'g'
        print(f"{key}: {resources[key]}{unit}")
    print(f"Money: ${money}")

def runMachine():
    drink_choice = input("What would you like? (latte, espresso, cappuccino: ")
    drink_selected = MENU[drink_choice]
    if check_resource_sufficiency(resources, drink_selected):
        ask_for_coins(drink_choice)
        deduct_resources(resources, drink_selected)
        printReport(resources, money)

while machine_on:
    # runMachine()
    # out_of_resources(resources)
    # print("---------------------",has_no_empty_resource(resources))
    if resources["water"] > 0 and resources["milk"] > 0 and resources["coffee"] > 0:
        runMachine()
    else:
        print("Machine is out of resources")
        machine_on = False


# while machine_on:
#     # runMachine()
#     # out_of_resources(resources)
#     for resource in resources:
#         # print("CHECK-->", resource)
#         # print(resources[resource])
#         if resources[resource] <= 0:
#             print("CHECK-->", resource)
#             print(resources[resource])
#             machine_on = False
#         else:
#             # print("CHECK-->", resource)
#             # print(resources[resource])
#             runMachine()


# def is_resource_sufficient(order_ingredients):
#     is_enough = True
#     for item in order_ingredients:
#         if order_ingredients[item] >= resources[item]:
#             print(f"Sorry there is not enough {item}")
#             is_enough = False
#     return is_enough


