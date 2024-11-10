import turtle
turtle.getscreen()
t=turtle.Turtle()
t.speed(-1)
t.pencolor('red')
for i in range(90):
    t.fd(300)
    t.bk(300)
    t.lt(1)
t.lt(90)    
for j in range (90):
     t.forward(300)
     t.bk(300)
     t.lt(1)
