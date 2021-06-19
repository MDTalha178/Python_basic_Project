from hangman_word import word_list
from hangman_art  import stages, logo
import random

print(logo)
choosen_word = random.choice(word_list)
word_length = len(choosen_word)


display =[]
for letter in choosen_word:
    display+= "_"

live = 6
game_finished = False


while not game_finished:
    guess = input("Guess  a letter")
    if guess in display:
        print("you have already guessed a letter")
        
    for position in range(word_length):
        letter = choosen_word[position]
        if guess == letter:
            display[position] = letter
    print(f"{' '.join(display)}")

    if guess not in choosen_word:
        print(f"You guessed {guess} that not in the word. you loose a life")
        live -=1
        if live ==0:
            game_finished = True
            print("You loose")

    if "_" not in display:
        game_finished = True
        print("Congrats you win")
    print(stages[live])

