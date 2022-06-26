from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

DRINK_PRICE = {
    "espresso": 1.5,
    "latte": 2.5,
    "cappuccino": 3.0
}
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

machine_is_on = True

while machine_is_on:
    drink = input(f"What would you like {menu.get_items()}: ")
    print(menu.find_drink(drink).ingredients['water'])
    water = menu.find_drink(drink).ingredients['water']
    milk = menu.find_drink(drink).ingredients['milk']
    coffee = menu.find_drink(drink).ingredients['coffee']
    cost = DRINK_PRICE[drink]

    if drink == "off":
        machine_is_on = False
    elif drink == "report":
        money_machine.report()
        coffee_maker.report()
    else:
        menu_item = MenuItem(drink, water, milk, coffee, cost)
        print(coffee_maker.is_resource_sufficient(menu_item))
        if not coffee_maker.is_resource_sufficient(menu_item):
            print(f"Sorry, there is not enough {menu_item}")
        else:
            if money_machine.make_payment(cost):
                coffee_maker.make_coffee(menu_item)
