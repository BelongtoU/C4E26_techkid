questions = [
    "If x = 8, then what is the value of 4(x + 3) ?",
    "Estimate this answer (exact caculation not need):\nJack scored these marks in 5 math tests: 49, 81, 72, 66 and 52. What is the mean ?",
    "Tiến Anh đz thứ mấy trong lớp ???",
]

right_ans = [44, "About 65", "Nhất",]

answers = [
    {
        "1": 35,
        "2": 36,
        "3": 40,
        "4": 44,
    },
    {
        "1": "About 55",
        "2": "About 65",
        "3": "About 75",
        "4": "About 85",
    },
    {
        "1": "Nhất",
        "2": "Nhất",
        "3": "Nhất",
        "4": "Nhất",
    },
]

t_ans = 0

for i, v in enumerate(questions):
    print(v)
    for k in range(1, 5):
        print(k, answers[i][str(k)], sep = ". ")
    ip_ans = input("Your choice: ")
    if answers[i][ip_ans] == right_ans[i]:
        print("Bingo")
        t_ans += 1
    else:
        print(":(")

print("You correctly answer %s out of %s questions"%(t_ans, len(questions)))