dict={}
string1=input("Enter a string")
for n in string1:
    if n in dict:
        dict[n]+=1
    else:
        dict[n]=1
print("Character frequency")
for k,v in dict.items():
    print(k,v)
