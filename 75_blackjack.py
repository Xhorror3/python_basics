import os
import random
# from replit import clear
from backjack_art import logo

def deal_card():
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  return random.choice(cards)
  
def calculate_score(card):
  if sum(card)==21 and len(card)==2:
    return 0

  if 11 in card and sum(card)>21:
    card.remove(11)
    card.append(1)
  return sum(card)
  
def compare(user_score,computer_score):
  if user_score>21 and computer_score>21:
    return "You went over. You lose!"
  if user_score==computer_score:
    print("Draw!")
  elif computer_score==0:
    print("You lose!Computer has black jack.")
  elif user_score==0:
    print("You win!You got a black jack.")
  elif user_score>21:
    print("You lose! You went over.")
  elif computer_score>21:
    print("You win! Computer went over.")
  elif user_score>computer_score:
    print("You win! Your total is greater than computer.")
  else:
    print("You lose! Your total is less than opponent.")
def play_game():
  print(logo)
  
  user_cards = []
  computer_cards = []
  is_game_over=False
  
  for _ in range(2):
    user_cards.append(deal_card())
    computer_cards.append(deal_card())
  while not is_game_over:
    user_score=calculate_score(user_cards)
    computer_score=calculate_score(computer_cards)
    
    print(f" User cards: {user_cards}, current_score: {user_score}")
    print(f" Computer's first card: {computer_cards[0]}")
    
    if user_score==0 or computer_score==0 or user_score>21:
      is_game_over=True
    else:
      user_should_deal=input("Enter 'y' to get another card, enter 'n' to pass: ")
      if user_should_deal=='y':
        user_cards.append(deal_card())
      else:
        is_game_over=True
  
  while computer_score!=0 and computer_score<17:
    computer_cards.append(deal_card())
    computer_score=calculate_score(computer_cards)
  
  print(f" Your final card deck is {user_cards} and your score is {user_score}.")
  print(f" Computer's final card deck is {computer_cards} and your score is {computer_score}.")
  print(compare(user_score,computer_score))
  
while input("Do you want to play game of blackjack? Type 'y' or 'n': ")=="y":
#   clear()
  os.system('cls')
  play_game()

