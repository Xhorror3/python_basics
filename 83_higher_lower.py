import random
from higher_lower_art import logo,vs
from higher_lower_data import data
import os


def format_data(account):
  account_name=account["name"]
  account_description=account["description"]
  account_country=account["country"]
  return f"{account_name}, a {account_description}, from {account_country}"

def check_answer(guess,a_follower_count,b_follower_count):
  if a_follower_count>b_follower_count:
    return guess=="a"
  else:
    return guess=="b"

print(logo)
score=0
should_continue=True
account_b=random.choice(data)

while(should_continue):
  account_a=account_b
  account_b=random.choice(data)
  
  while account_a==account_b:
    account_b=random.choice(data)
  
  print(f"Compare A:{format_data(account_a)}")
  print(vs)
  print(f"Against B:{format_data(account_b)}")
  
  guess=input("Who has more followers? Type 'A' or 'B': ").lower()
  
  a_follower_count=account_a["follower_count"]
  b_follower_count=account_b["follower_count"]
  is_correct = check_answer(guess,a_follower_count,b_follower_count)

  os.system('cls')
  print(logo)
  
  if is_correct:
    score+=1
    print(f"You are correct! Your score is {score}.")
  else:
    print(f"Sorry, You are wrong! Your final score is {score}.")
    should_continue=False
