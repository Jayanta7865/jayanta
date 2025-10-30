n=int(input("enter the number:"))
if(n<0):
    print("factorial is not possible")
elif(n==0):
    print("foctorial is the given number = 1")
else:
    f=1
    for i in range(1,n+1):
        f=f * i
    print("factorial of given number= ",f)

#using lambda function

fact=(lambda n: 1 if n==0 or n==1 else n*fact(n-1))
print(f"fact of {1} is{fact(1)}")
