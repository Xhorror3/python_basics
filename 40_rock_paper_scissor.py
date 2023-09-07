import random

user=int(input("Welcome to rock,paper,scissor game\nplease enter '0' for rock,'1' for paper, and '2' for scissor:\n"))
computer=random.randint(0,2)
print(f"{user}:{computer}")
if user==computer:
    print("Draw! Please try again!")
elif user==0 and computer==2:
    print("You win!")
elif user==2 and computer==0:
    print("You lose!")
elif user<3:
    if user>computer:
        print("You win!")
    elif computer > user:
        print("You lose!")
else:
    print("Invalid input! Please try once again!")