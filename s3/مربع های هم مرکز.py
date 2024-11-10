import turtle
t = turtle.Turtle()
t.color("black")
t.speed(-1)


t.rt(90)
for i in range(21):
    
    t.forward(i * 20)
    t.lt(90)

