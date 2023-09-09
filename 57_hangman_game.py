import random
import hangman_word_list
import hangman_hangman_designs

lives=6
print("Welcome to the hangman game!!!\n")
chosen_word=random.choice(hangman_word_list.words)
display=[]
for i in range(len(chosen_word)):
    display+='_'
print(display)
game_over=False
while not game_over:
    guessed_letter=input("Guess the letter: ").lower()
    for position in range(len(chosen_word)):
        letter=chosen_word[position]
        if letter==guessed_letter:
            display[position]=guessed_letter
    print(display)

    if guessed_letter not in chosen_word:
        lives-=1
        if lives==0:
            game_over=True
            print("You Lose!")
    if '_' not in display:
        game_over=True
        print("You won!")
    print(hangman_hangman_designs.hangman[lives])
