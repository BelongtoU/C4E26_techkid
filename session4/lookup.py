teen_code = {
    "pt": "phat trien",
    "eny": "em nguoi yeu",
    "any": "anh nguoi yeu",
    "stt": "status",
    }
bl = True
while bl:
    for i in teen_code:
        print(i, end = "    ")
    print()
    print("*"*20)
    ip = input("Your code ??? ")
    if ip in teen_code.keys():
        print("Code:", ip)
        print("Translation: ", teen_code[ip])
        break
    else:
        ask  = input("Not found, do U want adtribute a new code (Y/N) ???")        
        if ask == "y":
            trans = input("so, its translation: ")
            teen_code[ip] = trans
            for x in teen_code:
                print(x, end = "    ")
            print()
            break
        elif ask == "n":
            break
        else:
            print("only Yes or No (y/n), please !!!")
            break
