string=str(input("enter the string"))
print("the string is:",string)
start=string[0]
end=string[-1]
result=end+string[1:-1] + start
print("The result is",result)
