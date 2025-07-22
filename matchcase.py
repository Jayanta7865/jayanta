#check the string vowel or consonent
str=input("Enter single alphabet: ").upper()

    
match str:
    case "A"|"E"|"I"|"O"|"U":
        print(f"{str} is vowel.")
    case _ if str.isalpha and len(str)==1:
        print(f"{str} is consonent.")
    case _:
        print("enter a single and valid alphabet.")
    

    #check the number odd or even
n=int(input("Enter the number: "))
match n:
    case _ if(n%2==0):
        print(f"{n} is even number")
    case _:
        print(f"{n} is odd number")

#palindrome or not
str=input("Enter a string: ").lower()
reversed_str=str[::-1]
match str==reversed_str:
    case True:
        print("The string is palindrome")
    case False:
         print("The string is not  palindrome")

       




   



