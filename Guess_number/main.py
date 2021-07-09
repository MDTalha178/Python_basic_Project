import random
from art import logo
print("Welcome to the gussing number")
print(logo)

computer_thinking = random.randint(1,101)
print(computer_thinking)

Hard_level = 5
easy_level = 10

def easy_choice():
    print("You have 10 attempts to guess the number")
    level =0
    turns = easy_level
    while level <10:
        count =1
        # remaining_chance =0
        user_guess = int(input("Make a guess"))
        if user_guess >computer_thinking:
            print("Its too high \n Guess again")
            count += 1
            turns -= count
            print(f"You have {turns}  chance to guess: ")
            level+=1
            if turns ==0:
                print(f"You loose! The number is {computer_thinking}")
        elif user_guess < computer_thinking:
            print("Its too low")
            count+=1
            turns -= count
            print(f"You have {turns} chance to guess")
            level+=1
            if turns ==0:
                print(f"You loose! The number is {computer_thinking}")
        else:
            print("You win!")
            return
            

def hard_choice():
    print("You have 5 attempts to guess the number ")
    level =0
    turns = Hard_level
    while level < 5:
        count =0
        user_guess = int(input("Make a guess: "))
        if user_guess >computer_thinking:
            print("Its too high \n guess again")
            count += 1
            turns -= count
            print(f"You have {turns} chance to guess")
            level+=1
            if turns ==0:
                print(f"You loose! The number is {computer_thinking}")
        elif user_guess < computer_thinking:
            print("Its too low")
            count+=1
            turns -= count
            print(f"You have {turns} chance to guess")
            level+=1
            if turns ==0:
                print(f"You loose! The number is {computer_thinking}")
        else:
            print("You win!")
            return

        




user_choice = input("Choose a difficulty type 'easy' or 'hard'")
if user_choice == "easy":
    easy_choice()
else:
    hard_choice()
    # hard_choice()




