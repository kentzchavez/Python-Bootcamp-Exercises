import random
import string
# Art and word list provided by the course.
stages = [r'''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', r'''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']
word_list = ["aardvark", "baboon", "camel"]

# Get a word from the list
def get_word():
    return random.choice(word_list)

# Print which of the hangman sprite should be shown
def print_hangman(lives):
    print(stages[6-lives])

# Displays hangman sprite and current word progress
def display_turn(word, lives, correct_guesses, guess):
    print(f'\n\n\n\n\n==================\nLIVES: {lives}\n==================')
    correct_guesses.append(guess)
    print_hangman(lives)
    placeholder = ''
    for letter in word:
      if letter in correct_guesses:
          placeholder += f'{letter.upper()} '
      else:
          placeholder += '_ '
    print(placeholder)

# Validates guess if input is correct or letter has not yet been given.
def validate_guess(letters, guess):
    # checks if user input contains more than 1 character
    if len(guess) > 1:
        print('[X] You may only type ONE letter. Try again.')
        return False
    
    # checks if user input has been given before
    if guess not in letters:
        print('[X] You have given this letter before! Try again.')
        return False
    return True

# Checks if guess is correct or wrong
def check_guess(word, guess):
    if guess in word:
        return True
    else:
        return False

# Check if user has already won the round.
def check_win(word, correct_guesses):
    placeholder = ''
    for letter in word:
        if letter in correct_guesses:
            placeholder += letter
    if placeholder == word:
        return True
    else:
        return False
  
# Game function
def start_game():
    # INIT Game environment
    lives = 6
    word = get_word()
    guess = '_'
    correct_guesses = []
    letters = string.ascii_lowercase
    display_turn(word, lives, correct_guesses, guess)

    #Start game loop
    while lives != 0:
      # Ask user for guess and validate
      while True:
        guess = input('\n[?] Give me a letter...\n>> ').lower()
        if validate_guess(letters, guess): # Guess is valid
            if check_guess(word, guess): # Guess is correct
              print('[!] Yes! Your guess is correct!')
              correct_guesses.append(guess)
              break
            else: # Guess is incorrect
              print(f'[!] The word does not have {guess}')
              lives -=1
              break
            
        else: # Guess is invalid
            continue  
      
      letters = [l for l in letters if l != guess] # Adjust letter list so previous turn wont be repeated
      display_turn(word, lives, correct_guesses, guess)

      # Check if user won
      if check_win(word, correct_guesses):
          print('[!] Congrats! You have guessed the word correctly and saved the man!')
          break
    # If user loset
    if lives == 0:
        display_turn(word, lives, correct_guesses, guess)
        print('[X] You failed to save the man :(, try again next time.')

def main():
  print("Let's play HANGMAN\n\n[?] Are you ready? y or n?")
  while True:
      choice = input(">> ").lower()
      if choice == 'y':
          start_game()
          break
      elif choice == 'n':
          print('[!] Alright, bye!')
          break  
      else:
          print("[X] Please input 'y' or 'n' only! Again. ")

main()

