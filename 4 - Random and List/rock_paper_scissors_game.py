import random

# Init scores & art
user_score = 0
comp_score = 0

# Add score to the computer
def comp_wins():
    global comp_score
    print("[X] The score is for me! :P")
    comp_score += 1

# Add score to the user
def user_wins():
    global user_score
    print("[!] The score is for you! Nice!")
    user_score += 1

# Artworks provided by the course
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Welcome the player
print("[!] Let's play rock, paper, and scissors! How many rounds do you want (input an integer)?")

# Determine rounds for the user
rounds = 0
while True:
    try:
        rounds = int(input(">> "))
        if rounds == 0:
            print("You're so silly! You don't want to play with me? Let me ask you again...")
        else:
            break
    except:
        print('[X] You should input an integer!')

rps = [rock, paper, scissors]
print("[!] Let's Start!")

# Game loop
while rounds != 0:
    # Ask user to select turn
    user_turn = ''
    while True:
        print("[?] (1) Rock, (2) Paper, or (3) Scissors?")
        user_turn = input(">> ")

        # Determine if user input is valid
        if user_turn not in ['1', '2', '3']:
            print("[X] Invalid choice, let me ask you again...")
        else:
            user_turn = int(user_turn)-1
            print(f"Your turn:\n\n{rps[user_turn]}")
            break

    # Get computer turn
    comp_turn = random.randint(0,2)
    print(f"\nComputer turn:\n\n{rps[comp_turn]}")

    # Analyze Turn
    turn = [user_turn, comp_turn]
    comp_win = [[0,1], [1,2], [2,0]]
    if user_turn == comp_turn:
        print("[!] It's a tie!")
    elif turn in comp_win:
        comp_wins()
    else:
        user_wins()

    # End round
    rounds -= 1

# Conclusion -- Show scores
print("\nThe scores are.....")
print(f"[YOU]: {user_score}")
print(f"[COMPUTER]: {comp_score}")

# Compare Scores
if user_score == comp_score:
    print('Yup... It is a tie between us, I guess we are both good!')
elif user_score > comp_score:
    print('You won!!!!!')
else:
    print('I won! Try again next time :P')
