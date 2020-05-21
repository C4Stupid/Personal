import turtle
from time import sleep

screen_width = 800
screen_height = 600

# "square" shape is 20x20

# Functions
def at_border (obj):
    border = screen_height/2 - obj.shapesize()[0]*10
    if abs(obj.ycor()) > border:
        obj.sety(border*(2*(obj.ycor() > 0) - 1))
        return True
    return False

def up1():
    if not at_border(p[0]):
        p[0].sety(p[0].ycor() + 20)

def down1():
    if not at_border(p[0]):
        p[0].sety(p[0].ycor() - 20)

def up2():
    if not at_border(p[1]):
        p[1].sety(p[1].ycor() + 20)

def down2():
    if not at_border(p[1]):
        p[1].sety(p[1].ycor() - 20)

# Arena
w = turtle.Screen()
w.title("bong")
w.bgcolor("black")
w.setup(width=screen_width, height=screen_height)
w.tracer(0)

# Paddles
p = [turtle.Turtle(), turtle.Turtle()]
for i in range(2):
    p[i].speed(0)
    p[i].color("white")
    p[i].shape("square")
    p[i].shapesize(stretch_wid=5, stretch_len=1)
    p[i].penup()
    p[i].goto(screen_width/-2 + 50 + (screen_width - 100)*i, 0)

# Ball
b = turtle.Turtle()
b.color("white")
b.shape("square")
b.penup()

# Game
w.listen()
w.onkeypress(up1, "w")
w.onkeypress(down1, "s")
w.onkeypress(up2, "i")
w.onkeypress(down2, "k")

v = [.3, .3]
score = [0, 0]
scorer = turtle.Turtle()
scorer.speed(0)
scorer.ht()
scorer.penup()
scorer.color("white")

while True:
    w.update()
    scorer.clear()
    b.goto(0, 0)
    scorer.goto(0, 250)
    scorer.write(f"{score[0]} {score[1]}", False, align="center", font=("Comic Sans MS", 30, "normal"))

    counter = turtle.Turtle()
    for i in range(3):
        counter.clear()
        counter.goto(0, 150)
        counter.ht()
        counter.color("white")
        counter.write(str(3 - i), False, align="center", font=("Comic Sans MS", 40, "normal"))
        sleep(1)
        w.update()
    counter.clear()

    while True:
        sleep(.001)
        w.update()
        if at_border(b):
            v[1] *= -1
        b.goto(b.pos() + v)

        if b.xcor() > screen_width/2 - 50 - b.shapesize()[1]*10 - p[1].shapesize()[1]*10:
            if abs(b.ycor() - p[1].ycor()) <= b.shapesize()[0]*10 + p[1].shapesize()[0]*10:
                v[0] *= -1
            else:
                score[0] += 1
                break
        if b.xcor() < screen_width/-2 + 50 + b.shapesize()[1]*10 + p[0].shapesize()[1]*10:
            if abs(b.ycor() - p[0].ycor()) <= b.shapesize()[0]*10 + p[0].shapesize()[0]*10:
                v[0] *= -1
            else:
                score[1] += 1
                break