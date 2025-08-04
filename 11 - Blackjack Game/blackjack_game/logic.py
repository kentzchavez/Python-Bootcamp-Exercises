from enums import BlackjackResult

def check_blackjack(u, d):
    """Checks for blackjack cases"""
    user_b = u.has_blackjack()
    dealer_b = d.has_blackjack()

    if user_b and dealer_b:
        return {'result': BlackjackResult.TIE, 'message': "[!] It's a tie!"}
    elif user_b:
        return {'result': BlackjackResult.USER_WIN, 'message': "[!] YOU GOT A BLACKJACK! YOU WON! :-)"}
    elif dealer_b:
        return {'result': BlackjackResult.DEALER_WIN, 'message': "[!] DEALER GOT A BLACKJACK! YOU LOST! :-("}
    else:
        return {'result': BlackjackResult.CONTINUE, 'message': ''}

def check_scores(u, d):
    """Compares the scores of the two."""
    if u.score > d.score:
        return {'status': BlackjackResult.USER_WIN, 'message': "[!] Congratulations! You won! :-)"}
    elif u.score < d.score:
        return {'status': BlackjackResult.DEALER_WIN, 'message': "[!] You lost! :-("}
    else:
        return {'status': BlackjackResult.TIE, 'message': "It's a tie!"}

def is_final_result(result):
    """Checks whether results are final or scores has to be compared"""
    return result != BlackjackResult.CONTINUE
