for i in[2,3,4,5,6,8]:
    if(i%2!=0):
        continue
    print(i)
list=["jayanta","samanta",21,4+3j,True]
print(list)
print(list[0])
print(list[1])
print(list[2])
print(list[3])
print(type(list[4]))
# Take input from user
ch = input("Enter a single alphabet: ").lower()
match ch:
    case 'a'|'e'|'i'|'o'|'u':
        print("the alphabet is vowel")
    case _:
        print("the word is consonent")
    
    #check the number is odd and even using match case|

n=int(input("enter a number: "))
if n>0:
    match n:
        case _ if n/2==0:
            print("the number is even")
        case _:
            print("the number is odd")
else:
    print("You enter a nagative number, please enter a positive number")
