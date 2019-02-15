answers  = {
    "1": 35,
    "2": 36,
    "3": 40,
    "4": 44,
}

right_ans = 44
question = "4(x + 3)"
print("Answer the following algebra question:")
print("If x = 8, then what is the value of %s ?"%question)

for i in answers:
    print(i, answers[i], sep = ". ")

ip_ans = input("Your choice: ")
if answers[ip_ans] == right_ans:
    print("Bingo")
else:
    print(":(")