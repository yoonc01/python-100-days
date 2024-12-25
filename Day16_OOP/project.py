from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
is_on = True

while (is_on):
    options = menu.get_items()
    choice = input(f"What would you like? ({options}): ")
    if choice == "off":
        # turn off the machine
        is_on = False
    elif choice == "report":
        # Print report
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if drink == None:
            continue
        elif (coffee_maker.is_resource_sufficient(drink) and  money_machine.make_payment(drink.cost)):
            coffee_maker.make_coffee(drink)
