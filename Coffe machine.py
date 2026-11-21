MENU={
    "espresso":{
        "ingredients":{
            "water":50,
            "coffee":18,
        },
        "cost":1.5,
    },
    "latte":{
        "ingredients":{
            "water":200,
            "milk":150,
            "coffee":24,
        },
        "cost":2.5,
    },
    "cappuccino":{
        "ingredients":{
            "water":250,
            "milk":100,
            "coffee":24,
        },
        "cost":3.0,
    }
}
profit=0
recources={
    "water":300,
    "milk":200,
    "coffee":100,
}
def is_recourses_sufficient(order_ingredients):
    for item in order_ingredients:
       if order_ingredients[item]>=recources[item]:
           print(f"Sorry, there is not enough {item}.")
           return False
    return True
def process_coins():
    print("Please insert coins.")
    total=int(input("How many quarters?:")) * 0.25
    total+=int(input("How many dimes?:")) * 0.1
    total+=int(input("How many nickles?:")) * 0.05
    total+=int(input("How many pennies?:")) * 0.01
    return total

def is_transaction_successful(money_received, drink_cost):
    if money_received >= drink_cost:
        change = round(money_received-drink_cost,2)
        print(f"Here is ${change} in change.")
        global profit
        profit+=drink_cost
        return True
    else:
        print("Sorry, there is not enough money.")
        return False

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        recources[item]-=order_ingredients[item]
    print(f"Here is your {drink_name} ")
    print(" enjoy ")


is_on=True
while is_on:
    selection=input("What would you like?(espresso/latte/cappuccino):").lower()
    if selection=="report":
        print(f"water:  {recources['water']} ml")
        print(f"milk:   {recources['milk']} ml")
        print(f"coffee: {recources['coffee']} ml")
        print(f"money:  ${profit}")
        print("\n\n")
    elif selection=="off":
        is_on=False
    else:
        drink=MENU[selection]
        if is_recourses_sufficient(drink["ingredients"]):
            payment=process_coins()
            is_transaction_successful(payment,drink["cost"])
            make_coffee(selection,drink["ingredients"])











