s={"jayanta",2,3,2,True}
print(s)
print(type(s))
for i in s:
    print(i)
s=set()
print(type(s))


# set methods

#union and update ()

s1={1,2,3,4,5}
s2={5,6,7}
print(s1.union(s2))
s1.update(s2)
print(s1,s2 )

#intersection and intersection_update()

s1={1,2,3,4}
s2={1,3,4,6}
print(s1.intersection(s2))
s1.intersection_update(s2)
print(s1)

# symmentric_difference and symmentric_difference_update()

s1={1,2,3,4}
s2={2,3,6,7}
print(s1.symmetric_difference(s2))
s1.symmetric_difference_update(s2)
print(s1)

# add()

s={1,2,34,4}
s.add("jayanta")
print(s)

#difference and difference_update()
s1={1,2,3,4}
s2={1,2,5,7}
print(s1.difference(s2))
print(s1,s2)
s1.difference_update(s2)
print(s1,s2)

#isjoints()

s1={1,2,3,4}
s2={6,7,5,6}
print(s1.isdisjoint(s2))

#issuperset()

s1={1,2,3,4}
s2={1,2,4}
print(s1.issuperset(s2))

#subset()

s1={1,2,3,4}
s2={1,2,4,}
print(s2.issubset(s1))

# remove() and discard()#same use
s1={1,2,3,4,5}
s1.remove(5)
print(s1)

#pop()
s1={1,2,3,4,5}
s2=s1.pop()
print(s1)
print("the popped item is:",s2)

#del keyword
# s1={1,1,2,3,4,5}
# del s1
# print(s1)

#clear()

s1={1,2,3,4,5,6}
s1.clear()
print(s1)

#check if item is exists
s1={1,2,3,4,5,6}
if 1 in s1:
    print("1 is present in set")
else:
    print("1 is not presnt")

#copy()
s1={1,2,2,2,3,4,5}
print(len(s1))
s2=s1.copy()
print(s1)
print(s2)
