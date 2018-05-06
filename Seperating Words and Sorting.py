# Accept a sentence and display each word sorted and seperated with it's length

string = input("Enter a sentence: ")
length = len(string)

brk_str = string.split()

for i in range(0, len(brk_str)):
    sort_str = sorted(brk_str[i])
    for j in range(0, len(sort_str)):
        print(sort_str[j], sep="", end="")
    print("\t", len(brk_str[i]))
