clothes = ["T-Shirt", "Sweater"]
bool_var = True
while bool_var:
    act = input("Welcome to our shop, what do you want (C, R, U, D) ??? ")
    if act == "C":
        new_item = input("Enter new item: ")
        clothes.append(new_item)
        print("Our items: ", ', '.join(clothes))
        break
    elif act == "R":
        print("Our items: ", ', '.join(clothes))
        break
    elif act == "U":
        while True:# this loop help user can enter the position again when they fail in the first
            u_p = input("Update position? ")
            if u_p.isdigit():
                u_p = int(u_p)    
                if 0 < u_p <= len(clothes):
                    new_item = input("New item? ")
                    clothes.insert(u_p - 1, new_item)
                    print("Our items: ", ', '.join(clothes))
                    bool_var = False  
                    break
                else:
                    print("Please enter a number from 1 to", len(clothes))
                    print("Your shop only has %s items: "%len(clothes), ', '.join(clothes))
            else:
                print("Please enter a number from 1 to", len(clothes))
    elif act == "D":
        while True:# this loop help user can enter the position again when they fail in the first
            d_p = input("Delete position? ")
            if d_p.isdigit():
                d_p = int(d_p)    
                if 0 < d_p <= len(clothes):
                    clothes.remove(clothes[d_p - 1])
                    print("Our items: ", ', '.join(clothes))  
                    bool_var = False  
                    break  
                else:
                    print("Please enter a number from 1 to", len(clothes))
                    print("Your shop only has %s items: "%len(clothes), ', '.join(clothes))
            else:
                print("Please enter a number from 1 to", len(clothes))
    else:
        print("Please enter C or R or U or D (in upper) !!!")
