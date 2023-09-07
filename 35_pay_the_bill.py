import random

names=input("Enter the names of everybody.\n")
splitted_list=names.split(" ")
n= len(splitted_list)
a=random.randint(0,n-1)
print(splitted_list[a],"will pay the bill")