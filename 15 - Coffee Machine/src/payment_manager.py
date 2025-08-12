from enum import IntEnum
import src.input_checker as InputC

class Coins(IntEnum):
    """Classifies the number of coins"""
    PISO = 1
    LIMA = 5
    SAMPU = 10
    BENTE = 20

class PaymentStatus(IntEnum):
    """Classifies payment status"""
    PAID = 1
    CANCELED = 0

def display_ui(bal, price):
    print(f"""[?] What coins would you like to insert? Please enter appropriate number within the options.
    (1). Piso - ₱1
    (2). Lima - ₱5
    (3). Sampu - ₱10
    (4). Bente - ₱20
    
    (5). Cancel Order
    (6). Proceed
    
Balance Inserted: ₱{bal}
Remaining To Pay: ₱{price}

""")
    
def process_payment(price):
    bal = 0
    change = 0
    status = ''
    quantity = 0
    message = ''
    while True:
        display_ui(bal, price)
        # Step 1 of Payment get coin value
        if message:
            print(message)
            message = ''
        coin_value = InputC.get_coin_value()

        if coin_value == 5: # User cancelled their payment
            change = 0
            status = PaymentStatus.CANCELED
            break
        elif coin_value == 6: # User proceeds with their payment
            if bal < price:
                message = '[X] You still have a remaining balance, you cannot proceed yet.'
            else:
                status = PaymentStatus.PAID
                break
        else:
            # Step 2 of Payment get coin quantity
            quantity = InputC.get_coin_quantity()
        
        # Calculate
        if quantity != 0:
            bal, price, change = calculate_balance(bal, price, coin_value, quantity)

    return {"status": status, "change": change}

def calculate_balance(bal, price, coin_value, quantity):
    if coin_value == 1:
        coin_amount = Coins.PISO
    elif coin_value == 2:
        coin_amount = Coins.LIMA
    elif coin_value == 3:
        coin_amount = Coins.SAMPU
    else:
        coin_amount = Coins.BENTE

    total = coin_amount * quantity
    bal += total

    remaining_price = max(price - total, 0)
    change = max(total - price, 0)

    return bal, remaining_price, change

