from coffee import MENU, resources
print(MENU)
print(resources)

money_value = 0
turn_off = False

def generate(value):
    return resources[value]

water_value = generate('water')
milk_value = generate('milk')
coffee_value = generate('coffee')

def cost(prop):
    return MENU[prop]['cost']

espresso_price = cost('espresso')
latte_price = cost('latte')
cappuccino_price = cost('cappuccino')

def cost(prop):
    return MENU[prop]['ingredients']

espresso_ingredients = cost('espresso')
latte_ingredients = cost('latte')
cappuccino_ingredients = cost('cappuccino')

def payment():
    print('Please insert coins.')
    total_payment = int(input('How many quarters?: ')) * 0.25
    total_payment += int(input('How many dimes?: ')) *  0.10
    total_payment += int(input('How many nickels?: ')) * 0.05
    total_payment += int(input('How many pennies?: ')) * 0.01
    total_payment = round(total_payment, 2)
    return total_payment

def report_res():
        print(f'Water: {water_value}ml 🧊')
        print(f'Milk: {milk_value}ml 🥛')
        print(f'Coffee: {coffee_value}g ☕')
        print(f'Money: ${money_value} 💵')


def calculate():
    global money_value, water_value, coffee_value, milk_value
    valid_responce = ['report', 'espresso', 'latte', 'cappuccino']

    if user_choice not in valid_responce:
        print('invalid Entry')
    else:
        if user_choice == 'espresso':
            if espresso_water >= 0 and espresso_coffee >= 0:
                total = payment()
                if total >= espresso_price:
                    change = total - espresso_price
                    change = round(change, 2)
                    money_value += espresso_price
                    water_value = espresso_water
                    coffee_value = espresso_coffee
                    print(f'Here is ${change} in change.\nHere is your {user_choice} ☕. Enjoy!')
                else:
                    print('Sorry that\'s not enough money. Money refunded')
            elif espresso_coffee < 0:
                print('Sorry there is not enough coffee')
            elif espresso_water < 0:
                print('Sorry there is not enough water')

        if user_choice == 'latte':
            if latte_water >= 0 and latte_coffee >= 0 and latte_milk >= 0:
                
                total = payment()
                if total >= latte_price:
                    change = total - latte_price
                    change = round(change, 2)
                    money_value += latte_price
                    water_value = latte_water
                    milk_value = latte_milk
                    coffee_value = latte_coffee
                    print(f'Here is ${change} in change.\nHere is your {user_choice} ☕. Enjoy!')
                else:
                    print('Sorry that\'s not enough money. Money refunded')
            elif latte_coffee < 0:
                print('Sorry there is not enough coffee')
            elif latte_water < 0:
                print('Sorry there is not enough water')
            elif latte_milk < 0:
                print('Sorry there is not enough milk')

        if user_choice == 'cappuccino':
            if cappuccino_water >= 0 and cappuccino_coffee >= 0 and cappuccino_milk >= 0:
                total = payment()
                if total >= cappuccino_price:
                    change = total - cappuccino_price
                    change = round(change, 2)
                    money_value += cappuccino_price
                    water_value = cappuccino_water
                    milk_value = cappuccino_milk
                    coffee_value = cappuccino_coffee
                    print(f'Here is ${change} in change.\nHere is your {user_choice} ☕. Enjoy!')
                else:
                    print('Sorry that\'s not enough money. Money refunded')
            elif cappuccino_coffee < 0:
                print('Sorry there is not enough coffee')
            elif cappuccino_water < 0:
                print('Sorry there is not enough water')
            elif cappuccino_milk < 0:
                print('Sorry there is not enough milk')

while not turn_off:
    espresso_water = water_value - espresso_ingredients['water']
    espresso_coffee = coffee_value - espresso_ingredients['coffee']
    latte_water = water_value - latte_ingredients['water']
    latte_milk = milk_value - latte_ingredients['milk']
    latte_coffee = coffee_value - latte_ingredients['coffee']
    cappuccino_water = water_value - cappuccino_ingredients['water']
    cappuccino_milk = milk_value - cappuccino_ingredients['milk']
    cappuccino_coffee = coffee_value - cappuccino_ingredients['coffee']
    user_choice = input('What would you like? (espresso/latte/cappuccino): ')
    user_choice = user_choice.lower()
    if user_choice == 'off':
        turn_off = True
        print('Enjoy your day!!')
    elif user_choice == 'report':
        report_res()
    else:
        calculate()
    



