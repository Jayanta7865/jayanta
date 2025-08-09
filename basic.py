# # Write a program to take user input and print it.
user_input=input("Enter your Name: ")
print(user_input)

# # Print the sum of two numbers.
num1=int(input("Enter the first number: "))
num2=int(input("Enter the second number: "))
c=num1+num2
print("Result of addition",c)

# # Find whether a number is even or odd.
num=int(input("Enter the number: "))
if num<0:
    print("Enter a positive number")
elif num%2==0:
    print("The given number is even")

else:
    print("The number is odd")
    



# # Write a program to swap two numbers.
a=int(input("A="))
b=int(input("B="))
a=a+b
b=a-b
a=a-b
print(f"After the two number \n A={a}\n B={b}")


# # Print the multiplication table of a number.
n=int(input("Enter the number: "))
print(f"Multiplication table of {n} is")
for i in range(1,10+1):
    c=n*i
    print(f"{n} * {i} = {c}")

# # Find the factorial of a number using a loop.
n=int(input("Enter the number: "))
if n==0:
    print("The factorial of 0 is 1")
else:
    fact=1
    for i in range(1,n+1):
        fact=fact*i
    print(f"The factorial of {n} is {fact}")

# # Check if a number is prime or not.
n=int(input("Enter the number: "))
if n<=1:
    print("NOT a prime number")
else:
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            print("The number is not prime")
            break
    else:
        print("Prime number")



     






# # Find the largest of three numbers.
num1=int(input("Enter the 1st number: "))
num2=int(input("Enter the 2nd number: "))
num3=int(input("Enter the 3rd number: "))

if num1>num2 and num1>num3:
    print(f"{num1} is grater number")
elif num2>num1 and num2>num3:
    print(f"{num2} is grater number")
else:
    print(f"{num3} is grater number")

# # # Count the number of vowels in a string.
ch=input("Enter a string: ").lower()
temp=0
vowel_list = []
for i in ch:
   
    if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
        temp+=1
        vowel_list.append(i)  
print("In this name the vowel are:"," ".join(vowel_list))
        
        
print("The number of vowel in the above name is",temp)

#reverse the user input
n=int(input("enter the number: "))
rev=0
while n>0:
    
    j=n%10
    rev=rev*10+j
    n=n//10



print("the reverse number is",rev)



    




