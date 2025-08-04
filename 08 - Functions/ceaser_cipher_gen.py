import string
alphabet = string.ascii_lowercase
direction = ''
text = ''
shift = 0

# Handles text encryption
def encrypt(original_text, shift_amount):
    encrypted_text = ''
    for l in original_text:
        encrypted_text += alphabet[(alphabet.index(l) + shift_amount) % len(alphabet)] # Modulo to ensure index clarity
    print(f'[ ] The encoded version of the original text is: {encrypted_text}')

# Handles text decryption
def decrypt(encrypted_text, shift_amount):
    decrypted_text = ''
    for l in encrypted_text:
        decrypted_text += alphabet[(alphabet.index(l) - shift_amount) % len(alphabet)] # Modulo to ensure index clarity
    print(f'[ ] The decrypted version of the encrypted text is: {decrypted_text}')

def main():
    while True:
        direction = input("[!] Type 'encode' to encrypt, type 'decode' to decrypt:\n>> ").lower()
        
        if direction in ['encode', 'decode']:
            text = input("[!] Type your message:\n>> ").lower()
            shift = int(input("[!] Type the shift number:\n>> "))

            if direction == 'encode':
                encrypt(text,shift)
            elif direction == 'decode':
                decrypt(text, shift)
        else:
            print('[X] You typed an invalid choice')
            continue

        choice = ''
        while True:
            choice = input('[?] Would you like to try another text? Type \'y\' or \'n\'.\n>> ')
            if choice in ['y', 'n']: break
            print('[X] You typed an invalid choice')
        if choice =='n':
            print('[!] Okay, goodbye!')
            break

main()

