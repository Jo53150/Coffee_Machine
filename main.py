from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_on = True

menu = Menu()

making_coffee = CoffeeMaker()

payment = MoneyMachine()

while machine_on == True:
    print(menu.get_items())
    order = (input("What would you like? (espresso/latte/cappuccino): "))
    if order == "report":
        making_coffee.report()
        payment.report()
    elif order == "off":
        print("Coffee Machine turning off...")
        machine_on = False    
    else:    
        coffe = menu.find_drink(order)
        if making_coffee.is_resource_sufficient(coffe) == True:
            if payment.make_payment(coffe.cost) == False:
                pass
            else:    
                making_coffee.make_coffee(coffe)
        else:
            pass     
    