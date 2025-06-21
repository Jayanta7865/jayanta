year=int(input("enter any year:"))
if(year%4==0) and (year%100!=0 or year%400==0):
    print(year,"is leapyear",)
else:
    print(year,"is not leapyear")