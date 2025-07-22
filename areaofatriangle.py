import math
print("enter the three sides of triangle")
a=float(input("enter the 1st side: "))
b=float(input("enter the 2nd side: "))
c=float(input("enter the 3rd side: "))
if a + b > c and a + c > b and b + c > a:
 s=(a+b+c)/2.0
 area=math.sqrt(s*(s-a)*(s-b)*(s-c))
 print("area of a triangle=",area)
else:
 print("given side is do not a perfect triangle")
 

