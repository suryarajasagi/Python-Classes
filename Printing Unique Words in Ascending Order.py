# Accept a string and print it's unique words in a sorted order.

input_string = input("Enter a sentence: ")
new_str = []

string = input_string.split()
new_str.append(string[0])

for i in range(1, len(string)):
    if string[i] not in new_str:
        new_str.append(string[i])

final_str = sorted(new_str)

for j in range(0, len(final_str)):
    print(final_str[j])
