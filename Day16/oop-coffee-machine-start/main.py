# Coffee machine project with OOP concepts

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker_obj = CoffeeMaker()
money_machine_obj = MoneyMachine()
menu_obj = Menu()

running = True
while running:
    choice = input(f"What would you like? ({menu_obj.get_items()}): ")
    if choice == 'off':
        running = False
    elif choice == 'report':
        coffee_maker_obj.report()
        money_machine_obj.report()
    else:
        drink = menu_obj.find_drink(choice)
        if coffee_maker_obj.is_resource_sufficient(drink) and money_machine_obj.make_payment(drink.cost):
            coffee_maker_obj.make_coffee(drink)
