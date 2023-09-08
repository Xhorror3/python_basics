import random

# easy method

# letters=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
# numbers=('1','2','3','4','5','6','7','8','9','0')
# symbols=('!','@','#','$','%','^','&','*','_','+','=')
# print("Wellcome to the password generator machine:")
# l=int(input("Enter number of letters required in password:"))
# n=int(input("Enter number of numbers required in password:"))
# s=int(input("Enter number of symbols required in password:"))
# password=""
# for i in range(1,l+1):
#     char=random.choice(letters)
#     password=password+char
# for a in range(1,n+1):
#     char=random.choice(numbers)
#     password=password+char
# for b in range(1,s+1):
#     char=random.choice(symbols)
#     password=password+char
# print(password)


letters=('a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
numbers=('1','2','3','4','5','6','7','8','9','0')
symbols=('!','@','#','$','%','^','&','*','_','+','=')
print("Wellcome to the password generator machine:")
l=int(input("Enter number of letters required in password:"))
n=int(input("Enter number of numbers required in password:"))
s=int(input("Enter number of symbols required in password:"))
password=[]
for i in range(1,l+1):
    char=random.choice(letters)
    password.append(char)
for a in range(1,n+1):
    num=random.choice(numbers)
    password.append(num)
for b in range(1,s+1):
    sym=random.choice(symbols)
    password.append(sym)

random.shuffle(password)

password11=""
for m in password:
    password11 += m
print(password11)

