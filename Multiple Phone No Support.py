# Accept users' names and phone numbers until an end appears. Support multiple phone numbers.
# Then, display their names and phone numbers in ascending order.

end = False
details = {}

while end == False:
    name = input("Enter the name: ")
    if name == 'end':
        end = True
        break
    number = input('Enter the number: ')

    if name in details:
        details[name].add(number)
    else:
        details[name] = {number}

details = sorted(details.items())

for a, b in details:
    print(a)
    for i in b:
        print(i, end=" ")
    print()
