import src.input_checker as InputC
import src.dialogue as Dlgs
import src.menu as Menu
import src.payment_manager as PaymentManager
import os

class CoffeeMachine(object):
    def __init__(self):
        # Initialize supplies
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100
        }

        # Initialize profit
        self.profit = 0.0

        # libraries
        self.inputCheck = InputC
        self.dialogues = Dlgs
        self.menu = Menu.MENU
        self.paymentManager = PaymentManager
    
    # OPEN1 Interaction
    def open(self):
        """Provides choice to the user if they want to order, close, or access admin."""
        while True:
            self.clear_terminal()
            print(self.dialogues.OPENING_WELCOME)
            choice = self.inputCheck.get_open1_choice()
            if choice == 1:
                self.order()
            elif choice == 2:
                self.close()
                break
            elif choice == 3:
                self.get_resources()

    def order(self):
        """Allows the user to order their coffee"""
        available_drinks = self.check_available_items()
        if available_drinks:
            print(self.dialogues.CHOOSE_ORDER)

            # Prints the current available drinks
            for x in range(len(available_drinks)):
                print(f'    ({x+1}). {available_drinks[x].capitalize()}')

            # Gets the order of the user.
            order = self.inputCheck.get_order(len(available_drinks))

            # Proceed with the payment.
            payment = self.paymentManager.process_payment(self.menu[available_drinks[x]]["cost"])
            if payment['status']:
                self.make_order(available_drinks[order])
                print(f'[!] Payment Received! Your order of {available_drinks[order]} is coming right up!')
                if payment['change']:
                    print(f'Here\'s your change: ₱{payment['change']}')
                x = input('\n[!] Please enter any key to get your receipt.')
            else:
                x = input('[X] You cancelled your order. Enter any key to continue.')
        else:
            print('[X] Unfortunately, the machine is out of stock, the management will restock soon!')
            x = input('[?] Please enter any key to proceed.')

    def close(self):
        """Closes coffee machines"""
        print(self.dialogues.CLOSE_MACHINE)

    def check_available_items(self):
        """CHecks which items are available to order in the menu given the resources."""
        available_items = [
            recipe for recipe, info in self.menu.items() # Gets the recipe (drink name) for each items in the menu, saving 'info' for other.
            if all(val <= self.resources[ingredient] for ingredient, val in info["ingredients"].items()) # Sorts out which of the recipes can be made given the available resources by comparing ingredients vs. resources.
        ]
        return available_items

    def make_order(self, order):
        """Makes the order (reduces the resources from the drink ingredients)"""
        for ingredient, value in self.menu[order]["ingredients"].items():
            self.resources[ingredient] -= value
        self.profit += self.menu[order]["cost"]
    
    def get_resources(self):
        print('[!] Coffee Machine Report:' \
        f'\nWater: {self.resources["water"]}ml' \
        f'\nMilk: {self.resources["milk"]}ml' \
        f'\nCoffee: {self.resources["coffee"]}g' \
        f'\n\nProfit: {self.profit}')

        x = input('[?] Please enter any key to proceed: ')
    
    def clear_terminal(self):
        """Clears terminal, rather than using print(' ' * 20) lol"""
        os.system('cls' if os.name == 'nt' else 'clear') 



cm = CoffeeMachine()
print(cm.open())
    