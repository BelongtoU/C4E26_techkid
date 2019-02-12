e_dict = {
    "a.m": "Ante meridiem",
    "p.m": "Post meridiem",
    "AD": "Anno domini",
    "BC": "Before Christ",
    "Jr": "Junior",
    "Dist": "District",
    "St": "Saint",
    "MC": "Master of ceremony",
    "MBA": "Master of Business Administration",
    "Ph.D": "Doctor of Philosophy",
    "VAT": "Value added tax",
    "Ps": "Post Script",
}
print()
print()
for i in e_dict.keys():
    print(i, end = "      ")
print()
print()
while True:
    st = input("What word do U want know ??? ")
    if st in e_dict:
        print()
        print("It's mean:", e_dict[st])
        break
    else:
        print("Please enter a word above !!!")
        print()
        continue
print()
print()