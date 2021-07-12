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
profit =0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def resourses_is_sufficient(order_ingradient):
    for item in order_ingradient:
        if order_ingradient[item] >=resources[item]:
            return False
    return True

def process_coin():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total

def transaction_successful(money_received, cost_drink):
    if money_received >= cost_drink:
        change_amount = round(money_received - cost_drink)
        print(f"Here is ${change_amount} in change.")
        global profit
        profit+=cost_drink
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False

def make_coffee(drink_name, order_ingradient):
    for item in order_ingradient:
        resources[item] -= order_ingradient[item]

    print(f"Here is your {drink_name} ☕️. Enjoy!")
machine_on = True
while machine_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino):").lower()
    if user_choice == "off":
        machine_on = False
    elif user_choice == "report":
        print(f"water: {resources['water']} ml")
        print(f"milk: {resources['milk']} ml")
        print(f"coffee: {resources['coffee']} ml")
        print(f"Money: {profit} ml")
    else:
        drink = MENU[user_choice]
        if resourses_is_sufficient(drink["ingredients"]):
           payment =  process_coin()
           if transaction_successful(payment, drink["cost"]):
               make_coffee(user_choice, drink["ingredients"])

        

