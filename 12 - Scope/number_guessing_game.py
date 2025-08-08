import art
import random

def prompt_difficulty():
    """Asks and validates difficulty"""
    while True:
        d = input('>> Choose a difficulty. Type \'easy\' or \'hard\': ').lower()
        if d in ['easy', 'hard']:
            return d
        print('[X] Invalid choice. Try again.')

def prompt_number():
    """Asks and validates guess number"""
    while True:
        try:
            return int(input('>> Make a guess: '))
        except:
            print('[X] Invalid input. Try again.')

def prompt_play_again():
    """Asks and validates play again."""
    while True:
        choice = input('>> Do you want to play again? y or n?  ').lower()
        if choice not in ['y', 'n']:
            print('[X] Invalid input. Try again.')
        else:
            return choice == 'n'

def check_number(guess, num):
    """Checks if guess matches target number"""
    if guess == num:
        return True
    elif guess > num:
        print('[X] Number too high...')
        return False
    else:
        print('[X] Number too low...')
        return False

while True:
    # Initialize vars
    TARGET_NUMBER = random.randint(1, 100) # Target number to guess
    rounds = 0
    is_win = 0
    #  Print art
    print(art.logo)
    print('[!] I\'m thinking of a number between 1 and 100.')

    # Get and set difficulty
    if prompt_difficulty() == 'easy':
        rounds = 10
    else:
        rounds = 5

    # Game Loop
    while rounds > 0:
        print(f'\n[!] You have {rounds} attempts remaining to guess the number.')
        if check_number(prompt_number(), TARGET_NUMBER):
            print('[!] Correct Guess! You win!')
            is_win = 1
            break
        rounds -= 1

    # Checks if user lost
    if is_win == 0:
        print(f'[!] You lost :-(. The number is {TARGET_NUMBER} ')

    if prompt_play_again():
        break