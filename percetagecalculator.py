student_name=(input("Enter your name:"))
bengali_marks=int(input("Enter your Bengali marks:"))
english_marks=int(input("Enter your English marks:"))
math_marks=int(input("Enter your Math marks:"))
phys_marks=int(input("Enter your Phys marks:"))
chem_marks=int(input("Enter your Chem marks:"))
bios_marks=int(input("Enter your Bios marks:"))
percentage=((bengali_marks+english_marks+math_marks+phys_marks+chem_marks+bios_marks)/600)*100
print(f"The Result of {student_name} is {int(percentage)}%. Well done {student_name}")