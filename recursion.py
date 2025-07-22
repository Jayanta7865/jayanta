# Factorial

def factorial(num):
    '''I am Jayanta Samanta,  
    i am a Python Developer'''# example of docstring
    if(num==0 or num==1):
        return 1
    else:
        return num * factorial(num-1) #
num=int(input("enter any positive number: "))
print("Number",num)
print("Factorial is",factorial(num))#recursion
print(factorial.__doc__)#process of print docstring

#Fibonacci sequesce

def fibo(num):
    if num<=0 :
        return 0

    elif num==1:
        return 1
    else:
        return fibo(num-1)+fibo(num-2)# function call
num = int(input("Enter the number of terms: "))
print("Fibonacci sequence:")
for i in range(num):
    print(fibo(i),end=" ")

