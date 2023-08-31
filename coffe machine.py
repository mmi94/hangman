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
# TODO 1: what you want
# Todo 2: if there sufficient resources
# TODO 3: money



report ={"water": 300, "milk": 200, "coffee": 100, "Money": 0, }
def res_suffice(ingredients):
    for ingredient in ingredients:
        report[ingredient] -= ingredients[ingredient]
    return report

def money(cost):
    print('Please insert coins.')
    quarters = float(input('how many quarters?: '))
    dimes = float(input('how many dimes?: ')) #10
    nickles = float(input('how many nickles?: ')) # 5 cent
    pennies = float(input('how many pennies?: ')) #1 cent
    total = quarters / 4 + dimes /10 + nickles /20 + pennies / 100
    if total >= cost:
        change = total - cost
        print(f'Here is ${change} in change.')
        print(f'Here is your cappuccino ☕️. Enjoy!')
        report['Money'] += cost
    else:
        print('Sorry that\'s not enough money. Money refunded. ')
resources_sufficient = True
while resources_sufficient:
    choice = input('What would you like? (espresso/latte/cappuccino): ') #to know what they want

    if choice == 'report':
        for _ in report:
            print(_ , ':' , report[_])
    else:
        ingredients = MENU[choice]['ingredients'] #to know if the resources are sufficient and to reduce resources
        cost = MENU[choice]['cost'] #to know how much you have money and how much to refund

        if ingredients['water'] > report['water']:
            print('Sorry there is not enough water.')
            resources_sufficient = False
        else:
            res_suffice(ingredients)
            money(cost)

