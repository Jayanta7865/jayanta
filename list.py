#example of list
list=[1,3,2,6,10,4]
print(list)
print(list[4])
if 7 in list:
    print("yes")
else:
    print("no")

list=[i for i in range(11)]
print(list)
print(list[-3:-1])

#All the list method

#append() method
list=[5,6,7,8]
print(list)
list.append(9)
print(f"Update list is {list}")
#sort() method 
#ascending order
list=[9,5,8,3,7]
print(list)
list.sort()
print(f"After using sort method {list}") 
#descinding order
list=[9,5,8,3,7]
print(list)
list.sort(reverse=True)
print(f"After using sort method {list}")
#reverse() method
list=[9,5,8,3,7]
print(list)
list.reverse()
print(f"After using reverse method {list}")
#index()method
list=[9,5,8,3,7]
print(list)
print(f"The index of 7 is {list.index(7)}")
#count()method

list=[9,5,8,3,7,5,5,5]
print(list)
print(f"The number of 5 in list are {list.count(5)}")
#copy()method

list=[4,6,7,"jayanta"]
print(list)
list1=list.copy()
print(list1)
#insert()method

list=[4,5,6,3]
print(list)
list.insert(1,10)#1=index number,10=update value
print(f"New list {list}")
list[1]=13 # update the value of index 1 in list
print(list)
#extend()method
list=[3,4,6,7]
print(list)
new_list=[8,9,10,11]
list.extend(new_list)#extend
print(list)
#concatenate two string

New=(list+new_list)#concatenate
print(New)


