name="jayanta"
def even_odd(n):
    print(name)

    # n=int(input("Enter a number you want to check: "))
    try:    
        if n%2==0:
            return "The given number is even"
        elif n<0:
            return "Please enter possitive number"
        else:
            return "The give number is odd"
    except:
        print("Invalid input!!")
num=int(input("Enter a number you want to check: "))
print(even_odd(num))
print("Hello",name)
a=input("Enter your name:")
def hello():
    global a #global variable
    a="fried"
    print("Hello,",a)
hello()
# Write a function reverse_string(s) that returns the reverse of a string.
# Example: "Python" → "nohtyP"
def string_rev(string):
    return string[::-1]
    
str1=input("Enter your name: ")
print(f" reversed string is {string_rev(str1)}")

def string_rev(string):
    print("Your string is:",string)
    rev= string[::-1]
    if rev==string:
        return "The string is palindrome!"
    else:
        return "The string is not palindrome"
    
str1=input("Enter your name: ")

print(string_rev(str1))

# sum of n natural number
def sum_of_n(n):
    sum=0
    while n>=1:
        sum+=n
        n-=1
    print(sum)
    return sum
if __name__=="__main__":
 sum_of_n(8)
# using for loop
def sum_of_n(num):
 sum=0
 print("----Sum of n natural number----")
 for i in range(num+1):
    sum+=i
    if i < num:            
            print(i, end="+")
    else:
            print(i, end=" = ")
 print(sum)
 return sum
num=int(input("Enter a number:"))
sum_of_n(num)

print(sum_of_n(num))

#using recursion

def sum_num(num):
   
     if num==0:
          return 0
     else: 
          return num + sum_num(num-1)
print("Sum using recursion..")
print(sum_num(5))

def fact_n(n):
     if n==0 or n==1:
          return 1
     else:
          return n*fact_n(n-1)
num=int(input("Enter a number for factorial: "))
print(f"Factorial of {num} is {fact_n(num)}")
if __name__=="__main__":
    fact_n()
    
 