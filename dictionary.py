# #create a dist
# std_details={
#     "name":"Jayanta",
#     "Paper code":["cc13","cc14","DSE3","DSE4"],#print list
#     "Marks":(56,76,43,45),#print tuple
#     "Name":{"Jayanta","RAjju","Raja"},#print set
#     "ROll":72,
#     "Subject":"BCA",
#     "College Name":"Panskura Banamali College",
#     "Semester":6
# }
# std_details["name"]="Jayanta Kumar"#change name using his key
# std_details["surname"]="Samanta"#add new key value pair

# # print(std_details)#print dictionary
# # print(std_details['Name'])
# # print(std_details['Marks'])
# # print(std_details['Paper code'])
# # print(std_details["name"])
# # print(std_details["surname"])
# # for i in std_details: #only print keys
# #     print(i)
# empty_dist={}#creat a empty dist
# empty_dist['id']=76483463 #assign key value in empty dist

# print(empty_dist)

#nested Dist
# student={
#     "name":"Jayanta kumar Samanta",
#     "Subject":     #nested dist
#     {
#         "Beng":67,
#         "Eng":76,
#         "Math":56
#     }
# }
# print(student)
# print(student["Subject"])
# print(student["Subject"]["Beng"])
# print(student.keys())#print all keys
# print(list(student.keys()))#typecasting
# print(len(list(student.keys())))#lenght of dict
# print(student.values())#print all values
# print(list(student.values()))
# print(student.items())#return all key,value as tuple
# pairs=list(student.items())
# print(pairs[0])
# print(student.get("name"))#returns the key according value
# student.update({"Roll":72,"SEM":6})#insert the specified items to the dict
# print(student)
# new_dist={
#     "class":"BCA",
#     "Collage":"pbc",
# }
# student.update(new_dist)
# print(student)

student_marks={}
marks=int(input("Enter the marks for phy: "))
student_marks.update({"Phy":marks})
marks=int(input("Enter the marks for math: "))
student_marks.update({"math":marks})
marks=int(input("Enter the marks for eng: "))
student_marks.update({"eng":marks})
print(student_marks)