from turtle import*

colors = ["red", "blue", "brown", "yellow", "grey"]
lenght = 150
speed(0)
pensize(2)
for i in range(len(colors)):
    color(colors[i])
    for _ in range(i+3):
        forward(lenght)
        left(360/(i+3))




mainloop()