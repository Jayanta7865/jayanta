a="...WellCome to check prime or not calculator..."
print(a.center(100))
n=int(input("\n Enter a number you want to check: "))
if n<=1:
    print("not prime!!")
else:
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            print(f"{n} is not prime")
            break
    else:
       print(f"{n}is prime")




