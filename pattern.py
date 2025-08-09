# n=int(input("enter a number:"))
# for i in range(1,n+1):
#         print(" * " *i)
    

# n=int(input("enter a number:"))
# for i in range(n,0,-1):
#     print(" * " *i)


# n=int(input("enter a number:"))
# for i in range(1,n+1):
#       print(" " * (n-i) + " * " * i)

# n=int(input("enter a number:"))
# for i in range(1,n+1):
#       print(" " * (n-i) + "*" *(2*i-1))

# n=int(input("enter a number:"))
# if n<0:
#         raise ValueError("value should be posative")#raising the error custom
# for i in range(1,n+1):
#       print(" " * (n-i) + "*" *(2*i-1))
# for i in range(n-1,0,-1):     
#       print(" " * (n-i) + "*" *(2*i-1))


#  #handaling error     
# try:
#    n=int(input("enter a number:"))
#    if n<0:
#         raise ValueError("value should be posative")
#    for i in range(1,n+1):
#       print(" " * (n-i) + "*" *(2*i-1))
#    for i in range(n-1,0,-1):     
#       print(" " * (n-i) + "*" *(2*i-1))
# except ValueError:
#     print("please enter positive value")               
# finally:
#     print("i am always printable") 
# n=(int(input("Enter teh number:")))
# a=1
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(a,end="")
#         a+=1
#     print("\n")

# n=int(input("enter a number:"))
# for i in range(1,n):
#       print(" " *(n-i-1) + "*" * (2*i-1))
# for i in range(n):
#     print(" "*(n-i-1) + "*"*(2*i+1))
      
# n=int(input("enter a number:"))
# for i in range(n,0,-1):
#       print(" " *(n-i) + "*"* (2*i-1))
      

# n=int(input("enter a number:"))
# for i in range(n):
#       print(" " *(n-i-1) + "*" * (2*i+1))
# for i in range(n-2,-1,-1):
#     print(" "  * (n-i-1) + "*" * (2*i+1))

# n=int(input("Enter a number: "))
# n1=1
# for i in range(1,n+1):
#       for j in range(1,i+1):
#             print(j,end=" ")
#       print("\n")

# n=int(input("Enter a number: "))

# for i in range(n,0,-1):
#       for j in range(1,i+1):
#             print(j,end=" ")
#       print("\n")

# n=int(input("Enter a number: "))
# n1=1
# for i in range(1,n+1):
#       for j in range(1,i+1):
#             print(n1,end=" ")
#             n1+=1
#       print("\n")

# n=int(input("Enter a number: "))

# for i in range(n,0,-1):
#       for j in range(1,i+1):
#             print(chr(65 + j), end=" ")
            
#       print("\n")

# n=int(input("Enter a number: "))

# for i in range(n):
#       for j in range(i+1):
#             print(chr(65 + j), end=" ")
            
#       print("\n")

# *
# ***
# *****
# *******
# *****
# ***
# *
# n=int(input("Enter a number: "))
# for i in range(0,n+1):
#     print("*" *(2*i-1))
# for i in range(n-1,-1,-1):
#     print("*" *(2*i-1))
 
        
# *******
# *     *
# *     *
# *     *
# *     *
# *     *
# *******

rows=int(input("Enter a number:"))
colms=int(input("Enter a number:"))
for i in range(rows):
    if i==0 or i==rows-1:
        print('*' * colms)
    else:
        print('*' + ' '* (colms-2) + '*')


# a  
# ab
# abc
n=int(input("enter the num"))
for i in range(n):
    for j in range(i):
        print(chr(97+j),end=" ")
        
    print("\n")



