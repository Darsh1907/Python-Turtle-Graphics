import turtle as t
from random_colors import random_color

t.colormode(255)

my_screen=t.Screen()
my_screen.bgcolor('white')

a=t.Turtle()
a.speed(0)

a.shape='circle'

n=0
while n!=360:
    a.setheading(n)
    a.color(random_color())
    a.circle(150)
    n = n+1

my_screen.exitonclick()