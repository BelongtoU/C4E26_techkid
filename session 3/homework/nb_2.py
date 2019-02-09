flock_sheeps = [5, 7, 300, 90, 24, 50, 75]
size_default = 8
size_incr = 50
print("Hello, my name is Tien Anh and my sheeps size is:")
print("         ", flock_sheeps)
print()


print("Now my biggest sheep has size", max(flock_sheeps), "let's shear it !!!")
id_max = flock_sheeps.index(max(flock_sheeps))
flock_sheeps[id_max] = size_default
print("After shearing, here is my flock:")
print("         ", flock_sheeps)
print()
# for i in range(len(flock_sheeps)):
#     flock_sheeps[i] += size_incr
# print()
# print("One month has passed, now here is my flock:")
# print("         ", flock_sheeps)
for i in range(5):
    print("MONTH", i+1, ":")
    for x in range(len(flock_sheeps)):
        flock_sheeps[x] += size_incr
    print("One month has passed, now here is my flock:\n          ", flock_sheeps)
    print("Now my biggest sheep has size", max(flock_sheeps), "let's shear it !!!")
    i_d = flock_sheeps.index(max(flock_sheeps))
    flock_sheeps[i_d] = size_default
    print("After shearing, here is my flock:\n          ", flock_sheeps)
    print()
print()
print("My flock has size in total:", sum(flock_sheeps))
print("I would get %s * 2$ = %s$"%(sum(flock_sheeps), 2*sum(flock_sheeps)))