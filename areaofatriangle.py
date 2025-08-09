import math
print("enter the three sides of triangle")
a=float(input("enter the 1st side: "))
if a<0:
 raise ValueError("you can't prefer nagative value")
b=float(input("enter the 2nd side: "))
if b<0:
 raise ValueError("you can't prefer nagative value")
c=float(input("enter the 3rd side: "))
if c<0:
 raise ValueError("you can't prefer nagative value")

  
if a + b > c and a + c > b and b + c > a:
 s=(a+b+c)/2.0
 area=math.sqrt(s*(s-a)*(s-b)*(s-c))
 print("area of a triangle=",area)
else:
 print("given side is do not a perfect triangle")
 

