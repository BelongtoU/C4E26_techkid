1.Boolean value is either True or False 
	3 expression:
		1 == 'Anh'
		2.3 <= 2.0
		a in "TienAnh"
2. flowchart is map of the excutive flow  
3.Nested conditionals means a branch of conditional statement contains another conditional statement
Code:
year = int(input("Enter the year U was born: "))
age = 2019 - year
if age <= 22:
    print("Studying in", end = " ")
    if age < 6:
        print("kindergarten ???")
    elif age < 12:
        print("primary school ???")
    elif age < 16:
        print("secondary school ???")
    elif age < 19:
        print("high school ???")
    else:
        print("university ???")
else:
    print("working ???")