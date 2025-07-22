# arr=[5,8,19,4]

# if arr[0]>arr[1] and arr[0]>arr[2] and arr[0]>arr[3]:
#     print(f"{arr[0]} is grater")
# if arr[1]>arr[0] and arr[1]>arr[2] and arr[1]>arr[3]:
#     print(f"{arr[1]} is grater")
# if arr[2]>arr[0] and arr[2]>arr[1] and arr[2]>arr[3]:
#     print(f"{arr[2]} is grater")
# else:
#     print(f"{arr[3]} is grater")
# if arr[0]<arr[1] and arr[0]<arr[2] and arr[0]<arr[3]:
#     print(f"{arr[0]} is lower")
# if arr[1]<arr[0] and arr[1]<arr[2] and arr[1]<arr[3]:
#     print(f"{arr[1]} is lower")
# if arr[2]<arr[0] and arr[2]<arr[1] and arr[2]<arr[3]:
#     print(f"{arr[2]} is lower")
# if arr[3]<arr[0] and arr[3]<arr[1] and arr[3]<arr[2]:


#     print(f"{arr[3]} is lower")

list = list(map(int, input("Enter numbers separated by space: ").split()))

print(f"{max(list)} is greater")
print(f"{min(list)} is lower")

# list=[7,5,43,67,2,6]
# print(f"{max(list)} is grater")
# print(f"{min(list)} is lower")
# tup=(1,3,5,6)
# # list1=list(tuple)
# print(type(tup))
# # print(type(list1))
# new=list(tup)
# new.append(7)
# tup=tuple(new)
# print(tup)








