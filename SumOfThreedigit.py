#Take a three-digit number and calculate the sum of its digit
num1 = int(input("Enter your three digit number: "))
sum =0
while num1>0:
    reminder = num1%10
    sum += reminder
    num1 = num1//10
print("Sum is: ", sum)