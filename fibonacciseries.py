n=int(input("enter how many number you want:"))
print("fibonacci series")
a=0
b=1
for i in range (n):
    print(a , end = ",")
    c=a+b
    a=b
    b=c




#using function


def fibo(n):
    if n<=1:
        return n
    
    
    else:
        return fibo(n-1)+ fibo(n-2)
n=int(input("Enter the number: "))
print("fibonacci sequence")
for i in range(n):
    print(fibo(i),end=",")




    
