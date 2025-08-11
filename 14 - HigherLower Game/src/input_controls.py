def prompt_yes_no(question):
    """Prompts a yes or no question to the user returning True if answer is yes"""
    print(f'\n{question}')
    while True:
        choice = input('>> ').lower()
        if choice not in ['yes', 'no']:
            print('[X] Invalid input. Try again.')
            continue
        elif choice == 'yes':
            return True
        return False
    
def prompt_ready():
    """PRompts if user is ready to play"""
    return prompt_yes_no('[?] Are you ready? Type \'yes\' or \'no\'.')
    
def prompt_guess():
    """Prompts the guess of the user"""
    print('[?] Who as more followers? Type \'A\' or \'B\'.')
    while True:
        choice = input('>> ').lower()
        if choice not in ['a', 'b']:
            print('[X] Invalid input. Try again.')
            continue
        return choice
    
def prompt_playagain():
    """PRompts if user is ready to play"""
    return prompt_yes_no('[?] Do you want to play again? Type \'yes\' or \'no\'.')