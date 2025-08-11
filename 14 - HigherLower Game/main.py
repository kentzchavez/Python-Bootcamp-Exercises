import src.display as display
import src.input_controls as inputc
from src.data_manager import DataManager

while True:
    display.display_art()
    display.print_welcomeMsg()
    
    if inputc.prompt_ready():
        # GAME LOOP START
        while True:
            score = 0
            acounts_manager = DataManager()
       
            # ROUNDS LOOP
            while len(acounts_manager.data) > 1:
                acounts_manager.get_accounts() # Get 2 accounts
                display.print_round(acounts_manager.accounts, score, False) # Display round UI without showing follower counts
                # Get and validate guess
                if acounts_manager.is_guess_correct(inputc.prompt_guess()): # If guess is correct
                    score += 1
                    display.print_round(acounts_manager.accounts, score, True)
                    input('[!] Your guess is CORRECT! Enter any key to continue!\n>> ')
                else: # If guess is wrong
                    display.print_round(acounts_manager.accounts, score, True)
                    print('[X] Your guess is WRONG!'
                          f'[!] FINAL SCORE: {score}')
                    break
            
            if acounts_manager.is_win(): # Checks if user won
                print('[!] CONGRATULATIONS YOU WON!')
            
            if inputc.prompt_playagain() != True: # Prompt to play again.
                break
              
    print('[!] Thanks for playing! ')
    break