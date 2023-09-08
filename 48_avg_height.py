height=input("Enter everybodies heights seperated by space:\n")
height_list=height.split(" ")
count=0
for c in height_list:
    count=count+1
for i in range(count):
    height_list[i]=int(height_list[i])
print(height_list)
sum=0
for s in range(count):
    sum=sum+height_list[s]
print(sum)
avg=sum/count
print(round(avg))
