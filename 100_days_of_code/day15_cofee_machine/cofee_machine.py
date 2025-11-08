from art import coffee_machine

is_machine_on = True

stock = {
    "water": 200, "coffee":50, "milk":200, "Money":20
}

cofee_menu = {
    "Espresso": {"water":50 , "coffee":18, "milk":0, "Money":1.50},
    "latte":{"water":200, "coffee":24, "milk":150, "Money":2.50},
    "Cappucino":{"water": 200, "coffee":24, "milk":100, "Money":3}
}

#cofee menu with displaying all available cofee
def menu():
    print("What would you like to have?")
    index = 1
    for item in cofee_menu:
        print(f"{index}. {item}: $ {cofee_menu[item]["Money"]}")
        index += 1
    print("4. Cancel the process")
    return int(input("Enter item number from the menu: "))


#generate report on stocks
def generate_report():
    print("\nAvailable ingrediants:")
    print(f"1. Water: {stock['water']} ml \n2. Coffee: {stock['coffee']} g\n3. Milk: {stock['milk']} ml\n4. Money: {stock['Money']}")


#deduct charges for making that drink
def deduct_charges(drink_name):
    print("")
    print(f"Cutting charges for {drink_name}")
    quarters = int(input("Enter quarters: "))
    dimes = int(input("Enter dimes: "))
    nickles = int(input("Enter nickles: "))
    pennies = int(input("Enter Pennies: "))
    final_total = quarters*0.25 + dimes*0.10 + nickles*0.05 + pennies*0.01

    if final_total >= cofee_menu[drink_name]["Money"]:
        change = final_total - cofee_menu[drink_name]["Money"]
        final_total = final_total - change
        print(f"\nReturning Change ${change}")

        stock["Money"] += final_total
        print(f"Payment Processed, Enjoy the {drink_name}")
    else:
        print("Issuing Refund !! You fell short off Money")

#select the drink and call preparing function to prepare drink
def select_and_prepare_drink(choice):
    global is_machine_on
    if choice == 0:
        generate_report()
    elif choice == 1:
        prepare_order("Espresso")
    elif choice == 2:
        prepare_order("latte")
    elif choice == 3:
        prepare_order("Cappucino")
    elif choice == 4:
        is_machine_on=False

#compare required stock to avaialbe stock
def check_stock(drink_name):
    for item in stock:
        if cofee_menu[drink_name][item] > stock[item]:
            return True


#deduct resources
def deduct_resources(drink_name):
    for item in stock:
        if item == "Money":
            continue
        stock[item] -= cofee_menu[drink_name][item]

#prepare the order
def prepare_order(drink_name):
    if check_stock(drink_name):
        print("\nIngredient is not avaialable, cant cook that")
    else:
        deduct_charges(drink_name)
        deduct_resources(drink_name)

print(coffee_machine)
while is_machine_on:
    print("\n")
    choice = menu()
    select_and_prepare_drink(choice)
    print("\n\nThanks for Using the coffee machine \n")