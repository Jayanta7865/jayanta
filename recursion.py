# # Factorial

# def factorial(num):
#     '''I am Jayanta Samanta,  
#     i am a Python Developer'''# example of docstring
#     if(num==0 or num==1):
#         return 1
#     else:
#         return num * factorial(num-1) #recursion
# num=int(input("enter any positive number: "))
# print("Number",num)
# print("Factorial is",factorial(num))
# print(factorial.__doc__)#process of print docstring

# #Fibonacci sequesce

# def fibo(num):
#     if num<=0 :
#         return 0

#     elif num==1:
#         return 1
#     else:
#         return fibo(num-1)+fibo(num-2)# function call
# num = int(input("Enter the number of terms: "))
# print("Fibonacci sequence:")
# for i in range(num):
#     print(fibo(i),end=" ")

def sum_num(n):
    if n==0:
        return 0
    return sum_num(n-1)+n
num=int(input("Enter a number: "))
print(f" the sum of n number is:{sum_num(num)}")