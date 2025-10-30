# #  Print the sum of numbers from 1 to n using for loop
# n=int(input("enter the number: "))
# sum=0

# for i in range(1,n+1):
#     sum=sum+i
    
    
# print(sum)

    
# # 4. Functions

# # Write a function to calculate factorial
# def factorial(n):
#     fact=1
    
#     for i in range(1,n+1):
            
#             fact=fact*i
#     return fact

        
# num=int(input("Enter a number: "))
# if num < 0:
#     print("Factorial is not defined for negative numbers.")
# else:
#     print(f"The factorial of {num} is {factorial(num)}")

# # Write a function to check if a number is prime
# def prime_or_not(n):
#      if n<=1:
#          return "not prime!"
#      for i in range(2,int(n**0.5)+1):
#           if(n%i==0):
#             return False
#      return True
# num=int(input("Enter a number: "))
# if prime_or_not(num):
#     print("The number is prime")
# else:
#     print("not prime!")
# # 5. Strings

# # Count vowels in a string
# name=input("Enter a string: ").lower()
# temp=0
# for i in name:
#     if i=='a' or i=='e'or i=='i'or i=='o'or i=='u':
#         temp+=1
#         print(i)
# print(f"The number of vowel in ({name}) are:",temp)

# # Reverse a string

# # Check if a string is a palindrome
# st=input("Enter a string you want to check: ")
# a=st[::-1]
# if a==st:
#     print("The given string is palindrome..")
# else:
#     print("The given string is not palindrome..")
    

    
# # 6. Lists

# # Add numbers to a list using input()
# n=int(input("Enter a number: "))
# l=[]
# for i in range(n):
#     l1=int(input(f"Enter number one by one {i+1}:"))
#     l.append(l1)
#     a=sum(l)
# print("Your list is:",l)
# print("Sum of all list number=",a)

# # Find max, min, and average of a list
# n=int(input("Enter a number: "))
# l=[]
# for i in range(n):
#     l1=int(input(f"Enter number one by one {i+1}:"))
#     l.append(l1)
#     a=max(l)
#     b=min(l)
#     averag= sum(l)/n
# print("Your list is: ",l)
# print("The max value of the list is: ",a)
# print("The min value of the list is: ",b)
# print("The average of all the list value is: ",averag)

# # Reverse a list


# l=list(map(int,input("Enter values separet by space: ").split()))
# rev_l=l[::-1]
# print("Your list is:",l)
# print("After reveresd your list: ",rev_l)





# # 7. Pattern Printing

# # Print star and number patterns like triangle, pyramid, diamond

# # 🟡 Intermediate Level
# # 8. List Comprehension

# # Create a list of squares from 1 to 10 using list comprehension
def square(n):
    return n*n
l=[1,2,3,4,5,6,7,8,9,10]
# n=int(input("Enter the number of item you want to placed: "))
# for i in range(n):
#     item=int(input(f"Enter {i+1} item: "))
#     l.append(item)
print("Your list is:",l)
newlist=list(map(square,l))
print("After Square all items: ",newlist)


# 9. Dictionaries

# # Create a dictionary from user input and search a key
# dict={}
# name=input("Enter your name: ")
# dict.update({"name":name})
# roll=int(input("Enter your roll: "))
# dict.update({"roll":roll})
# clas=input("Enter your class: ")
# dict.update({"class":clas})
# print(dict.get("name"))
# print(dict)
# def hello(n):
#       my_dict = {}
      


#       n = int(input("How many items do you want to add? : "))


#       for i in range(n):
#           key = input(f"Enter key {i+1}: ")
#           value = input(f"Enter value for '{key}': ")
#           my_dict[key] = value  

#       search_key = input("Enter the key you want to search: ")


#       if search_key in my_dict:
#           print(f"Value for '{search_key}' is: {my_dict[search_key]}")
#       else:
#           print(f"'{search_key}' not found in the dictionary")



# 10. Sets

# # Find union and intersection of two sets
# a={2,3,4,6}
# b={2,3,7,8,9}
# print(a.union(b))
# print(a.intersection(b))
# 11. Tuples

# # Unpack a tuple and print values
# 12. File Handling

# # Write and read a file
with open("bio.txt","w") as file:
    file.write("Hello,My name is jayanta samanta.I'm a python devoloper.")

f=open("bio.txt","r")
data=f.read()
print(data)
f.close()
# 13. Exception Handling

# # Handle ZeroDivisionError using try-except
# n=float(input("Enter the dividend: "))
# n1=float(input("Enter the divisor: "))
# try:
#      result=n/n1
#      print(result)
# except ZeroDivisionError:
#      print("Any number can't devided by 0")
# 14. Recursion

# # Write a recursive function to calculate Fibonacci

# 🔵 Advanced Practice (Optional)
# 15. Classes and Objects

# # Create a class `Student` with attributes and a method to display info
# 16. Lambda Functions and map(), filter()
# # Use map to square a list of numbers

# # Use filter to get even numbers from a list

# 17. Decorators (Advanced)

# # Create a simple decorator to time a function
# Bonus: 🔢 Practice Questions
# Write a program to check if a number is Armstrong.


# n=int(input("Enter a number you want to check: "))
# l=len(str(n))
# sum=0
# temp=n
# while temp>0:
#      digit=temp%10
#      sum+=digit**l
#      temp=temp//10

# if n==sum:
#     print("The given number is Armstrong number!")
# else:
#     print("The given number is  not Armstrong number!")



# Write a program to generate all prime numbers between 1 to 100.

# Write a program to remove duplicates from a list.
# n=int(input("enter the number : "))
# a=[]
# for i in range(n):
#     a1=int(input(f"Enter the number one by one {i+1}: "))
#     a.append(a1)
# print("your list items are\n",a)
# s=set(a)
# l=list(s)
# print("After deleted duplicate values\n",l)
# Write a program to count word frequency in a string.

# Write a program to merge two dictionary
