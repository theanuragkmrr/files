
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
profit=0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_sufficient(ing):
    for i in ing:
        if ing[i] >= resources[i]:
            print(f"Sorry Resources insufficient{i}")
            return False
    return True

def coin():
    print("Insert coins.")
    total=int(input("How many quarters you have? ")) * 0.25
    total+=int(input("How many dimes you have? ")) * 0.1
    total+=int(input("How many nickels you have? ")) * 0.05
    total+=int(input("How many pennies you have? ")) * 0.01
    return total

def trans(money_received,drink_cost):
    if money_received>=drink_cost:
        change=round(money_received-drink_cost,2)
        print(f"Here is your change {change}")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry money is not enough.")
        return False

def make_coffee(drink_name,ing):
    for i in ing:
        resources[i]=resources[i]-ing[i]
    print("YOUR COFFEE IS READY ENJOY!❤")


is_on=True

while is_on:
    choice=input("What would you like: ")
    if choice=="off":
        is_on=False
    elif choice=="report":
        Water=resources["water"]
        Milk=resources["milk"]
        Coffee=resources["coffee"]

        print(f"Water:{Water}ml\nMilk:{Milk}ml\nCoffee:{Coffee}g\nMoney:{profit}")
    else:
        drink=MENU[choice]
        if is_sufficient(drink["ingredients"]):
            payment=coin()
            if trans(payment,drink["cost"]):
               make_coffee(choice,drink["ingredients"])


