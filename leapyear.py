year=int(input("enter any year:"))
if(year%4==0) and (year%100!=0 or year%400==0):
    print(year,"is leapyear",)
else:
    print(year,"is not leapyear")

#using lambda function
leap=(lambda n: "leap year" if n%4==0 and n%100!=0 or n%400==0 else "not leap year")
# print(leap(2010))
year=int(input("Enter year you want to check: "))
print(leap(year))