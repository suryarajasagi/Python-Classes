#Take 10 numbers and get their average

sum = 0

for i in range (0,10):
    num = int(input("Enter the numbers: "))
    sum += num
average = sum/(i+1)
average = str(average)
print("The average is: " + average)