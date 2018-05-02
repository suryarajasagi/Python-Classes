#Accept 10 numbers and display the largest one

largest = 0

for i in range(0,10):
    num = int(input("Enter a number: "))
    if num > largest:
        largest = num
largest = str(largest)
print("The largest number is: " + largest)
