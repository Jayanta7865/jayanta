#swaping value without using third veriable

a=int(input("A = ")) 
b=int(input("B = ")) 
a=a+b 
b=a-b 
a=a-b 
print("After swapping A =",a,"B =",b)

#swaping value  using bitwise xor
a=int(input("A = "))
b=int(input("B = "))
a=a^b
b=a^b
a=a^b
print("After swapping A =",a,"B =",b)

#swapping don't using 3rd veriale

a=int(input("A = "))
b=int(input("B = "))
a=a-b
b=a+b
a=b-a
print("After swapping A =",a,"B =",b)

#swapping  using 3rd veriale

a=int(input("A = "))
b=int(input("B = "))
c=a
a=b
b=c
print("After swapping: A =",a,"B =",b)
