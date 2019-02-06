#yob_str = input("Your year of birth? ")

while True:
    yob_str = input("Your year of birth? ")
    if yob_str.isdigit():
        yob = int(yob_str)
        if 1907 < yob < 2019:
            break
        else:
            print("plzzz enter a number between 1907 and 2019 !!!")
            continue
    print("Only number plsss !!!")
    
age = 2019 - yob
print(age)

