# Welcome message
print("Welcome to the Treasure Island.")
print("Your mission is to find the treasure")

# picture
print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
      ''')


# logic
choice = input(
    'You\'re at a cross road. Where do you want to go?\nType "left" or "right:"').lower()
if choice == "left":
    second_choice = input("You've come to a lake. There is an island in the middle of the lake.\n"
                          "Type wait to wait for a boat or swim to swim across:").lower()
    if second_choice == "wait":
        third_choice = input("You arrive at the island unharmed. There is a house with three doors.\n"
                             "One is Yellow, one is Red and one is Blue.\n"
                             "Which colour do you choose? Type yellow, red or blue: ").lower()
        if third_choice == "yellow":
            print("You win!")
        elif third_choice == "red":
            print("Burned by fire\nGame over")
        elif third_choice == "blue":
            print("Eaten by beasts\nGame over")
    else:
        print("Attacked by trout")
        print("Game over")
else:
    print("Fall into a hole")
    print("Game over")
