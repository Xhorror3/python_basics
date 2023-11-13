#Number Guessing Game Objectives:
import random
random_num=random.randint(1,100)
# Include an ASCII art logo.
from guess_number_art import logo
print(logo)
print("Welcome to the number guessing game:")
# Allow the player to select a difficulty.
print("I'm thinking of the number between 1 to 100")
difficulty=input("Choose a difficulty: e for easy or h for hard: ")
chances=0
if difficulty=="e":
  chances=10
elif difficulty=="h":
  chances=5
else:
  print("Please enter a valid difficulty")
  exit()


while chances!=0:
  number=int(input("Guess a number:"))
  # Ask the player to guess the number.
  # Allow the player to submit a guess for a number between 1 and 100.
  # Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
  if number>random_num:
    print("Too high")
  elif number<random_num:
    print("Too low")
  else:
    print(f"You got it! The answer was {random_num}.")
    exit()

  chances-=1
  if chances==0:
    print("You lost the game.")
  else:
    print(f"You have {chances} chances left to guess a number.\nGuess again.")

  # If they got the answer correct, show the actual answer to the player.
  # Track the number of turns remaining.
  # If they run out of turns, provide feedback to the player. 
  # Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
  
