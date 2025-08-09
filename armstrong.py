# Check if a number is Armstrong or not
num = int(input("Enter a number: "))
sum = 0
temp = num
n = len(str(num))  # Count the digits

while temp > 0:
    digit = temp % 10       # Get last digit
    sum += digit ** n       # Raise it to power of n and add to sum
    temp=temp // 10             # Remove last digit

if num == sum:
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")

