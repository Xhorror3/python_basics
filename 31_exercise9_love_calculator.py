name1=input("Enter your name:\n")
name2=input("Enter your crush name:\n")
nam1=name1.lower()
nam2=name2.lower()
totalstr=nam1+nam2
t=totalstr.count('t')
r=totalstr.count('r')
u=totalstr.count('u')
e=totalstr.count('e')
l=totalstr.count('l')
o=totalstr.count('o')
v=totalstr.count('v')
e1=totalstr.count('e')

str1=str(t+r+u+e)
str2=str(l+o+v+e1)

string1=str1+str2

string2=int(string1)

print("Your love percentage is:",string1,"%")

if(string2<10):
    print("You should work hard on your love\n")
elif(string2>=10 and string2<=50):
    print("You can make a nice pair together\n")
elif(string2>50 and string2<=90):
    print("You are best with your love\n")
else:
    print("Your are perfect match")