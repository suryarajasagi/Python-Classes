# Accept 10 numbers and print the largest of them. Include Negative Numbers also.

largest = num = int(input("Enter a number: "))

for i in range(0,4):
    num = int(input("Enter a number: "))
    if num > largest:
        largest = num

print("The largest number is: ",largest)
