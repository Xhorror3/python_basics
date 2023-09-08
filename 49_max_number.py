numbers=input("Enter everybodies heights seperated by space:\n")
number_list=numbers.split(" ")
count=0
for c in number_list:
    count=count+1
for i in range(count):
    number_list[i]=int(number_list[i])
print(number_list)
max=0
for a in range(1,count):
    if number_list[a-1]>number_list[a]:
        max=number_list[a-1]
    else:
        max=number_list[a]
print(max)
