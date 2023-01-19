list=[]
sum=0
n=int(input("Enter the number of elements in list:"))
for i in range(0,n):
    list.append(int(input()))
for i in list:
    sum=sum+i
print("Sum of elements in list:",sum)
