import math
print("enter the three sides of triangle")
a=float(input("enter the 1st side"))
b=float(input("enter the 2nd side"))
c=float(input("enter the 3rd side"))
s=(a+b+c)/2.0
area=sqrt(s*(s-a)*(s-b)*(s-c))
print("area of a triangle=",area)

