list1=[]
list2=[]
a=[]
n=int(input("enter the limit for list1:"))
for i in range(0,n):
    list1.append(input("enter the colours:"))
n2=int(input("enter the limit for list2:"))
for i in range(0,n2):
    list2.append(input("enter the colours:"))
for i in list1:
    if i not in list2:
        a.append(i)
print(a)
