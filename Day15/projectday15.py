# Coffee Machine

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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

QUARTERS = 0.25
DIMES = 0.10
NICKLES = 0.05
PENNIES = 0.01


resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0

def report():
    print(f'''
        Water: {resources["water"]}ml
        Milk: {resources["milk"]}ml
        Coffee: {resources["coffee"]}g
        Money: ${money}
          ''')
    
def monetary_value():
    quarters = int(input("How many Quarters? : "))
    dimes = int(input("How many Dimes? : "))
    nickles = int(input("How many Nickles? : "))
    pennies = int(input("How many Pennies? : "))
    
    total_amount = (QUARTERS * quarters) + (DIMES * dimes) + (NICKLES * nickles) + (PENNIES * pennies)
    return round(total_amount, 2)

def espresso():
    global resources
    if resources["water"] >= MENU["espresso"]["ingredients"]["water"]:
        if resources["milk"] >=  MENU["espresso"]["ingredients"]["milk"]:
            if resources["coffee"] >= MENU["espresso"]["ingredients"]["coffee"]:
                
                payment = monetary_value()
                global money
                if payment == MENU["espresso"]["cost"]:
                    money += MENU["espresso"]["cost"]
                    resources = {
                    "water" :
                    resources["water"] - MENU["espresso"]["ingredients"]["water"],
                    "milk" : 
                    resources["milk"] - MENU["espresso"]["ingredients"]["milk"],
                    "coffee" : 
                    resources["coffee"] - MENU["espresso"]["ingredients"]["coffee"]
                    }
                    print("Here is your Espresso ☕️. Enjoy!")
                elif payment > MENU["espresso"]["cost"]:
                    change = payment - MENU["espresso"]["cost"]
                    money += MENU["espresso"]["cost"]
                    resources = {
                    "water" :
                    resources["water"] - MENU["espresso"]["ingredients"]["water"],
                    "milk" : 
                    resources["milk"] - MENU["espresso"]["ingredients"]["milk"],
                    "coffee" : 
                    resources["coffee"] - MENU["espresso"]["ingredients"]["coffee"]
                    }
                    print(f"Here is ${change} in change.")
                    print("Here is your Espresso ☕️. Enjoy!")
                else:
                    print("Sorry that's not enough money. Money refunded.")
            else:
                print("Sorry there is not enough Coffee")
        else:
            print("Sorry there is not enough Milk.")
    else:
        print("Sorry there is not enough Water.")
        
    
def latte():
    global resources
    if resources["water"] >= MENU["latte"]["ingredients"]["water"]:
        if resources["milk"] >=  MENU["latte"]["ingredients"]["milk"]:
            if resources["coffee"] >= MENU["latte"]["ingredients"]["coffee"]:
                
                payment = monetary_value()
                global money
                if payment == MENU["latte"]["cost"]:
                    money += MENU["latte"]["cost"]
                    resources = {
                    "water" :
                    resources["water"] - MENU["latte"]["ingredients"]["water"],
                    "milk" : 
                    resources["milk"] - MENU["latte"]["ingredients"]["milk"],
                    "coffee" : 
                    resources["coffee"] - MENU["latte"]["ingredients"]["coffee"]
                    }
                    print("Here is your Latte ☕️. Enjoy!")

                elif payment > MENU["latte"]["cost"]:
                    change = payment - MENU["latte"]["cost"]
                    money += MENU["latte"]["cost"]
                    resources = {
                    "water" :
                    resources["water"] - MENU["latte"]["ingredients"]["water"],
                    "milk" : 
                    resources["milk"] - MENU["latte"]["ingredients"]["milk"],
                    "coffee" : 
                    resources["coffee"] - MENU["latte"]["ingredients"]["coffee"]
                    }
                    print(f"Here is ${change} in change.")
                    print("Here is your Latte ☕️. Enjoy!")
                else:
                    print("Sorry that's not enough money. Money refunded.")
            else:
                print("Sorry there is not enough Coffee")
        else:
            print("Sorry there is not enough Milk.")
    else:
        print("Sorry there is not enough Water.")
        
    
def cappuccino():
    global resources
    if resources["water"] >= MENU["cappuccino"]["ingredients"]["water"]:
        if resources["milk"] >=  MENU["cappuccino"]["ingredients"]["milk"]:
            if resources["coffee"] >= MENU["cappuccino"]["ingredients"]["coffee"]:
                
                payment = monetary_value()
                global money
                if payment == MENU["cappuccino"]["cost"]:
                    money += MENU["cappuccino"]["cost"]
                    resources = {
                    "water" :
                    resources["water"] - MENU["cappuccino"]["ingredients"]["water"],
                    "milk" : 
                    resources["milk"] - MENU["cappuccino"]["ingredients"]["milk"],
                    "coffee" : 
                    resources["coffee"] - MENU["cappuccino"]["ingredients"]["coffee"]
                    }
                    print("Here is your Cappuccino ☕️. Enjoy!")
                elif payment > MENU["cappuccino"]["cost"]:
                    change = payment - MENU["cappuccino"]["cost"]
                    money += MENU["cappuccino"]["cost"]
                    resources = {
                    "water" :
                    resources["water"] - MENU["cappuccino"]["ingredients"]["water"],
                    "milk" : 
                    resources["milk"] - MENU["cappuccino"]["ingredients"]["milk"],
                    "coffee" : 
                    resources["coffee"] - MENU["cappuccino"]["ingredients"]["coffee"]
                    }
                    print(f"Here is ${change} in change.")
                    print("Here is your Cappuccino ☕️. Enjoy!")
                else:
                    print("Sorry that's not enough money. Money refunded.")
            else:
                print("Sorry there is not enough Coffee")
        else:
            print("Sorry there is not enough Milk.")
    else:
        print("Sorry there is not enough Water.")
        
    
# Execution

running = True
while running:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == 'off':
        running = False
        break
    elif choice == 'report':
        report()
    elif choice == 'espresso':
        espresso()
    elif choice == 'latte':
        latte()
    elif choice == 'cappuccino':
        cappuccino()
    else:
        print(f"{choice} is not available! Please check your selection.")
    