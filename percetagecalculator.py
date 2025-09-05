student_name=(input("Enter your name: "))
n=int(input("How many subject you want: "))
mark=0
for i in range(n):

   name=input(f"Name of the subject {i+1}: ")
   marks=int(input(f"Enter the mark of {name}: "))

   
   mark+=marks
print("Grand Total: ",mark)
total_num=n*100

print("Total Marks: ",total_num)
per=(mark/total_num)*100
if per>=30:
   print("Passed")
else:
   print("Fail")
print(f"Your percentage is {int(per)}%. Welldone {student_name}")

# print(percentage)

# bengali_marks=int(input("Enter your Bengali marks:"))
# english_marks=int(input("Enter your English marks:"))
# math_marks=int(input("Enter your Math marks:"))
# phys_marks=int(input("Enter your Phys marks:"))
# chem_marks=int(input("Enter your Chem marks:"))
# bios_marks=int(input("Enter your Bios marks:"))
# percentage=((bengali_marks+english_marks+math_marks+phys_marks+chem_marks+bios_marks)/600)*100
# print(f"Percentage of Marks {int(percentage)}%. Well done {student_name}")