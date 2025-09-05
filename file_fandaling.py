#reading a file

# f=open("myfile.txt","r")
# # data=f.read()
# # print(data)     # read a file whole file  
# line1=f.readline()  # read a file line by line
# print(line1)
# f.close()

#writing a file

# f=open("myfile2.txt","w")
# f.write("Hello,My name is jayanta samanta.I'm a python devoloper.")
# f.close()

#writing append a file

# f=open("myfile2.txt","a")
# f.write("\nI have done my graduation in BCA from panskura banamali college.")
# f.close()

#read and write a file

# f=open("myfile2.txt","r+")
# f.write("we are")
# print(f.read())
# f.close()
# f=open("myfile2.txt","r+")
# f.write("i am")
# print(f.read())
# f.close()
#reading a file using with syntax
# with open("myfile.txt","r") as f:
#     print(f.read())

#deleting a file

# import os
# os.remove("myfile2.txt")

