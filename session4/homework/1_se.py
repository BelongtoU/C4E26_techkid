prices = {}

prices["banana"] = 4
prices["apple"] = 2
prices["orange"] = 1.5
prices["pear"] = 3

stock = {}

stock["banana"] = 6
stock["apple"] = 0
stock["orange"] = 32
stock["pear"] = 15

for fruit in prices :
    print(fruit, "\nprice:", prices[fruit], "\nstock:", stock[fruit])
    print()
print()
total = 0
for fruit in stock:
    print("If you sell %s, you would make: %s"%(fruit, stock[fruit] * prices[fruit]))
    print()
    total += stock[fruit] * prices[fruit]
print("So, if you sell all of your food, you would make:", total)
