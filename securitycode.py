import random
import string
str=input("Enter a string:")
print("Your string is:",str)
if len(str)<3:
    print(str[::-1])
else:
    c=(str[1:len(str)]+str[0])
    
    
    random_string = ''.join(random.choices(string.ascii_letters, k=3))
    
    random_string1 = ''.join(random.choices(string.ascii_letters, k=3))
    

    
                                                                                                   
    print("Security code is:",random_string1[0:]+c[0:len(c)]+random_string[0:len(random_string)])

#decoding code
