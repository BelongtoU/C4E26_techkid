data_ip = input("Enter a string of letter and this program will count the number of times each letter occurs\nNow, Please enter your string: ")

memo_dict = {}
for letter in data_ip:
    memo_dict[letter] = memo_dict.get(letter, 0) + 1

list_print = list(memo_dict.items())
list_print.sort()
print()
print(10*"--<3--")
print()
for i in range(len(list_print)):
    print("      %s occurs %s times"%(list_print[i][0], list_print[i][1]))
print()
print(10*"--<3--")
print()