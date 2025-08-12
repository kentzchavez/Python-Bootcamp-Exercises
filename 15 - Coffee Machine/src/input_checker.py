INVALID_MESSAGE = '[X] Invalid input, please try again.'

def get_open1_choice():
    """Gets and validates input for OPEN1 Interaction"""
    while True:
        choice = input('\n>> ')
        if choice in ['1', '2', '3']:
            return int(choice)
        print(INVALID_MESSAGE)
    
def get_order(x):
    """Gets and validates input for choosing an order."""
    while True:
        try:
            choice = int(input('\n>> '))-1
            if choice in range(x):
                return choice
            else:
                print(INVALID_MESSAGE)
        except ValueError:
            print(INVALID_MESSAGE)

def get_coin_value():
    """Gets and validates coin value for STEP 1 of payment"""
    while True:
        try:
            choice = int(input('>> '))
            if choice in range(1, 7):
                return choice
            print(INVALID_MESSAGE)
        except ValueError:
            print(INVALID_MESSAGE)

def get_coin_quantity():
    """Gets and validates coin quantity for STEP 2 of payment"""
    while True:
        try:
            quantity = int(input('[?] How many are you inserting?\n>> '))
            return quantity
        except ValueError:
            print(INVALID_MESSAGE)

