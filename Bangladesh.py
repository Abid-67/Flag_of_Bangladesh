# Flag of Bangladesh

import turtle

screen = turtle.Screen()
screen.bgcolor('light blue')
screen.title('Flag of Bangladesh')

t = turtle.Turtle()
t.color('black')

def rectangle(t):
    t.fillcolor('green')
    t.begin_fill()
    for i in range(2):
        t.forward(400)
        t.left(90)
        t.forward(240)
        t.left(90)
    t.end_fill()

def circle(t):
    t.fillcolor('red')
    t.begin_fill()
    t.circle(80)
    t.end_fill()

t.penup()
t.goto(-200, -120)
t.pendown()
rectangle(t)

t.penup()
t.goto(-20, -80)
t.pendown()
circle(t)

turtle.done()