from turtle import *

def quadrat(length=50, fillcolor=None):
    if fillcolor:
        color(fillcolor)
        begin_fill()
    else:
        color("black")
    for i in range(4):
        forward(length)
        right(90)
    if fillcolor:
        end_fill()

def kreis(length=3, fillcolor=None):
    if fillcolor:
        color(fillcolor)
        begin_fill
    else:
        color("black")
    for i in range(int(360/length)):
        forward(length)
        left(length)
    if fillcolor:
        end_fill

quadrat(50, "green")
left(180)
penup()
forward(200)
pendown()
left(180)
quadrat(100, "red")
left(90)
penup()
forward(250)
pendown()
quadrat()
right(90)
penup()
forward(250)
pendown()
kreis(2, "yellow")



exitonclick()