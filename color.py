list=[]
n=int(input("enter the colours:"))
for i in range(0,n):
    list.append(str(input()))
print(list)
print("the first colour is",list[0])
print("the last colour is",list[-1])
