MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
            "milk":0
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
    "change_money": 10.0,
    "profit":0
}

off = False

def print_resources():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]
    profit = resources["profit"]
    change_money = resources["change_money"]
    print(f"Water: {water}ml\nMilk: {milk}ml\nCoffe: {coffee}g\nProfit: ${profit}\nChange money :${change_money}")

def charge(choice):

    coffe_cost = MENU[choice]["cost"]

    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.10
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01

    if total < coffe_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    elif total > coffe_cost:
        change = round(total - coffe_cost,2)
        resources["profit"] += float(coffe_cost)
        resources["change_money"] -= change
        resources["change_money"] += coffe_cost
        print(f"Your change is : '${change}'")

        return True
    elif coffe_cost == total:
        change += round(total - coffe_cost, 2)
        resources["change_money"] -= change
        resources["profit"] += float(coffe_cost)

        return True

def make_coffee(choice):
    water_cost = MENU[choice]["ingredients"]["water"]
    milk_cost = MENU[choice]["ingredients"]["milk"]
    coffee_cost = MENU[choice]["ingredients"]["coffee"]

    for item in MENU[choice]["ingredients"]:
        if MENU[choice]["ingredients"][item] > resources[item]:
            print(f"Sorry, theres not enough {item}")
            global off
            off = True
            return
    if charge(choice) == True:
        resources["water"] -= water_cost
        resources["coffee"] -= coffee_cost
        resources["milk"] -= milk_cost
        print("Enjoy your coffee!")


while not off:

    while True:
        choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if choice != "cappuccino" and choice != "espresso" and choice != "latte" and choice != "report" and choice != "off":
            print("You must choose between the three options of coffee.")
        else:
            break

    if choice == "report":
            print_resources()

    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
                make_coffee(choice)


    else:
        off = True
