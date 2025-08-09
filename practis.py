# # sum of first n number using while loop
# n=int(input("Enter the value of n: "))
# sum=0
# i=1
# while i<=n:
#     sum+=i
#     i+=1
    
# print("sum of first ",n,"number is:",sum)
   
# # factorial of first n number using for loop
# num=int(input("Enter a number: "))
# fact=1

# if num==1 or num==0:
#     print(f"Factorial of {num} is 1")
# else:
#     for i in range(1,num+1):
        
#         fact=fact*i
#     print(f"Factorial of {num} is {fact}")

# movie1=input(f"Enter the name of first favarite movie: \n").upper()
# movie2=input(f"Enter the name of second favarite movie: \n").upper()
# movie3=input(f"Enter the name of third favarite movie: \n").upper()
# movies=[movie1,movie2,movie3]
# print(movies)
# for movie in movies:
#     print(movie)
# print(type(movies))
        
        
# a=('''i'm jayanta kumar samanta, i have completed my BCA dgreefrom pku in 2025 " \
# "and i carently pursuing my master degree in MCA from HIT holdia." \
# "i am in learning python language and i am very much interested in coding.''')

# print(a.count('a'))
# print(a)

n=int(input("enter a number: "))
movies=[]
for i in range(n):
    movie=input(f"Enter the movie name one by one {i+1}: ") .capitalize()
    movies.append(movie)
print("Your movies list are:",movies)


    




   