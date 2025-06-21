a=list()
n=int(input("enter how many array element you want:"))
print("enter array element one by one")
for i in range(0,n):
    x=int(input())
    a.append(x)
print("the array elements are:",a)
print("enter search ellement:")
item=int(input())
F=0
for i in range(0,n):
    if(a[i]==item):
        loc=i
        F=1
    if(F==1):
        print("the element is found and location",loc+1)
    else:
        print("item is not found")
