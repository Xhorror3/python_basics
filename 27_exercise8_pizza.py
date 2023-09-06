pizza = int(input("What type of pizza would you like to order:\n 1. Small pizza=100Rs.\n 2. Medium pizza=200Rs.\n 3. Large pizza=300Rs.\nEnter the respective number:"))
pepperoni = (input("Would you like pepperoni to be added?(y/n)"))
cheese = input("Do you want extra cheese?(y/n)")

bill=0
if pizza == 1:
    bill=100
    if pepperoni =='y':
        bill+=30
elif pizza ==2:
    bill=200
    if pepperoni =='y':
        bill+=50
elif pizza ==3:
    bill=300
    if pepperoni =='y':
        bill+=50
else:
    print("Wrong Input!")
if cheese =='y':
    bill+=20
print(f"Your total amount is {bill}")

