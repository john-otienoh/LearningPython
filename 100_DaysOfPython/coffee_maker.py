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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def resources_checker(ingredients):
    is_ingredient_enough = True
    for ingredient in ingredients:
        if ingredients[ingredient] >= resources[ingredient]:
            print(f"Sorry there is not enough {ingredient}")
            is_ingredient_enough = False
    return is_ingredient_enough
def coin_value():
    """Returns the total coins"""
    print("Insert coins")
    q_coin = int(input("How many Quarters?: ")) * 0.25
    d_coin = int(input("How many Dimes?: ")) * 0.1
    n_coin = int(input("How many Nickels?: ")) * 0.05
    p_coin = int(input("How many Pennies?: ")) * 0.01
    return q_coin + d_coin + n_coin + p_coin
def make_coffee(drink_name, ingredients):
    for ingredient in ingredients:
        resources[ingredient] -= ingredients[ingredient]
    print(f"Here is your {drink_name}")
is_machine_on = True

while is_machine_on:
    coffee_choice = input("What would you like to order? (espresso, latte, cappuccino): ")
    if coffee_choice == 'off' or coffee_choice == 'OFF' or coffee_choice == 'Off':
        is_machine_on = False
    elif coffee_choice == 'report' or coffee_choice == 'REPORT' or coffee_choice == 'Report':
        print(f"Water: {resources['water']}ml\nMilk: {resources['milk']}ml\nCoffee: {resources['coffee']}g\nMoney: ${profit}")
    else:
        drink_type = MENU[coffee_choice]
        if resources_checker(drink_type['ingredients']):
            payment = coin_value()
            if payment >= drink_type['cost']:
                profit += drink_type['cost']
                change = round(payment - drink_type['cost'], 2)
                make_coffee(coffee_choice, drink_type['ingredients'])
                print(f"Here is ${change} dollars in change.")
            else:
                print("Sorry that's not enough money. Money refunded.")