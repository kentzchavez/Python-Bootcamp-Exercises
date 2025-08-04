from player import Player
from enums import BlackjackResult
from logic import check_blackjack, check_scores, is_final_result
from display import show_display
from prompt_choices import prompt_draw, prompt_play_again

while True:
    # Initialize user and dealer
    user = Player()
    dealer = Player()

    # Initialize status var with the dict results of check_blackjack()
    status = check_blackjack(user, dealer)

    # Check blackjack results
    if not is_final_result(status['result']):
        # Initial display if not blackjack
        show_display(user, dealer, False)
    
        while True:
            # Asks if thhe user wants to draw another card
            if prompt_draw():
                user.draw_card()
                if user.is_busted():
                    status = {'result': BlackjackResult.DEALER_WIN, 'message': '[!] BUSTED! You lost! :-('}
                    break
                show_display(user, dealer, False)
            else:
                break
        #Dealer's turn to draw cards
        while dealer.score < 17:
            dealer.draw_card()
            if dealer.is_busted():
                status = {'result': BlackjackResult.USER_WIN, 'message': '[!] DEALER BUSTED! You won! :-)'}
                break

    # Check the scores and end round.
    if status['result'] == BlackjackResult.CONTINUE: # If four, it means there's no case of blackjack/bust, so scores will be compared.
        status = check_scores(user, dealer) 

    # Final display
    show_display(user, dealer, True)
    print(status['message'])

    # Asks if the user wanna play again or not.
    if not prompt_play_again():
        print("[!] Thanks for playing! Goodbye!")
        break
