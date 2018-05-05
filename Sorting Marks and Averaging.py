# Accept marks from students until there's a '-1'. Print them in ascending order.
# Get the count of no. of students whose marks are above the average.

marks = []
sorted_marks = []
i = 0
cond = True
sum = 0

while cond:
    number = int(input("Enter the marks: "))
    if number == -1:
        break
    sum += number
    marks.insert(i, number)
    i += 1

sorted_marks = sorted(marks)
print(sorted_marks)

average = sum / i
print(average)
count = 0

for j in marks:
    if j > average:
        count += 1
print(count)
