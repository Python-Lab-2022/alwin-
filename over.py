n=int(input("enter the number"))
list=[]
for i in range(0,n):
    list.append(int(input()))
x=[]
for i in list:    
    if i>100:
        x.append("over")
    else:
        x.append(i)
        print(x)
sum=0
for i in list:
    sum=sum+i
print(sum)
