import math
print("enter the three sides of triangle")
a=float(input())
b=float(input())
c=float(input())
s=(a+b+c)/2.0
area=sqrt(s*(s-a)*(s-b)*(s-c))
print("area of a triangle=",area)

