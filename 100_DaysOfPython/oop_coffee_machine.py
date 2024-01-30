from coffee_data import Menu, MenuItem, CoffeeMaker, MoneyMachine
money_machine = MoneyMachine()
coffee_machine = CoffeeMaker()
menu = Menu()

is_machine_on = True
while is_machine_on:
    option = menu.get_items()
    coffee_choice = input(f"What would you like({option}): ")
    if coffee_choice == 'off' or coffee_choice == 'OFF' or coffee_choice == 'Off':
        is_machine_on = False
    elif coffee_choice == 'report' or coffee_choice == 'REPORT' or coffee_choice == 'Report':
        coffee_machine.report()
        money_machine.report()
    else:
        drink_type = menu.find_drink(coffee_choice)
        if coffee_machine.is_resource_sufficient(drink_type) and money_machine.make_payment(drink_type.cost):
                coffee_machine.make_coffee(drink_type)