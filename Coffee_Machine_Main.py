MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 18,
        },
        "cost": 3.00,
    }
}
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def calculate_moneys(quarter, dime, nickel, pennie):
    """Calculates total money entered in coins."""
    total = 0
    total += quarter * 0.25
    total += dime * 0.10
    total += nickel * 0.05
    total += pennie * 0.01
    return total


def output_message(paid, drink):
    "Returns drink and amount of change, Drink with no change, or not enough money message."
    global MENU
    price = MENU[drink]['cost']
    if paid > price:
        change = "{:.2f}".format(paid - price,2)
        return f"Here is your {drink}. Your change is ${change}."
    elif paid == price:
        return f"Here is your {drink}."
    elif paid < price:
        return f"You do not have enough money."

def resource_check(drink):
    """Checks to make sure the ingredients are available for drink before allowing insertion of Money."""
    ingredients = MENU[drink]['ingredients']
    # print(ingredients)
    can_make_drink = True
    resources_amount = 0
    ingredients_amount = 0
    for item in ingredients:
        ingredients_amount = ingredients[item]
        # print(f"Ingredient: {item}")
        # print(f"Amount: {ingredients_amount}")
        if item in resources:
            resources_amount = resources[item]
            # print(f"Resource: {item}")
            # print(f"Amount: {resources_amount}")
        if resources_amount < ingredients_amount:
            return False
    return can_make_drink

def update_resources(drink):
    """Updates the resources to subtract used resources from just made drink"""
    ingredients = MENU[drink]['ingredients']
    price = "{:.2f}".format(MENU[drink]['cost'])
    new_resources = { }
    for item in resources:
        resources_amount = resources[item]
        ingredients_amount = 0
        # print(item, resources_amount)
        if item in ingredients:
            ingredients_amount = ingredients[item]
            # print(item, ingredients_amount)
        new_resources[item.title()]= resources_amount - ingredients_amount
    new_resources['Money'] = "$"+price
    return (new_resources)

def coffee_machine():
    run_machine = True
    while run_machine == True:

# User Input Selection Validation
            user_choice = input("What would you like to drink? (Espresso/Latte/Cappuccino) or Done: ").lower()
            if user_choice == 'report':
                for key in resources:
                    print(f"{key}: {resources[key]}")
                valid_choice = False

            # If User inputs available choices
            elif user_choice in MENU.keys():
                # Checks if resources available to make item
                if resource_check(user_choice) == True:
                    drink_price = "{:.2f}".format(MENU[user_choice]['cost'])
                    print(f"You owe: ${drink_price}. Please insert coins.")
                    quarters = int(input("How many Quarters?: "))
                    dimes = int(input("How many Dimes?: "))
                    nickels = int(input("How many Nickels?: "))
                    pennies = int(input("How many Pennies?: "))
                    drink = user_choice
                    money_input = round(calculate_moneys(quarters, dimes, nickels, pennies), 2)
                    output = output_message(money_input, drink)
                    print(output)
                    resources = update_resources(user_choice)
                    valid_choice = False
                else:
                    print("")
            elif user_choice == 'done':
                print("Thank you for buying coffee.")
                run_machine = False
            else:
                print("That is not a valid choice")
                run_machine = False


coffee_machine()