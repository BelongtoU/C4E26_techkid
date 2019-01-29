n = int(input("n = "))
# def factorial(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1    
#     elif n > 1:
#         return n*factorial(n-1)
#     else:
#         f = "Vui long nhap so duong !!!"
#         return f
# print("n! = ", factorial(n))

if n == 0:
    print("n! = 0")
elif n == 1:
    print("n! = 1")    
elif n > 1:
    for i in range(n, 1, -1):
        n *= (i-1)
    print("n! =", n)
else:
    print("Vui long nhap so duong !!!")
