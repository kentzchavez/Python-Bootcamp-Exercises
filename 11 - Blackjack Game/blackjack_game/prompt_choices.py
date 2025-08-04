def get_yn_answer(prompt_text):
    """Displays and validates a yes/no prompt."""
    print(prompt_text)
    while True:
        choice = input(">> ").lower()
        if choice in ['y', 'n']:
            return choice == 'y'
        print("[X] You typed an invalid answer. Try again.")

def prompt_draw():
    """Prompts if the user wnats to draw another card"""
    return get_yn_answer("[?] Do you want to draw another card? Type 'y' if yes (HIT) or 'n' if no (STAND).")

def prompt_play_again():
    """Prompts if the user wants to play again."""
    return get_yn_answer("[?] Do you want to play again? Type 'y' if yes or 'n' if no.")
