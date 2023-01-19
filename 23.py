from math import sqrt
a=int(input("Enter the starting index:"))
b=int(input("Enter the ending index:"))
for i in range(a,b):
    n=int(sqrt(i))
    if(n*n==i):
        n=i
        while(n!=0):
            r=n%10
            n=n//10
            if(r%2!=0):
                break
        else:
            print(i)
            

