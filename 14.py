list1=[]
list2=[]
a=[]
n=int(input("Enter the number of elemnts in list 1:"))
for i in range(0,n):
    list1.append(str(input()))
n2=int(input("Enter the number of elemnts in list 2:"))
for i in range(0,n2):
    list2.append(str(input()))
for i in list1:
    if i not in list2:
        a.append(i)
print(a)

    
        
            
            
