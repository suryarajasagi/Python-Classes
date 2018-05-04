# Print the string in reverse order..

string = input("Enter a word: ")
length = len(string)

for i in range(0, len(string)):
    print(string[length - 1],end="")
    length -= 1
