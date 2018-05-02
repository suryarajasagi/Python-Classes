# Check whether the number is prime or not

num = int(input('Enter the number: '))
count = 0
for i in range(2, num // 2 + 1):
    if num % i == 0:
        count = 1
if count == 1:
    print('The number is Composite..')
else:
    print('The number is Prime..')