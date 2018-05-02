# Accept a number and print the digits in reverse order

num = int(input("Enter a number: "))

while num != 0:
    rem = num % 10
    print(rem)
    num = num // 10