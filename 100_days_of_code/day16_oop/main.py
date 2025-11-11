from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


print("Welcome to Coffee maker app...")

coffee_menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

def prepare_order(drink):
    if(coffee_maker.is_resource_sufficient(drink)):
        print(f"{drink.name} costs ${drink.cost}, Please Enter the Coins...")
        is_payment_done = money_machine.make_payment(drink.cost)
        if is_payment_done:
            coffee_maker.make_coffee(drink)
        else:
            print("insufficient payment done, Try again")
    else:
        print("Not enough resurces please try again late")
    

is_machine_on = True

while is_machine_on:
    customer_order = input(f"Please type in the drink name you want to have from {coffee_menu.get_items()} :")
    if coffee_menu.find_drink(customer_order):
        coffee = coffee_menu.find_drink(customer_order)
        print(coffee.name)
        prepare_order(coffee)
    elif customer_order == "report":
        coffee_maker.report()
    elif customer_order == "off":
        print("Turning machine off")
        is_machine_on : False
        break
    else:
        print("Invalid Item name please enter valid coffee name...")
