# Accept a sentence and display each word seperately with it's length

string = input("Enter a sentence: ")
length = len(string)

brk_str = string.split()

for i in range(0,len(brk_str)):
    print(brk_str[i],len(brk_str[i]))
