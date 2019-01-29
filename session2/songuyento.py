n = int(input("Nhap so: "))
count = 0
for i in range(2, n):
    if n%i == 0:
        count += 1 
    else:
        continue
if count == 0:
    print("so nguyen to")
else:
    print("ko phai snt")   