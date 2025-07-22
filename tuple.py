tuple=(1,2,3,4,"jayanta")
print(type(tuple))
print(tuple)
print(tuple[0:3])
print(len(tuple))
print(tuple[0])
print(tuple[4])
print(tuple[-3])
if 1 in tuple:
    print("yes")
else:
    print("no")
print(tuple[0:5:4])
# manupulating tuple
fruits=("apple","mango","banana","orange","onion")
print(len(fruits))
change=list(fruits)
print(type(change))
print(type(fruits))
change.append("jackfruit")
change.pop(4)
change[2]="nut"
change.append("watermelon")

fruits=tuple(change)
print(fruits)
print(type(fruits))
print(len(fruits))


name=("joy","joy","ram","joy")
number=(name.count("joy"))
print("The count of joy in tuple is: ",number)

a=(1,2,3,4,3,5,6,34,7,6,3)
print(len(a))
new=a.index(3,5,11)
print("The index of 3 in the list is: ",new)
place=("kolkata","mumbai","bengaluru","goa","delhi")
new=list(place)
new.pop(2)#removes the item in index 3
new.append("chennai")
new1=["westbengal","panskura"]
new.extend(new1)
new[6]="tripura"
place=tuple(new)
print(place)
print(len(place))
print(place[3:7:2])
if "rajasthan" in place:
    print("yes")
else:
    print("no")
   