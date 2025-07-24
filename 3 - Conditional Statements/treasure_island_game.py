print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure. Type the number of the choice you'd like to proceed with if prompted ")
print("[?] There are two paths ahead, which way would you go? \n[1] Left \n[2] Right")
choice = input(">> ")
if choice == '1':
    print("[?] You chose the correct path and gained an access to a suspicious lake. What would you do?\n[1] Swim right away towards the other side \n[2] Wait for a while before swimming")
    choice = input(">> ")
    if choice == '2':
        print("[?] ou swam safely towards the land and was met with a magical wall containing three doors, which of the doors are you going to enter?\n[1] Red door\n[2] Yellow door\n[3] Blue door")
        choice = input(">> ")
        if choice == '1':
            print("[!] Upon entering the red door, it disappeared behind you and suddenly, your surroundings started to burn with no escape for you.\n\nGAME OVER")
        elif choice == '2':
            print("[O] Upon entering the yellow door, you saw a bright glowing light upon the end of the hall, you approached it and found the treasure!!!\n\nYOU WON!")
        elif choice == '3':
            print("[!] Upon entering the blue door, it disappeared behind you and suddenly, beasts appeared before you, looking menacing and hungry towards you.\n\nGAME OVER")
        else:
            print("[!] You decided to turn back and give up on your quest... No treasure for you.\n\nGAME OVER")
    else:
        print("[!] While swimming, you were attacked by a school of hungry trout!\n\nGAME OVER")
else:
    print("[!] While walking, you stepped on a bunch of fallen leaves, not realizing that it's a trap and there's a deep hole below which you fell in.\n\nGAME OVER")


