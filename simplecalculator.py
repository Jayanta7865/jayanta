print("Select an operation.")
print("1.Addition")
print("2.subtruction")
print("3.Multiplication")
print("4.Division")
choice=int(input("Enter your choice(1/2/3/4): "))
if choice==1:
    num1=float(input("Enter the first number:"))
    num2=float(input("Enter the second number:"))
    print("Final Result")
    result=num1+num2
    print(f" {num1} + {num2} = {result}")
    
         
         
       
elif choice==2:
     num1=float(input("Enter the first number:"))
     num2=float(input("Enter the second number:"))
     print("Final Result")
     result=num1-num2
     print(f" {num1} - {num2} = {result}")
elif choice==3:
      num1=float(input("Enter the first number:"))
      num2=float(input("Enter the second number:"))
      print("Final Result")
      result=num1*num2
      print(f" {num1} * {num2} = {result}")
elif choice==4:
      num1=float(input("Enter the first number:"))
      num2=float(input("Enter the second number:"))
      print("Final Result")
      
      if num2 ==0:
           raise ZeroDivisionError("Division by zero not possible")
      result=num1/num2
      print(f" {num1} / {num2} = {result}")
else:
     print("Invalid choice,please select a valid operation.")
     
print("Thank's for using calculator.")     


