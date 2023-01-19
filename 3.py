string="Woodchuck How much wood would a woodchuck chuck if a woodchuck could chuck Wood ?"
string=string.lower()
string=string.split(" ")
frequency={}
for i in string:
        if i in frequency:
            frequency[i]+=1
        else:
            frequency[i]=1
print(frequency)
