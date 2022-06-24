from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()
machine_is_on = True
while machine_is_on:
    drink = input(f"What would you linke {menu.get_items()}: ")
    if drink == "off":
        machine_is_on = False
    coffee_maker.report()