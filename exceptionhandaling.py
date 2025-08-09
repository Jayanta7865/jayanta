#exception is a runtime error, it occur when you write wrong logic.
#in python the exception handale by try,except,else,finally mechanism



try:
 a=int(input("Enter a number: "))
 
 print(f"The multiplication table of {a} is\n")
except :
 print("enter integer")
try:
 for i in range(1,11):
    print(f"{int(a)}*{i}={int(a)*i}")
except:
  print("invalid input")
print("hello have a good day")



try:
    a=int(input("entre a number:"))
    a1=[1,2,3]
    print(a1[a]) 
   
except ValueError:
    print("enter a correct value")
except IndexError:
    print("the index error")



n=int(input("enter a number:"))
if n<0:
        raise ValueError("value should be posative")#raising the error custom
for i in range(1,n+1):
      print(" " * (n-i) + "*" *(2*i-1))
for i in range(n-1,0,-1):     
      print(" " * (n-i) + "*" *(2*i-1))

#handaling error     
try:
   n=int(input("enter a number:"))
   if n<0:
        raise ValueError("value should be posative")
   for i in range(1,n+1):
      print(" " * (n-i) + "*" *(2*i-1))
   for i in range(n-1,0,-1):     
      print(" " * (n-i) + "*" *(2*i-1))
except ValueError:
    print("please enter positive value")
finally:
    print("i am always printable")

try:
    num1=int(input("Enter a number:"))
    num2=int(input("Enter a number:"))
    result=num1/num2
    
except ZeroDivisionError:
    print("Error: any number can't devide by zero!")
except ValueError:
    print("Error: please enter valid integer!")
else:
    print("Result:",result)
finally:
    print("Execution complete...")
