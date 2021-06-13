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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

s1 = input("You are at the cross road Where do you want to go? Type 'Left' or 'Right' ").lower()
if s1 == 'Left':
    s2 = input("You come to a lake. There is island in the middle of the lake  Type 'wait' to 'wait' for a boat Type 'swim' to swim across").lower()
    if s2 == 'wait':
      s3 = input("You arrive at the unharmed. There is a house with 3 doors one 'red' one 'yellow' and one 'blue' Which color do you choose").lower()
      if s3== 'blue':
        print("You enter a room of beasts Game over!")
      elif s3== 'red':
          print("Its a room full of fire Game over!")
      else:
          print("Congratulations You found a treasure You win")
    else:
        print("Game over")
else:
    print("Game over")       