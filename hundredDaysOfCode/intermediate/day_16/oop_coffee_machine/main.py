from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
menu = Menu()

print(f"What would you linke {menu.get_items()}")
coffee_maker.report()