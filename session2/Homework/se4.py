#a.
# for i in range(20):
#     print("*", end = "  ")


#b. 
# n = int(input("Enter your number: "))
# for i in range(n):
#     print("*", end = "  ")


#c.
# print("x ", end = "")
# for i in range(9):
#     print("* x", end = " ")


#d.
# n = int(input("Enter your number: "))
# print("x ", end = "")
# for i in range(n):
#     print("* x", end = " ")


#e.
# print("asdf")
# print()
# print("asdf")


#f.
print()
print()
print("         n columns\n         m rows")
n = int(input("n = "))
m = int(input("m = "))
print()
print()
print("Result:")
print()
for i in range(m):
    print("            ", end = "")
    for x in range(n):
        print("*", end = "    ")
    print("\n")
print()
