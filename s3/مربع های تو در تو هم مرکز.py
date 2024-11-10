import turtle

# تنظیمات اولیه
t = turtle.Turtle()
t.color("black")
t.speed(-1)

# رسم مربع‌های هم‌مرکز
for i in range(60):
    t.forward(i * 10)
    t.right(90)

# پایان کار
turtle.done()
