import turtle as t
from random_colors import random_color

t.colormode(255)

a=t.Turtle()

a.shape='circle'

n=3
while n!=10:
    a.color(random_color())
    a.circle(100, 360, n)
    n=n+1

screen=t.Screen()
screen.exitonclick()
