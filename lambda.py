
fact=(lambda n: 1 if n==0 else n*fact(n-1))
num=int(input("Enter a number: "))
print(f"The Factorial of {num} is {fact(num)}")


odd_even=(lambda n: "even" if n%2==0 else "odd")
num1=int(input("Enter a number: "))
print(f"The given number is {odd_even(num1)}")



a="Leap Year Calculater"
print(a.center(120))
leapyear=(lambda n:"leap year" if n%4==0 and n%100!=0 or n%400==0 else " not leap year")
while True:     
     year=int(input("Enter a year: "))
     print(f"The year {year} is {leapyear(year)}")
     choice=input("If you check another year write (yes) either (no): ").lower()
     if choice!="yes":
         print("Program Ended.Thank you....")
         break

    