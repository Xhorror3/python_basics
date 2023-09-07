import random

a=input("Tails or Head. Press 't' for tails and 'h' for heads\n")
x=0
y=0
if a=='t':
    x=1
else:
    y=1
b=random.randint(0,1)
if b==0:
    print("Tails it is.")
    if b!=x:
        print("You won the toss.")
    else:
        print("You lost the toss.")
else:
    print("Heads it is.")
    if b==y:
        print("You won the toss.")
    else:
        print("You lost the toss.")