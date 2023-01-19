list1=[]
list2=[]
n=int(input("enter the elements:"))
for i in range(0,n):
    list1.append(int(input()))
print("first list is:",list1)
num=int(input("enter the elements:"))
for i in range(0,num):
    list2.append(int(input()))
print("second list is:",list2)
len1=len(list1)
len2=len(list2)
if len1==len2:
    print("two list are same length")
else:
    print("two list are not same")
