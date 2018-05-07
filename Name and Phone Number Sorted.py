# Accept users' names and phone numbers until an end appears.
# Then, display their names and phone numbers in ascending order.

end = False
name = []
number = []

while end == False:
    new_name = input("Enter the person's name: ")
    if new_name == 'end':
        end = True
        break
    new_number = input("Enter the person's phone number: ")
    name.append(new_name)
    number.append(new_number)
details = list(zip(name, number))
details = sorted(details)

for i in range(0,len(details)):
    print(details[i][0],details[i][1])
