#Write your code below this line 👇

def prime_checker(number):
    count=2
    for x in range(2,number):
        if number%x==0:
            print("It's not a prime number.")
            break
        else:
            count+=1
            continue
    if count==number:
        print("It's a prime number.")
        


#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
