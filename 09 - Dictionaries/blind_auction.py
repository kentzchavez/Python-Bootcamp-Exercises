bids = {}
# TODO-1: Ask the user for input
while True:
    name = input('[?] What is your name?\n>> ')
    price = 0

    while True:
        try: # Gotta ensure that the price that the user will enter is valid
            price = int(input(f'[?] Got it {name}! What is your bid?\n>> '))
            break
        except:
            print('[X] You entered an invalid value. Please try again...')

    # TODO-2: Save data into dictionary {name: price}
    # Put values in the dictionary
    bids[name] = price
    print('[O] Bid successfully placed!\n')

    # TODO-3: Whether if new bids need to be added
    choice = ''
    # Check if choice is valid
    while True:
        choice = input('[?] Is there going to be another bid from another person? Type \'y\' if yes, otherwise type \'n\'\n>> ')
        if choice not in ['y', 'n']:
            print('[X] You have typed an invalid choice. Please try again.')
        else:
            break
    print('\n' * 20)
    if choice == 'n':
        break
    # Prompt if there will be other bids

# TODO-4: Compare bids in dictionary
best_bid = {'name': 'none', 'bid': 0}
for name, bid in bids.items():
    if bid > best_bid['bid']:
        best_bid['name'] = name
        best_bid['bid'] = bid

print(f'[!] The highest bidder is {best_bid['name']} with a bid of ${best_bid['bid']}.')