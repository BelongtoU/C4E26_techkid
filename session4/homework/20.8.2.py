'''
Python interpreter's response:

(a) 35
(b) 4
(c) True
(d) keyerror (maybe key not found)=)) - I don't remember exactly =))
(e) 0
(f) ['apples','bananas','oranges','grapes']
(g) like (d)-case =))   

'''

def add_fruit (inventory, fruit, quantity = 0):
    if fruit in inventory:
        inventory[fruit] += quantity
    else:
        inventory[fruit] = quantity
    return inventory

def test (a):
    print (a)

new_inventory = {}
add_fruit (new_inventory, "strawberries", 10)
test ("strawberries" in new_inventory)
test (new_inventory["strawberries"] == 10)
add_fruit (new_inventory, "strawberries", 25)
test (new_inventory["strawberries"] == 35)