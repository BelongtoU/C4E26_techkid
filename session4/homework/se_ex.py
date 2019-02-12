inventory = {
    'gold': 500,
    'pouch': ['flint', 'twine', 'gemstone',],
    'backpack': ['xylophone', 'dagger', 'bedroll', 'breadloaf',],
}
print()
print()
for i in inventory:
    print("{:9}:   {}".format(i, inventory[i]))
print()
print(10*'--<3--')
print()

# Add a key called 'pocket' and set its value to be a list
inventory['pocket'] = ['seashell', 'strange berry', 'lint', ]
for i in inventory:
    print("{:9}:   {}".format(i, inventory[i]))
print()
print(10*'--<3--')
print()

# .remove('dagger') from the list mapped by 'backpack' key
inventory['backpack'].remove('dagger')
for i in inventory:
    print("{:9}:   {}".format(i, inventory[i]))
print()
print(10*'--<3--')
print()

# Add 50 to the number stored under the 'gold' key
inventory['gold'] += 50
for i in inventory:
    print("{:9}:   {}".format(i, inventory[i]))
print()
print(10*'--<3--')
print()

