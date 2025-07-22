#simple interest
p=float(input("Enter  principle amount: "))
t=float(input("Enter  time(in years): "))
r=float(input("Enter intarest per annum : "))
simppleintarest=p*t*r/100
print(simppleintarest)

#compound interest
p=float(input("Enter  principle amount: "))
t=float(input("Enter  time(in years): "))
r=float(input("Enter intarest per annum : "))
ammount=p * pow((1+r/100),t)
compound_interest=ammount-p
print("compound interest=",compound_interest)
print("total ammount is",ammount)

