import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
n_letters = int(input("How many letters would you like in your password?\n"))
n_symbols = int(input(f"How many symbols would you like?\n"))
n_numbers = int(input(f"How many numbers would you like?\n"))


# Easy Version -- letters+symbols+numbers
pw = ''
# Get letters
for num in range(n_letters):
    pw += random.choice(letters)
# Get symbols
for num in range(n_symbols):
    pw += random.choice(symbols)
# Get numbers
for num in range(n_numbers):
    pw += random.choice(numbers)

# Hard version -- randomized
pw = list(pw) # Transform the password to a list
random.shuffle(pw) # Use shuffle function on the list
pw = "".join(pw) # turn the pw list back to string

print(f'Your password is: {pw}')