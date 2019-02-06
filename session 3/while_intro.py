from random import randint 
x = randint(0, 100)
loop = 0
while loop < 3:
    ip = int(input("Enter a number from 0 to 100: "))
    loop += 1
    if ip < x:
        print("x is bigger !!!")
    elif ip > x:
        print("x is less !!!")
    else:
        print("You win :((")
        print("Congratulate !!!!")
        break
print("Loser :))")