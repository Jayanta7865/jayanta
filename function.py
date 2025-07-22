def isgrater(a,b):
    if a>b:
        print(f"{a} is graterthan {b}")
    else:
         print(f"{b} is graterthan {a}")
def gmean(a,b):
    mean= (a*b)/(a+b)
    print(mean)
a=15
b=54
isgrater(a,b)
gmean(a,b)
        
# # #function arguments

def average(a=10,b=10,c=5):
  #example of defult argument
  def average(a=10,b=12):
     print("Average is the",(a+b)/2)
    
average(b=2)
def average(a,b=12):
    print("Average is the",(a+b)/2)
average(12)
def average(a,b,c=12):
    print("the average is ",(a+b+c)/3)
average(3,3)

def average(*number):
    sum=0
    for i in number:
        sum=sum+i

    return sum/len(number)
    print("the average is the", sum/len(number))
c=average(5,6,4,7,10)
print(c)

count=1
def jayanta():
    global count
    for i in range(1,5,10):
        count +=10
jayanta()
print(count)