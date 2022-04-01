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


# TODO: 1 - Input prompt "What would you like?"
# TODO: 2 - Print "Please insert coins"
# TODO: 3 - Prompt "How many quarters"
# TODO: 4 - Prompt "How many dimes"
# TODO: 5 - Prompt "How many nickles"
# TODO: 6 - Prompt "How many pennies"
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