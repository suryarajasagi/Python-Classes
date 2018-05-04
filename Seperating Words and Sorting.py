# Accept a sentence and display each word sorted and seperated with it's length

string = input("Enter a sentence: ")
length = len(string)

brk_str = string.split()

for i in range(0,len(brk_str)):
    print(sorted(brk_str[i]),len(brk_str[i]))