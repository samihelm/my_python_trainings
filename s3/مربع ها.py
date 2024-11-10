import turtle

t = turtle.Turtle()
t.color("black")
t.speed(-1)
t.penup()
t.goto(-100,-100)
t.pendown()

size = 20
for i in range(19):
    for j in range(4):
        t.forward(size)
        t.lt(90)
    size=size+20


