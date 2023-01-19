list1=[]
n=int(input("enter the number of elements"))
for i in range(0,n):
    list1.append(int(input()))
print(list1)
for i in range(len(list1)):
    print(list1[i])
    if(list1[i]%2==0):
        list1.remove(list1[i])

print(list1)
