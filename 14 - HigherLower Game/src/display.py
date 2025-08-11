import os
import src.lib.art as art

def clear_terminal():
    """Clears terminal, rather than using print(' ' * 20) lol"""
    os.system('cls' if os.name == 'nt' else 'clear')

def display_art():
    """Displays logo art"""
    print(art.logo)

def print_welcomeMsg():
    """Prints welcome message"""
    print('         W E L C O M E'
          '\n   Let\'s play Higher or Lower!')
    
def print_round(accounts, score, show_followers):
    """Prints a whole round"""
    clear_terminal()
    display_art()
    print(f'[!] Your current score is: {score}\n')

    # Person 1
    print(f'Compare A: {accounts[0]['name']}'
          f'\nDescription: {accounts[0]['description']}'
          f'\nCountry: {accounts[0]['country']}')
    if show_followers:
        print(f'Followers: {accounts[0]['follower_count']}')

    print(f'\n{art.vs}')

    # Person 2
    print(f'\nAgainst B: {accounts[1]['name']}'
          f'\nDescription: {accounts[1]['description']}'
          f'\nCountry: {accounts[1]['country']}')
    if show_followers:
        print(f'Followers: {accounts[1]['follower_count']}')


"""
SAMPLE DATA
    {
        'name': 'Instagram',
        'follower_count': 346,
        'description': 'Social media platform',
        'country': 'United States'
    }
"""