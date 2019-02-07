from turtle import*
size_sh = 100
colors = ["red", "blue", "brown", "yellow", "grey"]

speed(0)
for cl in colors:
    color(cl)
    for _ in range((size_sh//4) + 1):
        left(90)
        forward(size_sh)
        right(90)
        forward(1)
        right(90)
        forward(size_sh)
        left(90)
        forward(1)
        

mainloop()