# Check whether the given number is a Strong Number..

sum = 0
org = num = int(input("Enter a number: "))

while num>0:
    fact = 1
    last_digit = num%10
    num = num//10
    for i in range (last_digit,1,-1):
        fact *= i
    sum += fact
if sum == org:
    print(org, " is a Strong number..")
else:
    print(org, " is not a Strong number..")