import datetime
today= datetime.date.today()
startyear=today.year
finalyear=int(input("the final year"))
print(today)
for year in range(startyear,finalyear):
    if(year%400==0)and(year%100==0):
        print("{0} is a leap year".format(year))
    elif(year%4==0)and(year%100!=0):
         print("{0} is a leap year".format(year))


 
