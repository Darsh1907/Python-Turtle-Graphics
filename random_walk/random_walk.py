import turtle as t
from random import choice

t.colormode(255)

a=t.Turtle()
screen=t.Screen()
screen.bgcolor('black')

a.shape='square'
a.speed(0)
a.pensize(10)

from random_colors import random_color

for_direction=[0, 90, 180, 270]

n=0
while n!=1:
    a.color(random_color())
    a.forward(30)
    a.left(choice(for_direction))
    # never ending walk

screen.exitonclick()