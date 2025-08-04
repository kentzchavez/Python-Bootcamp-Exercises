import os
import art  # make sure this is available or replace it

def clear_terminal():
    """Clears terminal, rather than using print(' ' * 20) lol"""
    os.system('cls' if os.name == 'nt' else 'clear')

def show_display(u, d, show_all):
    """Shows blackjack display"""
    clear_terminal()
    print(art.logo)

    # Show dealer's set
    print("\nDEALER:")
    for i, card in enumerate(d.cards):
        if i == 0 or show_all:
            print(f"|{card}|", end=' ')
        else:
            print("|?|", end=' ')
    print(f"\nTotal: {d.cards[0] if not show_all else d.score}")

    # Shows user's set
    print("\nYOU:")
    for card in u.cards:
        print(f"|{card}|", end=' ')
    print(f"\nTOTAL: {u.score}\n")
