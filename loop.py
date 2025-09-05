#print 1 to 100 using while loops
# i=1
# while i<=100:
#     print(i)
#     i+=1
#print 100 to 1 using while loops
# i=100
# while i>=1:
#     print(i)
#     i-=1
#print multiplication table number n
# n=int(input("Enter a number: "))
# i=1
# while i<=10:
#     print(f"{n} * {i} ={n*i}")
#     i+=1
#print all the `element in the following list`
l=[1,4,9,16,25,36,49,64,81,100]
x=int(input("enter the item you want to search: "))
index=0
while index<len(l):
    if(l[index]==x):
        print(" Item found  at index",index)
        break
    else:
        print("finding...")
    # print(l[index])
    index+=1