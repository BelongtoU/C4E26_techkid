from random import randrange

word = "Handsome"
character_lst = list(word)
check_list = [len(word)+1]

while len(check_list) <= len(character_lst):
    i = randrange(0, len(character_lst))
    if i not in check_list:
        print(character_lst[i], end = " ")
        check_list.append(i)
print()
for i in range(3):
    answer = input("\nEnter your answer: ")
    if answer == word:
        print()
        print("Congratulate !!!!")
        break
    else:
        print("Wrong !!! again, you have 3 turns :))")
        print("And now, you just lost 1 turn :))")

if answer != word:
    print()
    print("Out of your turn, Loser :))")
